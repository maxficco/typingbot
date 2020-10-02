from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "/Applications/chromedriver"
driver = webdriver.Chrome(PATH)
import time
driver.get("https://www.nitrotype.com/login")
print(driver.title)
from selenium.webdriver.common.action_chains import ActionChains
onedown = 0
speed = 0.000001
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys("maxstypingbot")
password.send_keys("lmao69")
time.sleep(20)
#while True:
letter1 = driver.find_element_by_xpath('//*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div/span[1]/span[1]')
letter2 = driver.find_element_by_xpath('//*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div/span[1]/span[2]')
letter3 = driver.find_element_by_xpath('//*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div/span[1]/span[3]')
letter4 = driver.find_element_by_xpath('//*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div/span[17]/span[5]')
print(letter1.text)
