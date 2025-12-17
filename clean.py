import sys, pandas as pd, pathlib
in_path = pathlib.Path(sys.argv[1]); out_path = pathlib.Path(sys.argv[2])
out_path.parent.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(in_path)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.drop_duplicates()
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
df = df.sort_values('date')
df.to_csv(out_path, index=False)
print(f"Saved cleaned file -> {out_path}")
