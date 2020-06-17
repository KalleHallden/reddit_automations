from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from decouple import config
import time

# the way to locate the button or thing you want on a website in chrome is
# by pressing cmd + shift + c and then you can use your mouse to find the 
# info on the element that you want and you can copy the full xpath.

options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
driver = webdriver.Chrome("/Users/kalle/Downloads/chromedriver83", chrome_options=options)
driver.get(config('THEATRE_SITE'))
# for some odd reason you need to reload the site for it to load.
# possibly a bug of the theatre site
driver.get(config('THEATRE_SITE'))
time.sleep(3)
# select city
button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div[2]/ul/li[1]/label/input')
button.click()

# save city
button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/span/button')
button.click()
time.sleep(2)

# proceed to tickets tab
button = driver.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div[2]/div[1]/ul[1]/li[1]/a')
button.click()
time.sleep(2)

# select the movie you want (should be more specific than just selecting the first one but whateva)
button = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/ul/li[1]/ul/li/div/div[1]/div/span[2]/a')
button.click()
time.sleep(1)

# select the time you want to go
button = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[1]/div/div/div/div[4]/section/div/div[2]/div[2]/ul/li/ul/li[1]/div/span/span[3]/span[2]/span')
button.click()
time.sleep(1)

# choose amount of people
button = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div/div/div/div/section/div/div[2]/div/button')
button.click()
time.sleep(2)

# choose seats
button = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[1]/div/div/div/div[2]/section/div[3]/div[2]/button')
button.click()
time.sleep(2)

# pay
button = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[1]/div/div/div/div[2]/section/div[4]/div/div[2]/button/span')
button.click()

