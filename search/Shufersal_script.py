from selenium import webdriver
from selenium.webdriver.common.by import By


def shufersal(itemname):
    driver = webdriver.Chrome()
    driver.get(f'https://www.shufersal.co.il/online/he/search?text={itemname}')
    items = driver.find_elements(By.XPATH, '//ul[@class="tileContainer newDesignProductTabsMobile"]')
    print(type(items))
    print(len(items))
    for item in items:
        print(item.text)

itemname = input('Please enter item name:')
pro = shufersal(itemname)

print(f'Items from שופרסל \n {pro}')