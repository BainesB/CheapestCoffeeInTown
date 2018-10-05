from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import sqlite3 
import inspect 
import re 
import time

DBName = 'waitrose3.db'

def getwaitrose():
    browser = webdriver.Firefox()
    browser.get('https://waitrose.com/ecom/shop/browse/groceries')
    try:   
        for i in range(0,3):
    
            things = []

            things_title = browser.find_elements_by_class_name('name___2sgmL')
            things_price = browser.find_elements_by_class_name('prices___1JkR4 span span')
            countstuff = 0

            # turn price string into float ready for db
            for i in things_title:
                countstuff += 1
                cleanprice = things_price[countstuff].text.strip('£')
                if 'p' in cleanprice:
                    cleanprice = '0.'+cleanprice.strip('p')
                elif 'each est.' in cleanprice:
                    cleanprice = '0.'+cleanprice.strip('each est.')
                else: 
                    pass
                #print('check error', cleanprice)
                # replace ' ' with '_' 
                things.append((i.text.replace(' ','_') ,float(cleanprice))) 
            
            count = 0

            for i in things:
                #print('thing_title>>>',i[0],'thing_price>>>',i[1])
                #print('count',count)
                count +=1
            try:
                print('knock down pop up')
                webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
                print('keys sent')
                print('lets wait 1 seconds')
                time.sleep(1)
                browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/section/button').click()
            except:
                print('Cookei button not there anymore')

            print('try dismis servey')
            try: 
                servey = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/a/span').click()
            except:
                print('servey didnt pop up this time')
                pass

            #print('find LoadButton')
            LoadButton = browser.find_element_by_class_name('primary___2xk2l')
            #print('LoadButton:', LoadButton)     

            #print('press Spacebar again')
            spacebarcount = 0
            for i in range(0,8):
                spacebarcount += i
                #print('pressing spacebar:',i)
                webdriver.ActionChains(browser).send_keys(Keys.SPACE).perform()

            print('try clicking it') 
            browser.find_element_by_xpath('//*[contains(concat(" ", @class, " " ), concat(" ","button___2UT_5", " " ))]').click()
            print('it clicked!')
            print('first thing:',things[0])
            print('things has items:', len(things))
            print('last item:', things[len(things)-1])
            print('middle item', things[int(len(things)/2)])

    except:
        # dump the stuff in a db. 
        # only need to go in the db at the last run of the webbrowser. 
    
        conn = sqlite3.connect(DBName)
        cursor = conn.cursor()

        # put title and prices in a db

        for i in things:
            print('Enter title in DB:', i[0]) 
            try:
                cursor.execute(f'''
                INSERT INTO products (title, price)
                VALUES('{str(i[0])}',{i[1]});
                ''')

                conn.commit()
            except: 
                print('d\'oh')
                pass

    conn = sqlite3.connect(DBName)
    cursor = conn.cursor()

    # put title and prices in a db

    for i in things:
        print('Enter title in DB:', i[0]) 
        try:
            cursor.execute(f'''
            INSERT INTO products (title, price)
            VALUES('{str(i[0])}',{i[1]});
            ''')

            conn.commit()
        except: 
            print('d\'oh')
            pass

    cursor.close()
    conn.close()

    browser.close()

x = getwaitrose()


