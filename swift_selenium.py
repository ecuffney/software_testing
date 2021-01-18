from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://builtbyswift.com/")

closePop=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="mc-closeModal"]')))
closePop.click()    #waits for pop up to appear, clicks x button(located by xpath above)
time.sleep(3)

SaleLink= (driver.find_element_by_link_text('Sale')) #clicks on Sale button in menu
SaleLink.click()
time.sleep(3)

clickJrPack =WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//img[@alt="Jr. Ranger Pannier Set heather-xpac"]')))
clickJrPack.click()  #clicks on Jr ranger pack when it fully appears
time.sleep(2)

scroll= driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scrolls to bottom of page
time.sleep(4)

enterEmail = driver.find_element_by_id('mce-EMAIL');
enterEmail.send_keys("ekcuffney@gmail.com"); #enters email
time.sleep(2)
enterEmail.send_keys(Keys.RETURN); #hits return key


driver.close()
