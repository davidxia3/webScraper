from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json

options = Options()
options.headless = True

jsonOutput={
    "2010": {},
    "2011": {},
    "2012": {},
    "2013": {},
    "2014": {},
    "2015": {}
}

URL0 = "https://www.scrapethissite.com/pages/ajax-javascript/#2010"
URL1 = "https://www.scrapethissite.com/pages/ajax-javascript/#2011"
URL2 = "https://www.scrapethissite.com/pages/ajax-javascript/#2012"
URL3 = "https://www.scrapethissite.com/pages/ajax-javascript/#2013"
URL4 = "https://www.scrapethissite.com/pages/ajax-javascript/#2014"
URL5 = "https://www.scrapethissite.com/pages/ajax-javascript/#2015"

URLs =[("2010", URL0), ("2011", URL1), ("2012", URL2), ("2013", URL3), ("2014", URL4), ("2015", URL5)]



for URL in URLs:
    driver = webdriver.Chrome(options = options)
    driver.get(URL[1]) 
    time.sleep(5)


    filmTitles = driver.find_elements(By.CLASS_NAME, "film-title")
    filmNominations = driver.find_elements(By.CLASS_NAME, "film-nominations")
    filmAwards = driver.find_elements(By.CLASS_NAME, "film-awards")

    for i in range(len(filmTitles)):
        movie = {}
        nominations = int(filmNominations[i].text)
        awards = int(filmAwards[i].text)
        if (nominations < 3):
            movie["nominations"] = nominations
            movie["awards"] = awards
            jsonOutput[URL[0]][filmTitles[i].text] = movie


print(json.dumps(jsonOutput, indent = 4, ensure_ascii = False))

with open("output1.json", "w", encoding = "utf-8") as f:
    json.dump(jsonOutput, f, ensure_ascii = False, indent = 4)