from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

category_list = "6"  # IT, programming
project_type = "OUTSOURCING" # 외주
page = 1 # page offset
per_page = 10 # page limit

url = f"https://kmong.com/enterprise/requests?q=&sort=CREATED_AT&category_list={category_list}&sub_category_list=&project_type={project_type}&page={page}&per_page={per_page}"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get(url)

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li")))
# item_list = driver.find_elements(By.CLASS_NAME, "css-22yx7y")
countitem_list = driver.find_elements(By.CLASS_NAME, "css-x6apz0.eausbnt0")

for i in range(per_page):
    # get list
    item_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li")))

    # print header of the item
    header = item_list[i].find_element(By.CLASS_NAME, "css-22yx7y").text
    summary = item_list[i].find_element(By.CLASS_NAME, "css-1bwz212").text
    work_days = item_list[i].find_elements(By.CLASS_NAME, "text-gray-900.typo-14")[1].text
    pay = item_list[i].find_element(By.CLASS_NAME, "css-u0z7b3.eausbnt6").text

    print(f"{i+1}. {header}\n진행기간 : {work_days}\n{pay}\n{summary}\n")

    # click item
    item_list[i].click()

    # wait for the detail page
    wait.until(EC.url_changes(driver.current_url))

    # detail page
    print(driver.current_url)
    details = driver.find_elements(By.CLASS_NAME, "css-1x0d611.eprdb4x7")
    for detail in details:
        t = detail.find_element(By.CLASS_NAME, "css-1flyc9m.eprdb4x8").text
        d = detail.find_element(By.CLASS_NAME, "css-1qdbyyx.eprdb4x9").text
        print(f"{t}\n{d}\n")

    print()

    # go back to list page
    driver.back()

    # wait for the list page
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li")))
