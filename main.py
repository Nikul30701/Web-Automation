from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# Define driver, options and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

download_path = os.getcwd() # for file download in root directory
prefs = {'download.default_directory': download_path}
chrome_options.add_experimental_option('prefs', prefs)

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options,service=service)

# Load the webpage
driver.get("https://demoqa.com/login")

# Locate username, password, and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'password')))
login_button = driver.find_element(By.ID, 'login')

# Fill in username and password
username_field.send_keys("Nikul6403")
password_field.send_keys("Nikul@30701")
driver.execute_script("arguments[0].click();", login_button) # this is JS code to avoid intercept error

# Locate the Elements dropdown and textbox
elements = (WebDriverWait(driver, 10).
            until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]'))))
elements.click()

text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'item-0')))
text_box.click()

# Elements the form fields abuttonnd submit
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')


# Fill in forms fields
fullname_field.send_keys("John Smith")
email_field.send_keys("johnsmith@gmail.com")
current_address_field.send_keys("John Street 100, NewYork, USA")
permanent_address_field.send_keys("John Street 100, NewYork, USA")
driver.execute_script("arguments[0].click();", submit_button) # this is JS code to avoid intercept error

# Locate the Upload and Download section and the Download button
upload_download = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7'))))
driver.execute_script("arguments[0].click();", upload_download) # this is JS code to avoid intercept error

download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button) # this is JS code to avoid intercept error


input("Press Enter to close the browser")
driver.quit()

