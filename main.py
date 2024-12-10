import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class WebAutomation:
    def __init__(self):
        # Define driver, options and service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        download_path = os.getcwd()  # for file download in root directory
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        # Load the webpage
        self.driver.get("https://demoqa.com/login")

        # Locate username, password, and login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Fill in username and password
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)  # this is JS code to avoid intercept error

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Locate the Elements dropdown and textbox
        elements = (WebDriverWait(self.driver, 10).
                    until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]'))))
        elements.click()

        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Elements the form fields abuttonnd submit
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in forms fields
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)

        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)  # this is JS code to avoid intercept error

    def download(self):
        # Locate the Upload and Download section and the Download button
        upload_download = (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7'))))
        self.driver.execute_script("arguments[0].click();", upload_download)  # this is JS code to avoid intercept error

        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)  # this is JS code to avoid intercept error

        # Wait for the file download
        time.sleep(5)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login("Nikul6403", "Nikul@30701")
    webautomation.fill_form("John Smith", "johnsmith@gmail.com", "Street 1", "Street 2")
    webautomation.download()
    webautomation.close()









