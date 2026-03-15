#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def scrape_vehicle_details(vehicle_url):
    """Scrape details from an individual vehicle listing."""
    try:
        response = requests.get(vehicle_url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract details from the 'Vehicle Details' section
        details = {
            "Year": soup.select_one("li.dt-start span.gray").get_text(strip=True) if soup.select_one("li.dt-start span.gray") else "N/A",
            "Make": soup.select_one("li.p-manufacturer span.gray").get_text(strip=True) if soup.select_one("li.p-manufacturer span.gray") else "N/A",
            "Model": soup.select_one("li.p-model span.gray").get_text(strip=True) if soup.select_one("li.p-model span.gray") else "N/A",
            "Transmission": soup.select_one("li.p-transmission span.gray").get_text(strip=True) if soup.select_one("li.p-transmission span.gray") else "N/A",
            "Odometer": soup.select_one("li.p-odometer span.gray").get_text(strip=True) if soup.select_one("li.p-odometer span.gray") else "N/A",
            "Price": soup.select_one("li.p-price span.red").get_text(strip=True) if soup.select_one("li.p-price span.red") else "N/A",
            "Location": soup.select_one("li.p-address span.gray").get_text(strip=True) if soup.select_one("li.p-address span.gray") else "N/A",
            "Condition": soup.select_one("li.p-condition span.gray").get_text(strip=True) if soup.select_one("li.p-condition span.gray") else "N/A",
        }
        return details
    except Exception as e:
        print(f"Error scraping {vehicle_url}: {e}")
        return None

def scrape_listings(base_url):
    """Scrape all vehicle listings across all pages."""
    all_data = []
    page_number = 1
    while True:
        try:
            url = f"{base_url}?page={page_number}"
            print(f"Scraping page {page_number}: {url}")
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Find all individual listing links
            listing_links = [
                "https://classiccars.com" + a["href"]
                for a in soup.select(".panel-mod a")
                if "href" in a.attrs
            ]
            print(f"Found {len(listing_links)} listings on page {page_number}.")

            if not listing_links:
                print("No more listings found. Ending scrape.")
                break
            
            # Scrape each individual listing
            for link in listing_links:
                details = scrape_vehicle_details(link)
                if details:
                    all_data.append(details)

            page_number += 1
            # Random delay to avoid detection
            time.sleep(random.uniform(1, 3))
        except Exception as e:
            print(f"Error scraping page {page_number}: {e}")
            break

    return all_data

def main():
    base_url = "https://classiccars.com/listings/find/1920-2000"
    data = scrape_listings(base_url)

    # Save data to CSV
    df = pd.DataFrame(data)
    df.to_csv("classic_cars_full.csv", index=False)
    print(f"Scraping complete! Data saved to 'classic_cars_full.csv'.")

if __name__ == "__main__":
    main()


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_vehicle_details(detail_url):
    """Scrape the vehicle details from an individual listing page."""
    try:
        print(f"Scraping details from {detail_url}...")
        response = requests.get(detail_url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract vehicle details
        details = {
            "Year": soup.select_one("li.dt-start span.gray").text.strip() if soup.select_one("li.dt-start span.gray") else "N/A",
            "Make": soup.select_one("li.p-manufacturer span.gray").text.strip() if soup.select_one("li.p-manufacturer span.gray") else "N/A",
            "Model": soup.select_one("li.p-model span.gray").text.strip() if soup.select_one("li.p-model span.gray") else "N/A",
            "Transmission": soup.select_one("li.p-transmission span.gray").text.strip() if soup.select_one("li.p-transmission span.gray") else "N/A",
            "Odometer": soup.select_one("li.p-odometer span.gray").text.strip() if soup.select_one("li.p-odometer span.gray") else "N/A",
            "Price": soup.select_one("li.p-price span.red").text.strip() if soup.select_one("li.p-price span.red") else "N/A",
            "Location": soup.select_one("li.p-address span.gray").text.strip() if soup.select_one("li.p-address span.gray") else "N/A",
            "Condition": soup.select_one("li.p-condition span.gray").text.strip() if soup.select_one("li.p-condition span.gray") else "N/A",
        }
        print(f"Details extracted: {details}")
        return details

    except Exception as e:
        print(f"Error scraping {detail_url}: {e}")
        return None


def scrape_listings(base_url):
    """Dynamically scrape all listing pages and extract vehicle details."""
    all_vehicle_data = []
    page_num = 1

    while True:
        try:
            print(f"Scraping page {page_num}...")
            listing_page_url = f"{base_url}?page={page_num}"
            response = requests.get(listing_page_url, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            listing_links = [
                "https://classiccars.com" + a["href"]
                for a in soup.select(".flexbox.fx-justify.fx-va-top.panel-mod a[href]")
            ]
            print(f"Found {len(listing_links)} listings on page {page_num}.")

            if not listing_links:
                print("No more listings found. Ending scrape.")
                break

            for link in listing_links:
                details = scrape_vehicle_details(link)
                if details:
                    all_vehicle_data.append(details)
                time.sleep(2)  # Be polite and avoid overloading the server

            page_num += 1

        except Exception as e:
            print(f"Error scraping page {page_num}: {e}")
            break

    return all_vehicle_data


def main():
    base_url = "https://classiccars.com/listings/find/1920-2000"

    # Scrape data
    vehicle_data = scrape_listings(base_url)

    # Save to CSV
    if vehicle_data:
        df = pd.DataFrame(vehicle_data)
        df.to_csv("classic_cars_details.csv", index=False)
        print("Scraping complete! Data saved to classic_cars_details.csv.")
    else:
        print("No data scraped.")


# Run the scraper
if __name__ == "__main__":
    main()


# In[5]:


import pandas as pd

# Load the data from the CSV file
data = pd.read_csv("Updated_Classic_Cars_Data.csv")

# Define a function to determine the condition based on odometer
def update_condition(Odometer):
    if Odometer < 10000:
        return "Concourse"
    elif Odometer < 50000:
        return "Excellent"
    elif Odometer < 100000:
        return "Good"
    else:
        return "Fair"

# Apply the function to the 'odometer' column and update the 'condition' column
data['condition'] = data['Odometer'].apply(update_condition)

# Save the updated data to a new CSV file
data.to_csv("Updated_Classic_Cars_Data_with_Conditions.csv", index=False)

print("Condition column updated and saved to 'Updated_Classic_Cars_Data_with_Conditions.csv'")


# In[ ]:
