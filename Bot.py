from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import openai
import time
import datetime
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')

def daily_quote():
    def run_daily_code():
                    
                openai.api_key = os.getenv("API_KEY")
                bot_username=os.getenv("BOT_USERNAME")
                bot_password=os.getenv("BOT_PASSWORD")

                try:
                    browser = webdriver.Chrome()
                    


                    def send_Quote(username):
                        sendmsg_button=browser.find_element(By.CSS_SELECTOR,"div[class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x78zum5 x1i0vuye xwhw2v2 x10w6t97 xl56j7k x17ydfre x1f6kntn x1swvt13 x1pi30zi x2b8uid xlyipyv x87ps6o x14atkfc x9bdzbf x1n2onr6 x1d5wrs8 x1tu34mt xzloghq']")
                        sendmsg_button.click()

                        sleep(2)
                        search_input = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Search...']")
                        search_input.send_keys(username)
                        sleep(2)

                        user_chat = browser.find_element(By.CSS_SELECTOR, "div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1']")
                        user_chat.click()
                        sleep(2)
                        
                        chat= browser.find_element(By.CSS_SELECTOR, "div[class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x78zum5 x1i0vuye xwhw2v2 xl56j7k x17ydfre x1f6kntn x2b8uid xlyipyv x87ps6o x14atkfc x9bdzbf x1n2onr6 x1d5wrs8 xn3w4p2 x5ib6vp xc73u3c x1tu34mt xzloghq']")
                        chat.click()
                        sleep(2)



                
                        try:
                    
                                response = openai.Completion.create(
                                    model="text-davinci-003",
                                    prompt='Write a Quote',
                                    temperature=1,
                                    max_tokens=256,
                                    top_p=1,
                                    frequency_penalty=0,
                                    presence_penalty=0
                                    )
                                

                                reply_text = response.choices[0].text.strip()

                                a = browser.find_element(By.XPATH, '//div[contains(@class, "x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1i64zmx xw3qccf x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1")]')
                                reply_box = browser.find_element(By.XPATH, './/div/div/p')
                                reply_box.send_keys(reply_text)
                                reply_box.send_keys(Keys.RETURN)
                                print('Quote sent')

                                sleep(2)
                                inbox_button = WebDriverWait(browser, 10).until(
                                        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/direct/inbox/']"))
                                        )
                                inbox_button.click()

                                sleep(2)



                        except Exception as e:
                                print("An error occurred:", str(e))


                    browser.get('https://www.instagram.com/')
                    sleep(2)

                    username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
                    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
                    print(username_input)
                    username_input.send_keys(bot_username)
                    password_input.send_keys(bot_password)
                    sleep(2)

                    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
                    login_button.click()
                    sleep(2)

                    inbox_button = WebDriverWait(browser, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/direct/inbox/?next=%2F']"))
                    )
                    inbox_button.click()

                    sleep(2)

                    notnow_button = browser.find_element(By.CSS_SELECTOR, "button[class='_a9-- _a9_1']")
                    notnow_button.click()

                    sleep(2)

                

                    valid_users=['_mandar_0']  #usernames whom to send quote

                    for user in valid_users:
                        send_Quote(user)

                except NoSuchElementException as e:
                    print("Element not found:", e)

                except ElementClickInterceptedException as e:
                    print("Element click intercepted:", e)

                except ElementNotVisibleException as e:
                    print("Element not visible:", e)

                except Exception as e:
                    print("An error occurred:", e)

                finally:
                    browser.quit()






                print("Running daily code at", datetime.datetime.now())





    hour = 21
    minute = 35

    while True:
        now = datetime.datetime.now()
        if now.hour == hour and now.minute == minute:
            run_daily_code()
    
            time.sleep(86400)  
        else:
        
            time.sleep(10)


if __name__ == '__main__':
    app.run()


