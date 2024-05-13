from bs4 import BeautifulSoup
import requests as rq
import warnings
import pandas as pd

# List of African countries
african_countries = ["Algeria", "Angola", "Benin", "Botswana", "British Indian Ocean Territory", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde", "Central African Republic", "Chad", "Comoros", "Congo", "Cote D'Ivoire (Ivory Coast)", "Democratic Republic of Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "French Southern Territories", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Mayotte", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Saint Helena", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Western Sahara", "Zambia", "Zimbabwe"]

# For SSL warnings. If you are using your company laptop you can comment this out, including `import warnings`
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

def extract_links(url):
    # Send request and get response
    page = rq.get(url, verify=False)
    # Parse HTML
    soup = BeautifulSoup(page.text, "html.parser")

    # Find all option tags with a specific attribute
    options = soup.find_all('option')

    # For the list of links we collect
    values = []
    for option in options:
        # Text strip to match with country name
        country_name = option.text.strip()
        # Extract the value attribute from each option
        value = option.get('value')
        if country_name in african_countries and 'middle_east' in value.lower():
            values.append([country_name, value])
        if country_name in african_countries and 'africa' in value.lower():
            values.append([country_name, value])
    return values

# Get links from homepage for country profiles
url = "http://news.bbc.co.uk/2/hi/country_profiles/default.stm"
values = extract_links(url)

# Turn into a dataframe
df = pd.DataFrame(values, columns=["CountryName", "Links"])
df.to_csv("data/tl_links.csv", index=False)