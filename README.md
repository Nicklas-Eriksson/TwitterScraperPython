# Birdbot 2022
    A school project by Nicklas Eriksson


# Description:
Bird Bot is a program that can scrape Twitter based on user inputs given from the website,
and Tweet any given post as long as it fits Twitters post limit.

▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ 

# Third party programs:

Scraping: 
    Selenium
    Selenium is a webdriver that makes it possible for the program to locate a website's html
    attributes (i.e. Twitter.com).

    Selenium link: https://www.selenium.dev/

▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ 

# Python Lib:

Server:
    Socket and Pickle
    A socket server is initialized by the Twitter scraper and is up and running while the
    website is running. The website then establishes a client connection to the server to
    make requests and to receive requested data.
    ____________________________________________________________________
    Pickle is used for compressing, serializing and de-serializing the data object before
    sending the data to the server and/or client.

    Socket link: https://docs.python.org/3/library/socket.html
    Pickle link: https://docs.python.org/3/library/pickle.html


▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ 

# Functions: 

# Twitter login:
1. Login.InitialSetup:
    1. A webdriver is created using Selenium.
    The driver is given three commands, run on Windows Explored, the twitter-url and to
    maximize the browser window.
    The driver is returned and will from now on be used through the process.
2. Login.Procedure:
    1. EnterEmail: 
        1. With Selenium the input field for entering email address is found (done by finding
        input by XPath containing 'username').
        2. The email address is sent to the browser.
    2. Click:
        1. The "next" button is located using Selenium. 
        2. Once found, the button will be pressed.
    3. Enter password or phone number:
        1. The program will first try to enter a password, if that fails that means the
        browser requests the phone number first. (Depends if program logs in for the first
        time that day).
    4. EnterPass:
        1. With Selenium the input field for entering password is found (done by finding input
        by XPath containing 'password').
        2. The password is sent to the browser.
    4. EnterPhoneNumber:
        1. With Selenium the input field for entering phone number is found (done by finding
        input by XPath containing the correct div root.).
        2. The phone number is sent to the browser.
    5. Click:
        1. See previous 'Click:'.
    6. PotentialAuth:
        1. Twitter might ask for a phone number again for verification.
        Same procedure as previous (see EnterPhoneNUmber).
    7. Click:
        1. See previous 'Click':


# Scrape
1. Check search word / phrase:
    The search word / phrase is checked to see if it is a word or phrase. If a phrase is
    requested the " " symbols are added so Twitter can search for a sentence.
2. EnterSearchField:
    1. With Selenium the search bar is found (done by finding input by XPath containing the
    correct div root.).
    2. The search word / phrase is sent to the browser.
    3. The broswer is sent a key press (i.e. 'Enter') to make the search (using Selenium).
3. Search From:
    1. From the website the user decided where to scrape the data, 'Top', 'Latest' or 'Person'.
    Based on user input the scraper navigates to the correct type of search. The default is
    always 'Top results' (The program finds the correct button to press using Selenium by
    finding the XPath element containing 'Persons' or 'Latest').
4. Scrape Data:
    1. The program inspects the site and finds all the elements containing the CSS selector
    '[data-testid="tweet"]'.
    2. All the data is collected as a dictionary and converted into a list, the tweets are
    taken from the 'key' value of the dictionary.
     
    3. FormatTweet:
        Each tweet in the new list collection is formatted.
        1. The tweet is spliced into different variables, username, twitter-handle, creation
        date, post, comment count, retweet count and likes.
        2. The program will not always successfully parse the tweets into all variables
        since some tweets are commercial advertisements (containing no date, which gets
        discarded) and old tweets from when twitter used a different tweet format.
        3. A list of unique tweets-id's is stored and used to make sure the same tweet
        is not being saved again.
        4. As long as the requested amount of tweets has not yet been reached, the program
        will scroll down a whole page and capture a new batch of tweets.
5.  Scroll:
    1. The height of the screen is captured.
    2. The program scrolls down to the bottom of captured height.
    3. A new height is captured and the program continues to scroll, untill the function is
    no longer called.
    4. If the previous height and the new height correspond, this means that the bottom of
    the page is reached (no more tweets available). To ensure that the page is not just
    loading improperly the program is given three attempts to scroll the page.      
6. Close Driver:
    1. The driver is closed and the collected data is sent to the server function.

# Tweet it
1. Checks to see if the post is larger than 280-characters.
2. If a post is too large the post will be rewritten as an error message.
3. The program finds the input field given the XPath root.
4. The post is inserted into the input field.
5. The 'Tweet' button is found and pressed.

    * If the program fails to post a message will be returned as 'Flase'.
      If the program succeeds the message will be 'True'.
