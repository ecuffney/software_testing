from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

SORT = 'selectProductSort'
DROPDOWN = 'selectProductSort'
IN_STOCK = 'In stock'
PRODUCT = 'product-container'
ADD_ALL = '//*[@id="center_column"]/ul/li[%s]/div/div[2]/div[2]/a[1]/span'
KEEP_SHOPPING = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span'
FIND_CART = '/html/body/div/div[1]/header/div[3]/div/div/div[3]/div/a'
CLICK_CART = '//*[@id="button_order_cart"]/span'
PROD_QUANT = 'summary_products_quantity'


driver = webdriver.Firefox()
driver.get("http://automationpractice.com/index.php?id_category=8&controller=category")

#selects in stock items from dropdown menu
def select_in_stock():
    sort_menu = driver.find_element_by_id(SORT)
    sort_menu.click()
    select = Select(driver.find_element_by_id(DROPDOWN))
    select.select_by_visible_text(IN_STOCK)
    time.sleep(1)

#adds every in stock item to shopping cart
def add_to_cart():
    product_containers = driver.find_elements_by_class_name(PRODUCT)
    for index,product_container in enumerate(product_containers):
        driver.execute_script("arguments[0].scrollIntoView();", product_container)
        hover = ActionChains(driver).move_to_element(product_container)
        hover.perform()
        time.sleep(0.5)
        add_button =driver.find_element_by_xpath(ADD_ALL%(index+1))
        add_button.click()
        time.sleep(1)
        cont_shopping= driver.find_element_by_xpath(KEEP_SHOPPING)
        cont_shopping.click()
        time.sleep(1)

#navigates to shopping cart page
def review_cart():
    cart_button= driver.find_element_by_xpath(FIND_CART)
    driver.execute_script("arguments[0].scrollIntoView();", cart_button)
    hover = ActionChains(driver).move_to_element(cart_button)
    hover.perform()
    click_to_cart= driver.find_element_by_xpath(CLICK_CART)
    click_to_cart.click()
    time.sleep(1)

#asserts total number of items added to cart meets expected quantity
def confirm_item_quant():
    cart_quant = driver.find_element_by_id(PROD_QUANT)
    cart_quant_text = cart_quant.text
    if cart_quant_text == "5 Products":
        print("Test SUCCESS: all items added to cart")
    else:
        print("Test FAIL: # of products does not match")


select_in_stock()
add_to_cart()
review_cart()
confirm_item_quant()

driver.close()
