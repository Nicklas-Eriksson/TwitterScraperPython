import keyword
from click import exceptions
import login
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

#This functions are called when the program is asked to tweet the results from the webpage.
def Run(res):
    driver = login.Procedure()

    if (len(res) > 280):
        res = 'Bird Bot has been requested to post.\nCharacters exceed Twitters 280-character limit. Please try again!'

    res = NavigateForTweet(driver, res)
    
    return res

def NavigateForTweet(driver, res):
    try:        
        try:
            import time
            time.sleep(2)
            
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div"))).send_keys(res)

            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span"))).click()

            driver.close()
        except:
            print("Failed to fill tweet post field.")
        

        return 'Tweet has been publiched!'
    except:
        return 'Tweet of results has failed...'