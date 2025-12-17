import sys, pandas as pd
path = sys.argv[1]
df = pd.read_csv(path, parse_dates=['date'])
total = len(df)
applied = (df['stage'].str.lower() == 'applied').sum()
conversion = (applied/total*100) if total else 0
print({"total_records": int(total), "applied": int(applied), "conversion_pct": round(conversion,2)})
