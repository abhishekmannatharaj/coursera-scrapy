# About This Project

This project is a Scrapy-based web scraping application built to extract book information from the Books to Scrape website.

## Project Purpose

The scraper targets the Travel category and collects key details such as:

- Book title
- Price
- Availability

The goal is to demonstrate how to:

- crawl a website using Scrapy
- parse HTML content with CSS selectors
- clean and structure scraped data
- save items into a Python item model
- send the extracted data to an Excel file
- optionally insert the records into MongoDB Atlas

## Main Workflow

1. The spider starts from the Travel category page.
2. It requests multiple pages in the category.
3. Each product card is parsed for the required fields.
4. The scraped data is transformed into a structured item.
5. The item pipeline stores the data in Excel and optionally MongoDB.

## Key Files

- `ebook_scraper/ebook_scraper/spiders/ebook_scraper.py` : Scrapy spider that defines the crawl logic
- `ebook_scraper/ebook_scraper/items.py` : Data model for each book item
- `ebook_scraper/ebook_scraper/pipelines.py` : Saves scraped data to Excel and MongoDB
- `ebook_scraper/ebook_scraper/settings.py` : Scrapy project settings
- `.env` : Local environment variables such as MongoDB connection string

## Technologies Used

- Python
- Scrapy
- CSS selectors
- MongoDB Atlas
- OpenPyXL
- Python-dotenv

## Example Use Case

This project is useful for learning web scraping, data extraction, and data storage pipelines. It is a practical example of collecting structured data from a website and saving it for analysis or use in a database.
