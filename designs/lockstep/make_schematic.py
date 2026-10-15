import json
T = json.load(open("runs/tower.json"))["cases"]["scale1.0_dc500"]
svg = []
W, Hh = 1100, 760
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" font-family="DejaVu Sans, Helvetica, Arial, sans-serif" font-size="12">')
svg.append('''<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#52514e"/></marker>
<marker id="arrb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#1c5cab"/></marker>
<marker id="arro" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#b2431a"/></marker></defs>''')
svg.append(f'<rect width="{W}" height="{Hh}" fill="#fcfcfb"/>')
svg.append('<text x="20" y="28" font-size="16" font-weight="bold" fill="#0b0b0b">LOCKSTEP: a PWR and a data centre engineered as one island (electrical one-line above, heat rejection below)</text>')
svg.append('<text x="20" y="46" fill="#52514e">1,180 MWe gross PWR with a 520 MW liquid-cooled data centre. Three provisions: island on the data-centre load, share the cooling tower, tie the data-centre backup fleet to the plant safety buses.</text>')
def box(x, y, w, h, title, lines=(), fill="#f0efec", stroke="#52514e", tcol="#0b0b0b"):
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
    if title:
        svg.append(f'<text x="{x+w/2}" y="{y+17}" text-anchor="middle" font-size="11.5" font-weight="bold" fill="{tcol}">{title}</text>')
    for i, l in enumerate(lines):
        svg.append(f'<text x="{x+w/2}" y="{y+32+i*13}" text-anchor="middle" font-size="10" fill="#52514e">{l}</text>')
