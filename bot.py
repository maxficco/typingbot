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
time.sleep(15)
while True:
    if onedown == 0:
        try:
            firstletter = driver.find_element_by_class_name("is-waiting")
            print(firstletter.text)
            actions = ActionChains(driver)
            actions.send_keys(firstletter.text)
            actions.perform()
            time.sleep(speed)
        except:
            onedown = 1
            speed = speed * 0.75
            actions = ActionChains(driver)
            time.sleep(5)
            actions.send_keys(Keys.RETURN)
            actions.perform()
            time.sleep(12)
    if onedown == 1:
        try:
            firstletter = driver.find_element_by_class_name("is-waiting")
            print(firstletter.text)
            actions = ActionChains(driver)
            actions.send_keys(firstletter.text)
            actions.perform()
            time.sleep(speed)
        except:
            onedown = 0
            speed = speed * 0.75
            actions = ActionChains(driver)
            time.sleep(5)
            actions.send_keys(Keys.RETURN)
            actions.perform()
            time.sleep(12)
    if onedown == 2:
        break

print("dooooonnnneeee!")


