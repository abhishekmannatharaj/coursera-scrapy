# Ebook Scraper

A web scraping project built with **Scrapy** and managed via **uv** to extract book data from Coursera/target websites.

<img width="1914" height="917" alt="image" src="https://github.com/user-attachments/assets/1abb7904-9acc-4941-ad07-92216e98b9eb" />

<img width="1226" height="803" alt="image" src="https://github.com/user-attachments/assets/97ecb079-c522-4f56-9936-e708f0c62b60" />


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
