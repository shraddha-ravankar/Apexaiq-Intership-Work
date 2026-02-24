"""
Palo Alto Networks Software End-of-Life (EOL) Scraper.

 Selenium with Chrome WebDriver to scrape
software EOL information from the Palo Alto Networks website
and saves the extracted data into a CSV file.

"""

import time
import pandas as pd
from dataclasses import dataclass, asdict
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    from webdriver_manager.chrome import ChromeDriverManager
    CHROMEDRIVER = ChromeDriverManager().install()
except Exception:
    CHROMEDRIVER = None


URL = "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-life-summary"


@dataclass
class SoftwareRow:
    """
    Data structure representing a single software EOL record.
    """
    softwareName: str
    version: str
    releaseDate: str
    eolDate: str


def normalize_date(date_str: str) -> str:
    """
    Convert date strings from the website into yyyy-mm-dd format.

    Supported formats:
    - January 31, 2026
    - Jan 31, 2026

    Returns an empty string if conversion fails.
    """
    if not date_str:
        return ""

    for fmt in ("%B %d, %Y", "%b %d, %Y"):
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue

    return ""


class PaloAltoSoftwareScraper:
    """
    Scraper class responsible for loading the Palo Alto Software
    EOL page, extracting table data, and storing it in memory.
    """

    def __init__(self, headless: bool = True, timeout: int = 20):
        """
        Initialize Chrome WebDriver and wait configuration.
        """
        chrome_opts = Options()
        if headless:
            chrome_opts.add_argument("--headless=new")

        chrome_opts.add_argument("--disable-gpu")
        chrome_opts.add_argument("--no-sandbox")
        chrome_opts.add_argument("--disable-dev-shm-usage")
        chrome_opts.add_argument("--window-size=1400,900")
        chrome_opts.add_argument("--log-level=3")

        if CHROMEDRIVER:
            self.driver = webdriver.Chrome(
                service=Service(CHROMEDRIVER),
                options=chrome_opts
            )
        else:
            self.driver = webdriver.Chrome(options=chrome_opts)

        self.wait = WebDriverWait(self.driver, timeout)
        self.rows: list[SoftwareRow] = []

    def open_page(self):
        """
        Open the Palo Alto Software EOL page and wait
        until all tables are loaded.
        """
        self.driver.get(URL)
        self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.oneColumnPlain table")
            )
        )
        time.sleep(1.5)

    def parse_tables(self):
        """
        Extract software names, versions, release dates,
        and EOL dates from all tables on the page.
        """
        tables = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div.oneColumnPlain table"
        )

        for table in tables:
            software_name = "Unknown Software"

            for locator in [
                (By.CSS_SELECTOR, "th[colspan] p b"),
                (By.CSS_SELECTOR, "td[colspan] p b"),
                (By.XPATH, "./preceding::p[1]/b"),
                (By.XPATH, "./preceding::h2[1] | ./preceding::h3[1]")
            ]:
                try:
                    software_name = table.find_element(*locator).text.strip()
                    break
                except Exception:
                    continue

            rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

            for row in rows:
                cols = [
                    td.text.strip()
                    for td in row.find_elements(By.TAG_NAME, "td")
                ]

                if len(cols) >= 3 and cols[0] != "Version":
                    self.rows.append(
                        SoftwareRow(
                            softwareName=software_name,
                            version=cols[0],
                            releaseDate=normalize_date(cols[1]),
                            eolDate=normalize_date(cols[2])
                        )
                    )

        print(f"Parsed {len(self.rows)} rows from {len(tables)} tables.")

    def save_csv(self, path: str = "paloalto_software_eol.csv"):
        """
        Save extracted software EOL data into a CSV file.
        """
        df = pd.DataFrame([asdict(row) for row in self.rows])
        df.to_csv(path, index=False, encoding="utf-8")
        print(df.head())
        print(f"Saved {len(df)} rows to {path}")


def main():
    """
    Main execution function.
    """
    scraper = PaloAltoSoftwareScraper(headless=True)
    scraper.open_page()
    scraper.parse_tables()
    scraper.save_csv()
    scraper.driver.quit()


if __name__ == "__main__":
    main()
