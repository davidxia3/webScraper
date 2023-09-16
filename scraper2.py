from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json

options = Options()
options.headless = True

jsonOutput = {}

URL = "https://www.scrapethissite.com/pages/frames/"
driver = webdriver.Chrome(options = options)
driver.get(URL)


frame_ref = driver.find_elements(By.TAG_NAME, "iframe")[0]
iframe = driver.switch_to.frame(frame_ref)


turtleFamilyCardsList = driver.find_elements(By.CLASS_NAME, "turtle-family-card")

turtleTagsList = []
turtleFamilyNamesList = []
for i in range(len(turtleFamilyCardsList)):
    turtleTagsList.append(turtleFamilyCardsList[i].find_element(By.TAG_NAME, "a"))
    turtleFamilyNamesList.append(turtleFamilyCardsList[i].find_element(By.CLASS_NAME, "family-name").text)

turtleHREFs = []
for i in range(len(turtleTagsList)):
    turtleHREFs.append(turtleTagsList[i].get_attribute("href"))

for i in range(len(turtleHREFs)):
    driver.get(turtleHREFs[i])
    turtleDescription = driver.find_element(By.CLASS_NAME, "lead").text
    turtleYear = ""
    turtleName = turtleFamilyNamesList[i]
    for j in range(len(turtleDescription)):
        if turtleDescription[j].isdigit():
            turtleYear += turtleDescription[j]
    if int(turtleYear) < 1840:
        turtle = {}
        turtle["Discovery Year"] = turtleYear
        turtle["Description"] = turtleDescription.replace("\"", "")
        jsonOutput[turtleName] = turtle



print(json.dumps(jsonOutput, indent = 4, ensure_ascii = False))

with open("output2.json", "w", encoding = "utf-8") as f:
    json.dump(jsonOutput, f, ensure_ascii = False, indent = 4)

