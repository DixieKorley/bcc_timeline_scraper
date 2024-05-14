import pandas as pd

# Load CSVs
df2 = pd.read_csv('data/cids.csv')
df = pd.read_csv('data/raw_timeline.csv')

# Merge
df_merged = pd.merge(df, df2, on="CountryName", how='left')

# Check for errors
missing_ids = df_merged[df_merged['CountryID'].isnull()]
if not missing_ids.empty:
    print("No matching CountryID for these rows")
    print(missing_ids)

# Save as CSV
df_merged.to_csv('data/all_timeline.csv', index=False)