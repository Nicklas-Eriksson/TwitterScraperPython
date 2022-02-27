import time
from selenium.webdriver.support import expected_conditions as EC
import scroll

uniqueIdenteties = []

#Scrapes the twitter posts from the page by finding the HTML element containing the tweets.
def Data(driver, numberOfTweetsRequested):
    time.sleep(2)

    #subtracts duplicates from list
    tweetDataSet = []
    index = 1

    print('Tweets collected:')
    KeepGoing = True

    while True:
        #scrapes twitter page on all elements containing data-testid="tweet"
        if index <= numberOfTweetsRequested:
            tweets = driver.find_elements_by_css_selector("[data-testid=\"tweet\"]")
            tweets = list(dict.fromkeys(tweets))

            for tweet in tweets:
                if index <= numberOfTweetsRequested:
                    t = formateTweet(tweet)

                    if t[0] not in uniqueIdenteties:
                        tweetDataSet.append(t)
                        uniqueIdenteties.append(t[0])
                        print(index)
                        index += 1
                    else:
                        print('Whops! Post is in unique identeties.')                        
                else:
                    print('Number of requested tweets is reached! (Inner loop)')
                    break             
        else:    
            print('Number of requested tweets is reached! (Outer loop)')
            break  
        
        if KeepGoing == True and numberOfTweetsRequested >= index:
            print("Request not reached.")
            keepGoing = scroll.Down(driver) #returns True if scroll was successful. False if there are no more tweets on the subject.
            
            if keepGoing is False:
                print('Bottom of the page is reached!')
                break
        else:
            break

    uniqueIdenteties.clear()

    return tweetDataSet

#Formats the tweet into a tuple containing username, handle, post and so on.
def formateTweet(tweet):
    attempts = 0
    success = True

    try:
        while attempts < 2 or success == True:
            try:
                username = tweet.find_element_by_xpath('.//span').text
                break
            except:
                attempts += 1
    except:
        username = "None"
    try:
        handle = tweet.find_element_by_xpath('.//span[contains(text(), "@")]').text
    except:
        handle = "None"
    try:
        attempts = 0

        while attempts < 2 or success == True:
            try:
                tryDate = tweet.find_element_by_xpath('.//time')
                date = tryDate.get_attribute('datetime')
                break
            except:
                attempts += 1
                date = None
    except:
        date = None
    try:
        attempts = 0

        while attempts < 2 or success == True:
            try:
                post = tweet.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
                break
            except:
                attempts += 1
                post = "None"

    except:
        post = "None"
    try:
        commentCount = tweet.find_element_by_xpath('.//div[@data-testid="reply"]').text
    except:
        commentCount = "None"
    try:
        retweetCount = tweet.find_element_by_xpath('.//div[@data-testid="retweet"]').text
    except:
        retweetCount = "None"
    try:
        likes = tweet.find_element_by_xpath('.//div[@data-testid="like"]').text
    except:
        likes = "None"

    #if date == None the post is a commercial
    if(date == None):
        return None
    else:
        tweetId = username+date
        return (tweetId, username, handle, date, post, commentCount, retweetCount, likes)