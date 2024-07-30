from selenium import webdriver
from selenium.webdriver.common.by import By


def tzomet(bookname):
    driver = webdriver.Chrome()
    # צומת ספרים
    driver.get(f'https://www.booknet.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')
    prices = driver.find_elements(By.TAG_NAME, 'ins')
    books = driver.find_elements(By.XPATH, '//div[@class="products product-cube col-md-2"]')
    authors = driver.find_elements(By.XPATH, '//a[@class="book-below-title product-author"]')
    images = driver.find_elements(By.XPATH, '//img[@class="img-responsive img-lazy-load"]')
    # azal = driver.find
    in_stock = None
    is_printed = 'מודפס'
    is_digital = False
    in_basket = 'הוסף לסל'
    price_str = 'מחיר מכירה'
    price_before = 'מחיר קודם'
    books_image = []
    for image in images:
        books_image.append(image.get_attribute("src"))

    books_dict = {}
    looper = 0
    exc = driver.find_elements(By.XPATH, '//button/span[@class="sr-only"]')
    # print(exc[0].text)
    for book in books:
        raw_details = book.text
        book_id = book.get_attribute("data-prodid")
        book_details = raw_details.split('\n')
        print(book_details)
        if exc[looper].text in book_details:
            book_details.remove(exc[looper].text)
        #if price_str in book_details:
        #    book_details.remove(price_str)
        print(book_details)
        #if price_before in book_details:
        #    book_details.remove(price_before)
        print(book_details)
        if len(book_details) >= 5:
            book_details.pop(0)
        book_details.append(books_image[looper])
        #print(book_details)
        if in_basket in book_details:
            in_stock = 'במלאי'
        else:
            in_stock = 'אזל'
        book_details.pop(3)
        book_details.insert(3, in_stock)
        book_details.append(is_printed)

        ########## For checking purposes ##########
        '''i = 0
        for item in book_details:
            print(f'{i} - {item}')
            i += 1
        if looper < len(exc) - 1:
            looper += 1
            # print(looper)'''
        ###########################################
        books_dict[book_id] = book_details

    #print(books_dict)
    return books_dict


#driver = webdriver.Chrome()
#driver.get('https://www.booknet.co.il/')
#bookname = input('Please enter books name:')



#print('Books frm צומת ספרים \n', tzomet(bookname))
