import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

def format_date(date_text):
    """Converts 'Month DD, YYYY' to 'YYYY-MM-DD'"""
    date_text = date_text.strip()
    if not date_text or "End of Life" in date_text:
        return "N/A"
    
   
    try:
       
        obj = datetime.strptime(date_text, "%B %d, %Y")
        return obj.strftime("%Y-%m-%d")
    except:
        return date_text

def scrape_software():
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-life-summary"
    
    driver.get(url)
    driver.implicitly_wait(10)

    rows = driver.find_elements(By.XPATH, "//table//tr")
    
    data = []
    current_name = ""

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        
       
        if len(cells) == 1:
            current_name = cells[0].text.strip()
            continue
            
       
        if len(cells) == 3:
            version = cells[0].text.strip()
            
            if version.lower() == "version":
                continue
                
            
            info = {
                "Software Name": current_name,
                "Version": version,
                "Release Date": format_date(cells[1].text),
                "EOL Date": format_date(cells[2].text)
            }
            data.append(info)

    pd.DataFrame(data).to_csv("software_eol.csv", index=False)
    print("Done! Scraped", len(data), "items.")
    driver.quit()

if __name__ == "__main__":
    scrape_software()