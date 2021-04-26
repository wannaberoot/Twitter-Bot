from selenium import webdriver
import time
import credentials

driver = webdriver.Chrome(executable_path="assets/chromedriver.exe")
userName = credentials.userName
password = credentials.password


def twitterLogin():
    driver.get('https://twitter.com/login')
    time.sleep(5)
    text_area1 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
    text_area1.clear()
    text_area1.send_keys(userName)
    text_area = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
    text_area.clear()
    text_area.send_keys(password)
    submit_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
    submit_button.click()
    time.sleep(5)


def sendTweet(kvp):
    tweet_area = driver.find_element_by_xpath("//div[@role='textbox']")
    tweet_area.send_keys(" " + kvp)
    tweet_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div')
    tweet_button.click()
    time.sleep(3)
    driver.refresh()
