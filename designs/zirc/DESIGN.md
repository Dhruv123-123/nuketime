# ZIRC: two zirconium ideas tested and killed

Small models behind `research/converge/PICK4.md`.

- `zr91_value.py`: one-group textbook estimate on a public 17x17 PWR pin cell. Cladding takes about
  0.3% of thermal absorptions, so stripping Zr-91 frees about 200-340 pcm, a 0.6-1.0% fuel saving at
  2026 prices, about $80-160 per kg Zr, and a world value pool of $160-310M/yr. Output in `zr91_value.out`.
- `hafnium_market.py`: constant-elasticity demand for hafnium with a cost floor, giving a new Western
  producer's revenue-maximising output with and without China's export controls and rival supply.
  Clears $300M/yr in one of eight scenarios. Output in `hafnium_market.out`.
