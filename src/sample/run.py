import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

SLEEP = 3
CSV_NAME = "trend.csv"

if __name__=="__main__":
    driver_path = ChromeDriverManager().install()
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome(service=Service(executable_path=driver_path), options=options) as driver:
        url = "https://github.com/trending"
        driver.get(url)
        time.sleep(SLEEP)
        results = list()
        items = driver.find_elements(By.CSS_SELECTOR, "article.Box-row")
        for i in items[:10]:
            item = dict()
            item["title"]= i.find_element(By.TAG_NAME, "h2").text
            item["url"] = i.find_element(By.CSS_SELECTOR, "a.Link").get_attribute("href")
            results.append(item)
        df = pd.DataFrame(results)
        df.to_csv(CSV_NAME)
        items[0].find_element(By.CSS_SELECTOR, "a.Link").click()
        time.sleep(SLEEP)
