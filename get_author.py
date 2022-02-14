#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

----------------------------------------------------------------------------
Created By  : Nathan Rohlfs
Created : February 2022
version ='1.0'
---------------------------------------------------------------------------

Script perfoms the following as part of a take home test for Alert Media:
1. Navigate to google.com
2. Type in stackoverflow
3. Click the link for the official stackoverflow site
4. Open the hamburger menu icon in the top left &amp; select Tags
5. Type &quot;python&quot; into the &#39;filter by tag name&#39; search bar
6. Select the link for python-3.6
7. Sort by most frequent
8. Click the question with the highest number of votes
9. Print the author of the answer with the highest number of votes
"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


class DomVariables:
    """A class used to store DOM variables and enable easier maintenance and reuse of elements.

    ...

    Attributes
    ----------
    google_search : str
        XPATH string for the google search input (google.com)
    google_submit : str
        ID string for the google search button(google.com)
    stack_link: str
        XPATH string for first google search result containing stack overflow url(google.com)
    stack_burger : str
        CSS selector string for hamburger menu on stack overflow main page(stackoverlow.com)
    tag : str
        XPATh string for Tag options within stackoverflow hamburger menu(stackoverlow.com)
    python_3_6 : str
        XPATh string for python-3.6 filter result(stackoverlow.com)
    more : str
        XPATH string for more filter options button(stackoverlow.com)
    frequent : str
        XPATH string for frequent filter option(stackoverlow.com)
    first_post : str
        XPATH string for link to top post(stackoverlow.com)
    author_answer_most_votes : str
        XPATH string for author of most voted answer within post (stackoverlow.com)

    Methods
    --------
    None

    """

    def __init__(self):
        self.google_search = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
        self.google_submit = 'btnK'
        self.stack_link = "//cite[contains(text(), 'https://stackoverflow.com')]"
        self.stack_burger = '.left-sidebar-toggle'
        self.tag = "//div[contains(text(), 'Tags')]"
        self.python_3_6 = "//a[contains(text(), 'python-3.6')]"
        self.more = "//button[contains(text(), 'More')]"
        self.frequent = "//a[contains(text(), 'Frequent')]"
        self.first_post = "//div[contains(@id, 'questions')]/div[1]/descendant::a[contains(@class,'s-link')]"
        self.author_answer_most_votes = "//div[contains(@id,'answers')]/div[2]/descendant::div[contains(@class,'post-signature flex--item fl0')][last()]/descendant::div[contains(@class,'user-details')]/a"




def get_author():
    #initialize dom variables
    vars = DomVariables()
    #set driver options and initialize driver
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    #uncommenting the headless option below may enable better performance.  Not recommended during testing/debugging of this script.
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    #implicit wait works well for current use
    driver.implicitly_wait(2)
    driver.get('https://google.com')
    #navigate to answer
    driver.find_element(By.XPATH,vars.google_search).send_keys('stackoverflow')
    driver.find_element(By.NAME,vars.google_submit).click()
    driver.find_elements(By.XPATH,vars.stack_link)[0].click()
    driver.find_element(By.CSS_SELECTOR,vars.stack_burger).click()
    driver.find_element(By.XPATH,vars.tag).click()
    #input field is default highlighted
    actions = ActionChains(driver)
    actions.send_keys('python')
    actions.send_keys(Keys.ENTER)
    actions.perform()
    driver.find_element(By.XPATH,vars.python_3_6).click()
    driver.find_element(By.XPATH,vars.more).click()
    driver.find_element(By.XPATH,vars.frequent).click()
    driver.find_element(By.XPATH,vars.first_post).click()
    author = driver.find_element(By.XPATH,vars.author_answer_most_votes).text
    driver.close()
    return(author)


def main():
    print('Fetching Author of most frequent Python 3.6 post from stackoverflow:')
    #start = time.time()
    print(get_author())
    #print(f'Returned in: {time.time()-start} ')


if __name__ == '__main__':
    main()
