import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def scrape_palo_alto():
    driver = get_driver()
    url = "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware-end-of-life-dates"
    
    try:
        driver.get(url)
        driver.implicitly_wait(10)

    
        rows = driver.find_elements(By.XPATH, "//table[contains(@class, 'table')]//tr")
        results = []

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            
            
            if len(cells) < 4:
                continue

            
            name = cells[0].text.strip()
            eol = cells[2].text.strip()
            replacement = cells[3].text.strip()
            
            try:
                link = cells[0].find_element(By.TAG_NAME, "a").get_attribute("href")
            except:
                link = "N/A"

            results.append({
                "Vendor": "Palo Alto",
                "ProductName": name,
                "EOL Date": eol,
                "Resource": link,
                "Recommended Replacement": replacement
            })

        df = pd.DataFrame(results)
        df.to_csv("palo_alto_eol.csv", index=False)
        print(f"Success: {len(results)} products extracted to palo_alto_eol.csv")

    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_palo_alto()