from playwright.sync_api import Page , sync_playwright
import pyperclip
from rich.console import Console
from pprint import pprint


console = Console()

def scrape_business_from_maps(map_url):
    """
    Scrape business data from Google Maps URL.

    Args:
        map_url (str): The Google Maps URL of the business.
        """
    with console.status("[bold green]Scraping business data from Google Maps..."):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(map_url)

            # Wait for the business name to load
            page.wait_for_selector("xpath=//h1[@class='DUwDvf lfPIob']")

            # Extract business data
            business_name = page.locator("xpath=//h1[@class='DUwDvf lfPIob']").inner_text()
            pprint(f'Business Name: {business_name}')

            address = page.locator("xpath=(//div[@class='rogA2c ']//div)[1]").inner_text()
            

            phone_number = page.locator("xpath=(//div[@class='rogA2c ']//div)[4]").inner_text()
            

            try:
                website = page.locator("xpath=(//a[@data-tooltip='Open website'])[1]").get_attribute('href')
            except:
                website = None

            # Close the browser
            browser.close()

        return {
            "business_name": business_name,
            "address": address,
            "phone_number": phone_number,
            "website": website
        }

def business_site_scraper(site_link):


    with console.status("[bold green]Scraping business site..."):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(site_link)

            page_content = page.locator("body").inner_text()

            #2.Extract all the links
            links = page.locator("a")
            links_count = links.count()
            all_links = []
            for i in range(links_count):
                link = links.nth(i).get_attribute("href")
                if link:
                    all_links.append(link)
            pprint(f'Number of links found: {links_count}')

        return {
            "page_content": page_content,
            "links": all_links
        }

if __name__ == "__main__":
    business_link = pyperclip.paste()
    print("The copied link is : ", business_link)
    if business_link.startswith("https://www.google.com/maps"):
        business_data = scrape_business_from_maps(business_link)
        pprint(business_data)

    else:
        print("The copied link is not a Google Maps link. Please copy a valid Google Maps business URL.")

    '''
        page_content_data = business_site_scraper(business_link)
        print(page_content_data)
    '''

        