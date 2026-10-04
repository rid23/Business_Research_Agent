# Business Research Agent

An automated tool that scrapes business information from Google Maps and the business's website, then uses Google Gemini to extract a structured business profile.

## How It Works

1. **Clipboard Input** — Reads a Google Maps business URL from the system clipboard.
2. **Google Maps Scraping** — Uses Playwright to open the Maps page and extract the business name, address, phone number, and website link.
3. **Website Scraping** — If a website is found, visits it and extracts the full page text and all hyperlinks.
4. **Text Cleaning** — Strips extra whitespace, blank lines, and noise from the scraped content.
5. **AI-Powered Extraction** — Sends the cleaned text to Google Gemini 2.5 Flash via LangChain, which returns a structured `BusinessProfile` (name, industry, services, target customers, description).

## Project Structure

```
business_research_agent/
├── main.py                              # Entry point — orchestrates the full workflow
├── pyproject.toml                       # Dependencies and project metadata
├── crawler/
│   ├── business_crawler.py              # Playwright scraper for Google Maps + business websites
│   ├── business_data_schemas.py         # Pydantic models for crawler output (placeholder)
│   └── utils/
│       └── text_cleaner.py              # Text normalization utility
├── agents/
│   ├── business_details_extraction_agent.py  # LangChain + Gemini structured extraction agent
│   ├── agent_schemas.py                 # BusinessProfile Pydantic schema
│   ├── sample_data.py                   # Sample website content for standalone testing
│   └── .env                             # API keys (GOOGLE_API_KEY)
└── README.md
```

## Prerequisites

- Python 3.14+
- A Google Gemini API key (set as `GOOGLE_API_KEY` in `agents/.env`)
- Playwright Chromium browser installed

## Installation

```bash
# Install dependencies (using uv)
uv sync

# Install Playwright browsers
playwright install chromium
```

## Usage

1. Copy a Google Maps business URL to your clipboard (e.g., `https://www.google.com/maps/place/...`)
2. Run the script:

```bash
python main.py
```

3. The script will:
   - Display a banner
   - Scrape the Maps page for business details
   - Visit the business website (if available) and scrape its content
   - Use Gemini AI to extract a structured profile
   - Print the results to the console

### Example Output

```
Business Name: Social Chanakya
Address: 1st Floor, Mamatalay, MC Garden Road, Dum Dum, Kolkata
Phone: +91 844 66 844 36
Website: https://socialchanakya.com

{
  "business_name": "Social Chanakya",
  "business_industry": "Digital Marketing Agency",
  "business_services": ["SEO", "Google Ads", "Meta Ads", "Performance Marketing", ...],
  "target_customers": "Businesses in Kolkata and across India",
  "business_description": "A digital marketing agency helping businesses improve online visibility..."
}
```

## Configuration

| Variable | Location | Description |
|---|---|---|
| `GOOGLE_API_KEY` | `agents/.env` | Google Gemini API key for the extraction agent |

## Technologies

- **Playwright** — Browser automation for scraping Google Maps and websites
- **LangChain** — LLM orchestration framework
- **Google Gemini 2.5 Flash** — Structured information extraction
- **Pydantic** — Data validation and schema definition
- **Rich** — Terminal UI (banner, status indicators)
- **pyperclip** — Clipboard access
- **pyfiglet** — ASCII art banner