def line(x1, y1, x2, y2, col="#52514e", w=2, marker="arr", dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"{d}{m}/>')
def label(x, y, t, col="#52514e", size=10, anchor="middle", bold=False):
    fw = ' font-weight="bold"' if bold else ''
    svg.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{col}"{fw}>{t}</text>')
svg.append('<rect x="20" y="66" width="1060" height="322" fill="none" stroke="#c3c2b7" stroke-dasharray="4 3"/>')
label(30, 82, "ELECTRICAL", "#52514e", 10.5, "start", True)
box(40, 120, 120, 70, "Reactor + SGs", ["3,400 MWth", "rods, dump, runback"])
box(190, 120, 120, 70, "Turbine", ["fast valving", "droop + island freq. control"])
box(340, 120, 110, 70, "Generator", ["1,300 MVA", "H = 5.5 s"])
line(160, 155, 190, 155); line(310, 155, 340, 155)
line(450, 155, 520, 155, marker=None)
svg.append('<circle cx="520" cy="155" r="4" fill="#0b0b0b"/>')
box(560, 130, 26, 50, "", fill="#fcfcfb"); label(573, 123, "GCB", size=9)
line(520, 155, 560, 155, marker=None); line(586, 155, 640, 155, marker=None)
box(640, 125, 100, 60, "Main transformer", ["24 / 345 kV"])
line(740, 155, 800, 155, marker=None)
box(800, 125, 110, 60, "Switchyard", ["345 kV"])
line(910, 155, 1000, 155, marker=None); box(1000, 130, 60, 50, "Grid", fill="#e6e5e1")
label(955, 145, "opens on grid loss", "#b2431a", 9)
svg.append('<line x1="950" y1="140" x2="965" y2="170" stroke="#b2431a" stroke-width="2"/>')
line(520, 155, 520, 246, marker=None)
box(460, 246, 120, 50, "Unit aux. transformer", ["house load 60 MW"])
line(520, 296, 520, 330, marker=None)
box(400, 330, 120, 46, "Non-safety buses", ["RCPs, feed, CW pumps"], fill="#f7f6f2")
box(540, 330, 130, 46, "Safety buses A / B", ["ESF loads, 2 × EDG"], fill="#dbe7f7", stroke="#1c5cab")
line(520, 330, 460, 330, marker=None); line(520, 330, 605, 330, marker=None)
line(520, 155, 520, 106, marker=None); line(520, 106, 760, 106, marker=None)
box(760, 70, 130, 48, "DC feeder transformer", ["24 / 34.5 kV, 600 MVA"])
line(890, 106, 930, 106, marker=None); line(930, 106, 930, 210, marker=None)
box(870, 210, 190, 90, "Data centre 520 MW", ["liquid-cooled AI halls", "UPS batteries 520 MW / 10 min", "gensets N+1, 560 MW"], fill="#fdeee4", stroke="#b2431a")
line(870, 280, 700, 280, col="#1c5cab", marker=None, dash="6 4")
line(700, 280, 700, 353, col="#1c5cab", marker="arrb", dash="6 4")
line(700, 353, 672, 353, col="#1c5cab", marker="arrb", dash="6 4")
svg.append('<circle cx="700" cy="280" r="4" fill="#1c5cab"/>')
label(860, 268, "normally open diverse-AC tie: gensets + batteries", "#1c5cab", 9, "end")
label(860, 298, "sync-check, seismically qualified breaker", "#1c5cab", 9, "end")
svg.append('<rect x="20" y="400" width="1060" height="330" fill="none" stroke="#c3c2b7" stroke-dasharray="4 3"/>')
label(30, 416, "HEAT REJECTION", "#52514e", 10.5, "start", True)
box(40, 450, 130, 70, "Condenser", ["2,000 MWth", "TTD 3 K"])
box(300, 440, 150, 90, "Natural-draft tower", ["43,400 kg/s water", "design 25.6 °C WB", "approach 5.4 K"])
box(620, 450, 150, 70, "Plate heat exchangers", ["2 K pinch", "open CW / closed DC loop"])
box(870, 450, 190, 70, "Data centre cooling loop", ["520 MW at 12 K rise", f"supply ≤ {T['dc_supply_p99']:.0f} °C 99 % of hours"], fill="#fdeee4", stroke="#b2431a")
line(170, 470, 300, 470, col="#b2431a", w=3, marker="arro"); label(235, 462, "hot return 42 °C", "#b2431a", 9)
line(620, 470, 450, 470, col="#b2431a", w=3, marker="arro"); label(535, 462, "DC heat joins hot return", "#b2431a", 9)
line(870, 470, 770, 470, col="#b2431a", w=3, marker="arro")
line(300, 505, 170, 505, col="#1c5cab", w=3, marker="arrb"); label(235, 522, "cold water 31 °C design", "#1c5cab", 9)
line(450, 505, 620, 505, col="#1c5cab", w=3, marker="arrb"); label(535, 522, "12 m³/s tapped (28 %)", "#1c5cab", 9)
line(770, 505, 870, 505, col="#1c5cab", w=3, marker="arrb")
label(375, 560, "plant penalty: 7.6 MW average", "#0b0b0b", 10, "middle", True)
label(375, 574, f"(0.6 %), max cold water {T['Tcold_max']:.1f} °C", "#52514e", 9.5)
label(965, 560, "data centre: no towers, no dry coolers,", "#0b0b0b", 10, "middle", True)
label(965, 574, "no chillers; 20 MW of fans avoided", "#52514e", 9.5)
box(40, 610, 1020, 100, "What the island gives each party", [
    "Plant: rides through grid loss without a reactor trip (needs data-centre load ≥ 40 % of rating with a 40 % steam dump); station-blackout core-damage frequency ÷ 190 with both provisions",
    "Data centre: firm nuclear power that survives the grid, water at 26 to 35 °C from the plant's tower, and $125 M of cooling plant not built",
    "Both: one switchyard interface, one water permit, one control room watching the island; the reactor never manoeuvres for the grid, only for the island"], fill="#f7f6f2")
svg.append('</svg>')
open("figures/schematic.svg", "w").write("\n".join(svg))
print("schematic written")
