import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidSelectorException
import numpy as np


driver = webdriver.Chrome("C:/Users/piyus/Downloads/chromedriver_win32 (1)/chromedriver.exe")

time.sleep(3)
 
driver.maximize_window()

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3505702305&f_AL=true&f_E=2&geoId=102713980&keywords=data%20scientist&location=India')
 

soup = BeautifulSoup(driver.page_source,'lxml')


sign_in_button = driver.find_element(By.XPATH,'''/html/body/div[1]/header/nav/div/a[2]''')

sign_in_button.click()

time.sleep(2)

username = 'piyushrane3105@gmail.com'
pas = 'Piyushrane@999'

# Login page
mail = driver.find_element(By.XPATH , '//*[@id="username"]')
mail.send_keys(username)
sec = driver.find_element(By.XPATH, '//*[@id="password"]')
sec.send_keys(pas)
sec.send_keys(Keys.ENTER)

time.sleep(7)
# Searh button for job title
search_button = driver.find_element(By.CLASS_NAME,  'jobs-search-box__text-input.jobs-search-box__keyboard-text-input')

if search_button.get_attribute("value"):
    search_button.clear()
    
search_button.send_keys('data scientist')
search_button.send_keys(Keys.ENTER)


time.sleep(4)



# Easy Apply button
j = 0
while True:
    
    try:
        
        time.sleep(2)
        
       
        listings =  driver.find_elements(By.CLASS_NAME, 'disabled.ember-view.job-card-container__link.job-card-list__title')
        
    
        for i in listings:
             i.click()
             time.sleep(3)
             path = True
     
             
             try:
                     driver.find_element(By.CLASS_NAME, 'jobs-apply-button--top-card').click()
                     time.sleep(0.5)
                     path = True
                     while path:
                         try:
                             driver.find_element(By.CLASS_NAME, 'artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view').click()
                             try:
                                  driver.find_element(By.CLASS_NAME, 'artdeco-inline-feedback.artdeco-inline-feedback--error.ember-view.mt1')
                                  driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--2.artdeco-button--tertiary.ember-view').click()    
                                  driver.find_element(By.CLASS_NAME, 'artdeco-modal__confirm-dialog-btn.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view').click()
                             except NoSuchElementException:
                                 pass
                                 
                                
                             time.sleep(1)
                         except NoSuchElementException:
                             path = False   
                             pass
                         except ElementNotInteractableException:
                             
                             time.sleep(2)
                             driver.find_element(By.CLASS_NAME, 'artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.mlA.block').click()
                   
             except StaleElementReferenceException:
                     pass
             except NoSuchElementException:
                    pass

        
        url = f'https://www.linkedin.com/jobs/search/?currentJobId=3505702305&f_AL=true&f_E=2&geoId=102713980&keywords=data%20scientist&location=India&start={j+25}'               
        j+=25
        
        driver.get(url)
        
        time.sleep(2)
        
            
        stop = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div[1]/div/h1')
        soup = BeautifulSoup(driver.page_source,'lxml')
        time.sleep(3)
        break
    
    except NoSuchElementException:
        pass
    except StaleElementReferenceException:
        pass
    

 




