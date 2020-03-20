from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  

driver = webdriver.Chrome('E:\Downloads\chromedriver_win32/chromedriver') 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
  

target = ['"Name of your friend"']
  

string = "Your Message"
for j in target:  
    x_arg = '//span[contains(@title,'+ j +')]'
    group_title = wait.until(EC.presence_of_element_located(( 
        By.XPATH, x_arg))) 
    group_title.click() 
    inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
    input_box = wait.until(EC.presence_of_element_located(( 
        By.XPATH, inp_xpath))) 
    for i in range(100): 
        input_box.send_keys(string + Keys.ENTER) 
        time.sleep(1) 
