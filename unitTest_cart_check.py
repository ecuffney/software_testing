import unittest
import time
from selenium import webdriver

URL= 'http://automationpractice.com/index.php?id_product=1&controller=product#/size-s/color-orange'
PLUS_BUTTON= 'input[id= "quantity_wanted"]'
DROPDOWN= 'select#group_1'
SIZE_M= 'option[value="2"]'
COLOR= "Blue"
CART_BTTN= 'button[name= "Submit"]'
PROCEED_BTTN= 'a[title= "Proceed to checkout"]'
CART_CONTAINS= 'span[id= "summary_products_quantity"]'
LINK_TEXT= 'Color : Blue,'


class CartCheck(unittest.TestCase):

#sets up WebDriver
    def setUp(self):
        self.driver = webdriver.Firefox()

#navigates to url
    def test_cartQuant(self):
        driver = self.driver
        driver.get(URL)

#increases item quantity to 3
        select_quant = driver.find_element_by_css_selector(PLUS_BUTTON)
        select_quant.click()
        select_quant.clear()
        select_quant.send_keys(3)
        time.sleep(1)

#selects size M from dropdown menu
        size =  driver.find_element_by_css_selector(DROPDOWN)
        size.click()
        select_med = driver.find_element_by_css_selector(SIZE_M)
        select_med.click()
        time.sleep(1)

#changes color to blue
        color_square = driver.find_element_by_name(COLOR)
        color_square.click()
        time.sleep(1)

#clicks add to cart button
        cart_button = driver.find_element_by_css_selector(CART_BTTN)
        driver.execute_script("arguments[0].scrollIntoView();", cart_button)
        cart_button.click()
        time.sleep(1)

#clicks proceed button
        checkout_proceed = driver.find_element_by_css_selector(PROCEED_BTTN)
        checkout_proceed.click()
        time.sleep(1)

#confirms cart quantity matches expected # of items
        check_cart_quant = driver.find_element_by_css_selector(CART_CONTAINS)
        cart_quant_text = check_cart_quant.text
        expect_text= "3 Products"
        assert expect_text in cart_quant_text

#confirms item color and size match product description
        prod_desc = driver.find_element_by_partial_link_text(LINK_TEXT)
        prod_desc_text = prod_desc.text
        expected_text = "Color : Blue, Size : M"
        assert expected_text in prod_desc_text

#closes browser instance
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
