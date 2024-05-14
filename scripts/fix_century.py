import pandas as pd
import re

def convert_century(year_str):
    match = re.match(r'(\d+)(st|nd|rd|th)? Century', year_str)
    if match:
        century = int(match.group(1))
        if 'bc' in year_str.lower():
            return -(century * 100 - 1)
        else:
            return century * 100
    else:
        return None

df = pd.read_csv('data/updated_timeline_v3.csv', index_col=0)

df_cy = df['ConvertedYear'] 
df['ConvertedYear'] = df['EventYear'].apply(convert_century)

# Fill missing na with values from 'ConvertedYear'
df["ConvertedYear"].fillna(df_cy, inplace=True)

# Output to dataset new version
df.to_csv('data/final_timeline.csv')
