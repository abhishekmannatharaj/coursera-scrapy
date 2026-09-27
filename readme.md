# Ebook Scraper

A web scraping project built with **Scrapy** and managed via **uv** to extract book data from Coursera/target websites.

<img width="1914" height="917" alt="image" src="https://github.com/user-attachments/assets/1abb7904-9acc-4941-ad07-92216e98b9eb" />

<img width="1226" height="803" alt="image" src="https://github.com/user-attachments/assets/97ecb079-c522-4f56-9936-e708f0c62b60" />

<img width="1145" height="670" alt="image" src="https://github.com/user-attachments/assets/26ada04e-550f-4dfe-be53-b9b1bc6dd6fb" />

## 🛠️ Prerequisites

Ensure you have [uv](https://github.com) installed on your system.

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd scrapy-coursera
```

### 2. Set Up the Virtual Environment
Create and activate the virtual environment using `uv`:
```powershell
# Create the environment
uv venv

# Activate on Windows (PowerShell)
.venv\Scripts\activate
```

### 3. Install Dependencies
Install Scrapy and required packages using `uv pip`:
```bash
uv pip install scrapy
```

## 💻 Usage

### Create a New Spider
Navigate to your project directory and generate a spider:
```bash
cd ebook_scraper
scrapy genspider ebook_spider ://toscrape.com
```

### Run the Crawler
To run your spider and export the scraped data into a structured file format (e.g., CSV or JSON):

```bash
# Export to CSV
scrapy crawl ebook_spider -o output.csv

# Export to JSON
scrapy crawl ebook_spider -o output.json
```

## 📂 Project Structure
```text
scrapy-coursera/
├── .venv/               # Virtual environment
├── .gitignore          # Git ignore patterns
├── README.md           # Project documentation
└── ebook_scraper/      # Scrapy project root
    ├── scrapy.cfg      # Scrapy configuration file
    └── ebook_scraper/  # Project's Python module
        ├── items.py
        ├── middlewares.py
        ├── pipelines.py
        ├── settings.py
        └── spiders/     # Directory for your custom spiders
```








# Advanced Web Crawling & Scraping Suite

A collection of Scrapy learning projects covering book extraction, table parsing, product details, and desktop crawler integration.

## Repository Structure

- `ebook_scraper/`: Foundational spiders, item loaders, pagination, and data-cleaning pipelines.
- `project_1_champions_league/`: HTML table extraction for standings and team statistics.
- `project_2_amazon_rank/`: Product title, price, and Best Sellers Rank extraction with configurable request headers.

## Setup

From the repository root, activate the virtual environment and install dependencies:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run Projects

Each Scrapy command runs from that project's directory. Supply a target URL with `-a url=...`.

```powershell
# ESPN-style standings table
cd project_1_champions_league
scrapy crawl table -a url="https://example.com/standings" -O standings.json

# Amazon product page
cd ..\project_2_amazon_rank
scrapy crawl tracker -a url="https://www.amazon.com/dp/PRODUCT_ID" -O product.json


The target sites may use JavaScript rendering or restrict automated access. Check each site's terms and `robots.txt`, and keep requests rate-limited. Scrapy's robots setting remains enabled in both new projects.
