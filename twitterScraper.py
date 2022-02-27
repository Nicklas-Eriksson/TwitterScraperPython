import login, search, scrape, parse

'''
    Example:
        userSearch = Running is fun
        searchFrom = Latest / Top
        numberOfTweets = 100
'''
def Run(userSearch, searchFrom, numberOfTweets):
    numberOfTweets = parse.ToInt(numberOfTweets)
    driver = login.Procedure()

    if(userSearch.rstrip().__contains__(' ')):
        userSearch = "\"" + userSearch + "\""

    print('Attempting to enter search...')
    search.EnterSearchField(driver, userSearch)
    print('Search entered!')

    print('Attempting to filter search...')
    if(searchFrom == "Latest results"):
        search.SelectLatest(driver)
    elif(searchFrom == "Persons"):
        search.SelectPersons()
    else: #Defaults to Top results
        pass
    print('Search filtered!')


    data = scrape.Data(driver, numberOfTweets)
    driver.close()

    return data
