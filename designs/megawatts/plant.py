"""A PWR secondary cycle at daily resolution, with the slow faults that cost
megawatts and the sensors a plant actually has.

Faults (each may or may not occur in a scenario):
  venturi  feedwater venturi fouling: indicated flow reads high by b, so operators,
           holding indicated thermal power at the licence limit, run the reactor
           b below it
  leak     cycle-isolation leakage: main steam bypasses the turbine to the condenser
  foul     condenser tube fouling: lower heat-transfer coefficient, higher back-pressure
  heater   feedwater heater degradation: lower final feedwater temperature

Everything here is a reduced-order model with textbook sensitivities; magnitudes are
set from published ranges (see DESIGN.md), not from a specific plant.
"""
import numpy as np

LICENSE_MWT = 3411.0
ETA0 = 0.3460          # gross efficiency at design back-pressure
GEN_LOSS = 0.985       # generator efficiency (losses go to air, not condenser)
P_DESIGN = 6.0         # kPa design back-pressure
BP_SENS = 0.0060       # fractional output loss per kPa above design (~2 % per inHg)
HTR_SENS = 0.0009      # fractional output loss per degC of final feedwater deficit
LEAK_ETA = 0.92        # share of a leaking steam flow's work that is lost
CP = 4.186e-3          # MJ/kg/K
DAYS = 730


def psat_kpa(T):
    """Saturation pressure of water, kPa, T in degC (Antoine, 1-100 C)."""
    return 0.133322 * 10 ** (8.07131 - 1730.63 / (233.426 + T))


def ramp(t, t0, dur, size):
    return size * np.clip((t - t0) / max(dur, 1), 0, 1)


class Scenario:
    def __init__(self, seed, faults=("venturi", "leak", "foul", "heater"), p_fault=0.6):
        rng = np.random.default_rng(seed)
        t = np.arange(DAYS)
        self.t = t
        # cooling water inlet temperature: seasonal plus weather
        phase = rng.uniform(0, 2 * np.pi)
        wx = np.convolve(rng.normal(0, 1.2, DAYS + 20), np.ones(7) / 7, "same")[10:-10]
        self.Tcw = 17 + 8 * np.sin(2 * np.pi * t / 365 + phase) + wx
        self.mcw = 45000.0 * rng.uniform(0.95, 1.05)       # kg/s, constant but unknown
        self.UA0 = 120.0 * rng.uniform(0.9, 1.1)           # MW/K clean
        # faults: onset after a 90-day clean baseline
        on = lambda: rng.uniform(100, 600)
        self.truth = {}
        self.b = np.zeros(DAYS); self.leak = np.zeros(DAYS)
        self.foul = np.zeros(DAYS); self.dTh = np.zeros(DAYS)
        if "venturi" in faults and rng.random() < p_fault:
            s = rng.uniform(0.002, 0.015); t0 = on()
            self.b = ramp(t, t0, rng.uniform(60, 240), s); self.truth["venturi"] = (t0, s)
        if "leak" in faults and rng.random() < p_fault:
            s = rng.uniform(0.001, 0.008); t0 = on()       # fraction of steam bypassing
            self.leak = ramp(t, t0, 1, s); self.truth["leak"] = (t0, s)
        if "foul" in faults and rng.random() < p_fault:
            s = rng.uniform(0.05, 0.30); t0 = on()         # fractional loss of UA
            self.foul = ramp(t, t0, rng.uniform(90, 300), s); self.truth["foul"] = (t0, s)
        if "heater" in faults and rng.random() < p_fault:
            s = rng.uniform(1.0, 6.0); t0 = on()           # degC
            self.dTh = ramp(t, t0, 1, s); self.truth["heater"] = (t0, s)
        # fixed sensor calibration errors and slow drift (unknown to everyone)
        self.cal = dict(p1=rng.normal(0, 0.01), cond=rng.normal(0, 0.015))
        self.p1_drift = np.cumsum(rng.normal(0, 0.0015 / np.sqrt(365), DAYS))
        # slow, real output variation no fault model explains (steam-generator fouling,
        # coolant temperature programme, moisture carry-over, correction-curve error):
        # AR(1), sd 0.25 %, ~60-day memory, plus a seasonal correction-curve error
        u = np.zeros(DAYS); a = np.exp(-1 / 60)
        e = rng.normal(0, 0.0025 * np.sqrt(1 - a * a), DAYS)
        for i in range(1, DAYS):
            u[i] = a * u[i - 1] + e[i]
        self.unexpl = u + rng.normal(0, 0.0003) * (self.Tcw - 17)
        # measurement noise drawn once, so re-running with repairs keeps the same noise
        self.noise = {k: rng.normal(0, 1, DAYS) for k in
                      ("gen", "venturi", "p1", "cond", "Tfw", "Pc", "Tin", "Tout")}

    def simulate(self, fixed):
        """fixed: dict fault -> day it was corrected (fault removed from then on).
        Returns (true dict, sensor dict) arrays over all days."""
        t = self.t
        mask = {k: (t < fixed.get(k, np.inf)) for k in ("venturi", "leak", "foul", "heater")}
        b = self.b * mask["venturi"]; leak = self.leak * mask["leak"]
        foul = self.foul * mask["foul"]; dTh = self.dTh * mask["heater"]
        Q = LICENSE_MWT / (1 + b)                   # true thermal power
        # condenser: iterate back-pressure with heat rejected
        eta_htr = 1 - HTR_SENS * dTh
        P = np.full(DAYS, P_DESIGN)
        for _ in range(6):
            eta = ETA0 * (1 - BP_SENS * np.maximum(P - P_DESIGN, -2.0)) * eta_htr
            gen = eta * Q * (1 - LEAK_ETA * leak) * (1 + self.unexpl)
            Qrej = Q - gen / GEN_LOSS
            dT = Qrej / (self.mcw * CP)
            UA = self.UA0 * (1 - foul)
            ttd = dT / (np.exp(UA / (self.mcw * CP)) - 1)
            Ts = self.Tcw + dT + ttd
            P = psat_kpa(Ts)
        msteam = Q / 2.0                             # kg/s per MJ/kg enthalpy rise (relative units)
        N = self.noise
        sens = dict(
            gen=gen * (1 + 0.0015 * N["gen"]),
            venturi=msteam * (1 + b) * (1 + 0.002 * N["venturi"]),
            p1=msteam * (1 - leak) * (1 + self.cal["p1"] + self.p1_drift) * (1 + 0.002 * N["p1"]),
            cond=msteam * (1 + self.cal["cond"]) * (1 + 0.006 * N["cond"]),
            Tfw=226.0 - dTh + 0.3 * N["Tfw"],
            Pc=P * (1 + 0.01 * N["Pc"]),
            Tin=self.Tcw + 0.1 * N["Tin"],
            Tout=self.Tcw + dT + 0.1 * N["Tout"],
        )
        true = dict(Q=Q, gen=gen, P=P, b=b, leak=leak, foul=foul, dTh=dTh)
        return true, sens

    def ideal_gen(self):
        """Generator output with no faults, for the lost-MWh account."""
        z = Scenario.__new__(Scenario); z.__dict__ = dict(self.__dict__)
        z.b = z.leak = z.foul = z.dTh = np.zeros(DAYS)
        tr, _ = z.simulate({})
        return tr["gen"]
