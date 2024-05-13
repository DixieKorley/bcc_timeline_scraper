import pandas as pd
import re

# Load the data
df = pd.read_csv('data/all_timeline.csv')

# Function for converting the year
def convert_year(year_str):
    year_str = year_str.lower().strip()

    # Check for bc in EventYear value
    if 'bc' in year_str:
        year = re.findall(r'\d+', year_str)
        return -int(year[0]) if year else None
    
    # For AD
    elif 'ad' in year_str:
        year = re.findall(r'\d+', year_str)
        return int(year[0]) if year else None

    # Check for - in EventYear value
    elif '-' in year_str:
        first_year = year_str.split('-')[0].strip()
        return int(first_year) if first_year.isdigit() else None
    # Check for if Event Year has a digit
    elif year_str.isdigit():
        return int(year_str)
    return None

# Go on each row and apply the convert year function
df['ConvertedYear'] = df['EventYear'].apply(convert_year)

# Fill NaN values with values before
df['ConvertedYear'] = df['ConvertedYear'].ffill()

# Make the year table
unique_yrs = pd.DataFrame(df['ConvertedYear'].dropna().unique(), columns=['EventYear'])
unique_yrs = unique_yrs.sort_values(by='EventYear').reset_index(drop=True)

# Save as CSV
unique_yrs.to_csv('data/years.csv', index=False)
df.to_csv('data/updated_timeline.csv', index=False)


