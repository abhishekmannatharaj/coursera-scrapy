from playwright.sync_api import sync_playwright

with sync_playwright() as p:
  # Open visible Chromium with a 1-second delay between actions
  browser = p.chromium.launch(headless=False, slow_mo=1000)
  page = browser.new_page()

  # 1. Visit the practice website
  page.goto("https://quotes.toscrape.com/")

  # 2. Click the Login link in the top-right corner
  page.get_by_text("Login").click()

  # 3. Print the new URL
  print("Landed on URL:", page.url)

  browser.close()