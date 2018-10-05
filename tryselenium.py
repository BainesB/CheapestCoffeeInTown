# for some reason scrapy can't take in the waitrose site. So I'm going to see if selenium can. 
# test code works!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import sqlite3 
import inspect 
import re 
import time

def getwaitrose():
    browser = webdriver.Firefox()
    browser.get('https://waitrose.com/ecom/shop/browse/groceries')
    thing_title = browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/main/div/div[3]/div[2]/div/div[1]/article[1]/div/section[1]/header/div[1]/a/h2/div/span[1]')
    things_titles = browser.find_elements_by_class_name('name___2sgmL')

    for i in thing_title:
        print('thing_title:',i.text)
    count = 0
    for i in things_titles:
        print('thing_title:',i.text)
        print('count',count)
        count +=1

    print('Trying to send keys')
    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    print('keys sent')
    print('lets wait 3 seconds')
    time.sleep(3)
    browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/section/button').click()
    print('try dismis servey')

    try: 
        servey = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/a/span').click()
    except:
        print('servey didnt pop up this time')
        pass

    print('find LoadButton')
    LoadButton = browser.find_element_by_class_name('primary___2xk2l')

    print('LoadButton:', LoadButton)     

    print('press Spacebar again')

    spacebarcount = 0
    for i in range(0,8):
        spacebarcount += i
        print('pressing spacebar:',i)
        webdriver.ActionChains(browser).send_keys(Keys.SPACE).perform()

    print('try clicking it') 
    browser.find_element_by_xpath('//*[contains(concat(" ", @class, " " ), concat(" ","button___2UT_5", " " ))]').click()
    print('it clicked!')

    print('Grab the list again')

    things_titles = browser.find_elements_by_class_name('name___2sgmL')

    for i in thing_title:
        print('thing_title:',i.text)
    count = 0
    for i in things_titles:
        print('thing_title:',i.text)
        print('count',count)
        count +=1
    browser.close()

x = getwaitrose()


#   /html/body/div[2]/div/map/area[1]

#    html body.scrollDown div#content div div.hasSiteSideBar main#main.appMain___2G0oc div div.products___QyYoI div#tSr.productList___2F99i div.container-fluid div.loadMoreWrapper___UneG1 button.primary___2xk2l.button___2UT_5
