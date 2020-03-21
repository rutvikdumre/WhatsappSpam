from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
target = []
n=int(input("Enter no of contacts:"))
for i in range(n):
    x=input("Enter WhatsApp contact name:")
    x='"'+x+'"'
    target+=[x]
string = input('Enter message:')
t=int(input('Enter no of times you want to spam this message:'))
driver = webdriver.Chrome('/chromedriver') 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
  

print(target)
    


for j in target:  
    x_arg = '//span[contains(@title,'+ j +')]'
    group_title = wait.until(EC.presence_of_element_located(( 
        By.XPATH, x_arg))) 
    group_title.click() 
    inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
    input_box = wait.until(EC.presence_of_element_located(( 
        By.XPATH, inp_xpath))) 
    for i in range(t): 
        input_box.send_keys(string + Keys.ENTER) 
        time.sleep(1) 
