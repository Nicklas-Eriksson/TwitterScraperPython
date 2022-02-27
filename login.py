from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()
EmailAdress = os.getenv("EmailAdress")
TwitterPassword = os.getenv("TwitterPassword")
PhoneNumber = os.getenv("PhoneNumber")

def Procedure():
    options = EdgeOptions()
    options.use_chromium = True

    driver = InitialSetup(options)

    #Will allways ask for username first.
    if(EnterEmail(driver) == True):
        Click(driver)

        if(EnterPass(driver) == True):
            PressLogIn(driver)
            EnterPhoneNumber(driver)
            Click(driver)
        else:
            EnterPhoneNumber(driver)
            Click(driver)
            EnterPass(driver)
            PressLogIn(driver)

        try:
            PotentialAuth(driver)
            Click(driver)
        except:
            print("Auth failed")
            return driver

        return driver
    else:
        print('Login failed @ Enter email')    

def InitialSetup(options):
    baseUrl = "https://twitter.com/home?lang=sv"
    driver = Edge(options=options)
    driver.get(baseUrl)
    driver.maximize_window()
    return driver
    
def EnterEmail(driver):
    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='username']"))).send_keys(EmailAdress)
        return True
    except:
        return False

def EnterPhoneNumber(driver):
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/label[1]/div[1]/div[2]/div[1]/input[1]"))).send_keys(PhoneNumber)
        return True
    except:
        return False

def EnterPass(driver):
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/label[1]/div[1]/div[2]/div[1]/input[1]"))).send_keys(TwitterPassword)
        return True
    except:
        return False    

def Click(driver):
    try:
        driver.find_element_by_xpath("//span[contains(text(),'Nästa')]").click()
        return True
    except:
        return False   

def PressLogIn(driver):
    try:
        driver.find_element_by_xpath("//span[contains(text(),'Logga in')]").click()
        return True
    except:
        return False      
    
def PotentialAuth(driver):
    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='tel']"))).send_keys(PhoneNumber)
        return True
    except:
        return False 