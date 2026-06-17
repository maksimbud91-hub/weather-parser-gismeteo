from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import os

driver = webdriver.Chrome()

driver.get("https://www.gismeteo.ru/")

search = driver.find_element(By.CSS_SELECTOR, "input[class='input js-input']")
search.click()
sleep(2)

place = str(input("какой город? "))
search.send_keys(place.strip())
sleep(2)

try:
    href = driver.find_element(By.CLASS_NAME, "city-link")
    href.click()
except:
    print("Город не найден")
    driver.quit()
    exit()

sleep(1)

temp = driver.find_element(By.CLASS_NAME, "weather-value")
temp1 = temp.find_element(By.TAG_NAME, "temperature-value")
sleep(1)

name = driver.find_element(By.CLASS_NAME, "page-title")
name1 = name.find_element(By.TAG_NAME, "h1")

city_name = name1.text.strip()
temperature = temp1.text.strip()

print(city_name, ":", temperature)

data = {
    "Город": city_name,
    "Температура": temperature
}

filename = "pogoda.xlsx"

if os.path.exists(filename):
    df_old = pd.read_excel(filename)
    df_new = pd.DataFrame([data])
    df = pd.concat([df_old, df_new], ignore_index=True)
else:
    df = pd.DataFrame([data])

df.to_excel(filename, index=False)
print(f"✅ Сохранено в {filename}")

sleep(2)
driver.quit()