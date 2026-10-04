#impoting banner dependencies
import pyfiglet
import rich
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from pprint import pprint
#Importing the business crawler
from crawler.business_crawler import scrape_business_from_maps, business_site_scraper
import pyperclip
from crawler.utils.text_cleaner import clean_text

from agents.business_details_extraction_agent import extract_business_details
console = Console()

def Banner():
    banner_text_raw_ascii= pyfiglet.figlet_format("Business Research Agent", font="slant")
    banner_text = Text(banner_text_raw_ascii)
    banner_text.stylize("bold cyan")
    banner_panel = Panel(banner_text,
                         title="[bold yellow]v2.4.0[/bold yellow]",
    subtitle="[dim green]System Online[/dim green]",
    border_style="magenta")
    console.print(banner_panel)




if __name__ == "__main__":
    Banner()
    # Get the copied link from the clipboard
    business_link = pyperclip.paste()

    if business_link.startswith("https://www.google.com/maps"):
        business_data = scrape_business_from_maps(business_link)
        pprint(business_data)

        if business_data.get("website"):
            page_content_data = business_site_scraper(business_data["website"])
            with rich.console.Console().status("[bold_blue]Cleaning Page content..."):
                page_content_data["page_content"] = clean_text(page_content_data["page_content"])
            with rich.console.Console().status("[bold_blue]Extracting Business Details..."):
                business_profile = extract_business_details(page_content_data["page_content"])
                business_profile_dict = business_profile.dict()  # Convert to dictionary
                pprint(business_profile_dict)  # Pretty print the dictionary
        else:
            print("No website found for this business.")
    else:
        print("The copied link is not a Google Maps link. Please copy a valid Google Maps business URL.")
