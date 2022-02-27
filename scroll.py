import time

#Allows bot to scroll down on the twitter page.
def Down(driver):
    tries = 0
    previousHeight = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        print('Scrolling...')
        newHeight = driver.execute_script("return document.body.scrollHeight")
        
        if newHeight == previousHeight: #End of scrolling reached.
            if tries >= 3:
                print('3 scroll attempts reached...')
                return False #no more tweets to scrape
            else:
                tries += 1
                time.sleep(2)
         
        else: #Continue scrolling
            previousHeight = newHeight
            break;