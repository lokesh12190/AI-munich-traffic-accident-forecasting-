<!-- .github/copilot-instructions.md -->
# Copilot / AI Agent Instructions

Short, actionable guidance so an AI coding agent can be immediately productive in this repository.

## Big picture
- This repository is a small analysis project centered on a single Jupyter notebook: `main.ipynb`.
- Primary data source: `monatszahlen2510_verkehrsunfaelle_30_10_25.csv` (present at the repo root). The notebook loads and visualizes this CSV using pandas and plotting libs.

## Key files & patterns
- `main.ipynb` — the single source of code and analysis. It imports: `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`.
- No `requirements.txt`, no tests, no CI configuration — assume an ad-hoc developer workflow driven by the notebook.

## Project-specific gotchas (do these first)
- CSV path bug (frequent fix): in `main.ipynb` there is a wrong string literal used when reading the CSV: the line currently looks like:

```python
data = pd.read_csv('rC:\Users\lokes\Desktop\unternehmer tum project\monatszahlen2510_verkehrsunfaelle_30_10_25.csv')
```

Fixes (pick one):
- Use a raw string literal prefix outside the quotes: `pd.read_csv(r'C:\Users\lokes\Desktop\unternehmer tum project\monatszahlen2510_verkehrsunfaelle_30_10_25.csv')`
- Prefer a relative path (recommended for portability): `pd.read_csv('monatszahlen2510_verkehrsunfaelle_30_10_25.csv')` (the notebook's working dir is repo root in VS Code by default)
- Or use pathlib where converting to scripts: `from pathlib import Path; pd.read_csv(Path(__file__).parent / 'monatszahlen2510_verkehrsunfaelle_30_10_25.csv')`

## How to run & validate changes
- Open `main.ipynb` in VS Code or JupyterLab. Select a Python kernel with pandas/numpy/matplotlib/seaborn installed.
- Typical PowerShell dev setup (example):

```powershell
python -m venv .venv; .venv\Scripts\Activate.ps1; pip install pandas numpy matplotlib seaborn
```

- After edits to the notebook: restart kernel and run all cells top-to-bottom to ensure no import/path errors and figures render.

## Editing guidelines for agents
- Keep changes minimal and notebook-oriented when possible (this is primarily an analysis notebook, not a library).
- If you extract reusable code into .py files, add a short README or `requirements.txt` documenting runtime dependencies, and put data in a `data/` folder.
- When fixing the CSV path, update the single cell that loads data and re-run the notebook to verify.

## Conventions & style seen in this repo
- Visual style: use seaborn/matplotlib for plots; code currently relies on in-notebook cell execution order; prefer explicit cell initialization (imports + config) at the top.
- File names are long and descriptive (German text). Preserve original CSV name when altering code.

## Facts an agent should not assume
- There is no test suite or CI — don't assume automated checks exist.
- No existing packaging, so changes that introduce packages should include an updated `requirements.txt` or instructions in a short README.

## Example fixes / PR message suggestions
- PR title: "Fix CSV path and make data loading robust"
- PR body (short): "Fix CSV raw-string path in `main.ipynb`, prefer relative path so notebook runs in repo root; added short note on requirements. Verified by running all cells top-to-bottom."

---

If anything is unclear or you want this expanded (for example, to include a `requirements.txt` template or a small data validation script and tests), tell me which direction and I'll update this file. ✅
