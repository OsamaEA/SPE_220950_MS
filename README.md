Code for Research Paper SPE-220950-MS "Reference Synthetic Dataset for Drilling Inventory Optimization" - presented at ATCE "Annual Techincal Conference and Exhibition" in New Orleans, USA, in September 2024

# Drilling Inventory & Transactions Simulator

A Python simulation that generates 23 years of drilling activity, inventory **receptions**, field **issues**, and **returns**, producing a time-ordered transaction history per SKU and a printable PDF of item timelines.

The workflow models realistic oilfield logistics (drilling prep → casing/tubular → wellhead → completion tubular/equipment → Xmas tree), with randomized yet constrained behavior (lead times, obsolescence, re-issues, side tracks, etc.). The simulator enforces sensible ordering and ensures nothing is issued before it has ever been received.

---

## Features

- **Drilling program generator (2000–2023)** based on inflation-adjusted oil prices.
- **Inventory entries (PO receptions)** with weighted categories and per-category sub-specs.
- **Field activity engine** that schedules **issues** and **returns** by well and operation stage.
- **SKU realization**: converts generic categories into concrete stock keeping units.
- **Obsolescence & substitution logic**: prevents issuing obsolete SKUs; substitutes compatible SKUs when needed.
- **Integrity constraints**: prevents issuing items before reception; enforces tubular sequencing constraints.
- **Export**: creates `output_tables.pdf` with color-coded transaction tables by item.

---

## Getting Started

### 1) Environment

```bash
# Python 3.9
python -m venv .venv
# Windows PowerShell users may need to allow script execution:
#   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
#   .\.venv\Scripts\Activate.ps1
source .venv/bin/activate  # (Linux/macOS)
pip install -r requirements.txt
