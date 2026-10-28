from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import sys

# 1. Grab arguments passed from n8n via the terminal command
# sys.argv[0] is the script name itself
# sys.argv[1] will be the URL
# sys.argv[2] will be the Company Name
if len(sys.argv) < 3:
    print("[Error] Missing arguments! Please provide URL and Company Name.")
    sys.exit(1)

target_url = sys.argv[1]
company_name = sys.argv[2]

print(f"[Log Info] - Attempting to scrape for: {company_name}")

try:
    driver = webdriver.Chrome()
    try:
        # 2. Use the dynamic URL passed from n8n
        driver.get(target_url)
        time.sleep(5)  # Good for a quick test; later we can upgrade to Explicit Waits!
        
        print(f"[Log Info] - Title = '{driver.title}'.")

    except WebDriverException as e:
        print(f"[Error] Failed to open the website.")
        print(f"Details: {e}")
        
finally:
    driver.quit()
    print("[Log Info] - Browser closed cleanly.")