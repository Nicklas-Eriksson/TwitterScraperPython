from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Executing the search recived from the front end.
def EnterSearchField(driver, search):
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/label[1]/div[2]/div[1]/input[1]"))).send_keys(search, Keys.ENTER)
    except:
        return None

def SelectLatest(driver):
    try:
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Senaste')]"))).click()
    except:
        return None

def SelectPerson(driver):
    try:
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Personer')]"))).send_keys.click()       
    except:
        return None