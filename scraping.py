import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape titles from a webpage and export them to an Excel file
def scrape_titles(url, excel_file):
    try:
        # Send a request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all article titles
        titles = soup.find_all(class_='card')

        # Create a DataFrame to store the titles
        df = pd.DataFrame({'Title': [title.get_text(strip=True) for title in titles]})

        # Export the DataFrame to an Excel file
        df.to_excel(excel_file, index=False)
        print(f"Scraped titles successfully exported to '{excel_file}'")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")

# URL of the webpage to scrape
print("enter the url:")
url = input()

# File path to save the Excel file
excel_file = 'scraped_titles.xlsx'

# Call the function to scrape titles and export them to Excel
scrape_titles(url, excel_file)
