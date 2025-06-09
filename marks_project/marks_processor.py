import pandas as pd
from pathlib import Path

INPUT_FILE  = "marks_input.xlsx"
OUTPUT_DIR  = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "marks_report.xlsx"

df = pd.read_excel(INPUT_FILE)

mark_cols = df.columns[2:]          
df["Total"]   = df[mark_cols].sum(axis=1)
df["Average"] = (df["Total"] / len(mark_cols)).round(2)

def get_grade(avg):
    if avg >= 80: return "A+"     
    elif avg >= 75: return "A"
    elif avg >= 70: return "A-"
    elif avg >= 65: return "B+"
    elif avg >= 60: return "B"
    elif avg >= 55: return "B-"
    elif avg >= 50: return "C+"
    elif avg >= 45: return "C"
    elif avg >= 40: return "D"
    else: return "F"

df["Grade"] = df["Average"].apply(get_grade)

OUTPUT_DIR.mkdir(exist_ok=True)

df.to_excel(OUTPUT_FILE, index=False)

print(f"Report generated → {OUTPUT_FILE}")
