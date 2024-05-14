import pandas as pd


df1 = pd.read_csv('data/updated_timeline_v2.csv')
df1['EventYear'] = df1['EventYear'].str.encode('utf-8').str.decode('ascii', 'ignore')
df1 = df1.rename(columns={'Unnamed: 0': 'EventID', '': 'EventID'})

l = len(df1)

def shift_cells(df):
    for i in range(l):
        if type(df['EventLink'][i]) == float:
            df.loc[i, 'EventLink'] =  df['CountryName'][i]
            df.loc[i, 'CountryName'] = df['EventDescription'][i]
            df.loc[i, 'EventDescription'] = df['EventYear'][i]
            df.loc[i, 'EventYear'] = df['EventYear'][i-1] 
    return df

final = shift_cells(df1)
final.to_csv('data/updated_timeline_v3.csv')