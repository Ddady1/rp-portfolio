from selenium import webdriver
from selenium.webdriver.common.by import By


def shufersal(itemname):
    driver = webdriver.Chrome()
    driver.get(f'https://www.shufersal.co.il/online/he/search?text={itemname}')
    items = driver.find_elements(By.XPATH, '//div[@class="textContainer"]')
    images = driver.find_elements(By.XPATH, '//div/a/img[@class="pic"]')
    print(type(items))
    print(len(items))
    item_images = []
    for image in images:
        item_images.append(image.get_attribute('src'))
    print(len(item_images))
    item_images.pop(len(item_images) -1)
    item_images.pop(0)
    print(item_images)
    '''if len(item_images) != len(items):
        item_images.pop(0)
        clean_item_images = []
        for x in range(len(items)):
            clean_item_images.append(item_images[x])'''

    #print(clean_item_images)
    for x in range(2, len(items)):
        print(items[x].text)

itemname = input('Please enter item name:')
pro = shufersal(itemname)

print(f'Items from שופרסל \n {pro}')