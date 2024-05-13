import pandas as pd

# Fill Country ID cells
df_links = pd.read_csv('data/tl_links.csv')
df_ids = pd.read_csv('data/cids.csv')
df_timeline = pd.read_csv('data/updated_timeline.csv')

df_timeline['CountryID'] = df_timeline['CountryID'].ffill()

# Save
df_timeline.to_csv('data/updated_timeline_v2.csv')

