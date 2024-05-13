import pandas as pd
from bs4 import BeautifulSoup
import requests as rq
import warnings

# For SSL warnings. If you are using your company laptop you can comment this out, including `import warnings`
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# Function to scrape timeline
def scrape_timeline(url):
    # First, get the html
    page = rq.get(url, verify=False)
    soup = BeautifulSoup(page.text, "html.parser")

    # Locate main > article tags, where text is located
    main_content = soup.find('main')
    articles = main_content.find_all('article')

    # For collecting text needed
    events = []

    # To help avoid text not needed
    collect = False

    
    for article in articles:
        text_blocks = article.find_all('div', attrs={'data-component': 'text-block'})
        for block in text_blocks:
            text = block.get_text(strip=True)
            if text.startswith("Some key date"):
                collect = True
                continue
            if collect:
                events.append(text)
    return events


# Going to go over each link
def collect_data(df):
    tl = []
    for index, row in df.iterrows():
        events = scrape_timeline(row["Links"])
        for event in events:
            tl.append(event.strip().split("- ", 1)) 
            tl[-1].append(row['CountryName'])
            tl[-1].append(row['Links'])
        print(tl)
    return tl


# Load CSV
df = pd.read_csv('data/tl_links.csv')
collect_data(df)

#  Collect all timeline data
events_data = collect_data(df)

# Convert to dataframe
events_df = pd.DataFrame(events_data, columns=["EventYear", "EventDescription", "CountryName", "EventLink"])

# Save to DSV
events_df.to_csv('data/raw_timeline_test.csv', index=False)