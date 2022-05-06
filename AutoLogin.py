# Used to import the webdriver from selenium
from selenium import webdriver 
import os
import time
# Get the path of chromedriver which you have install
 
def startBot(username, password, url):
    path = "/home/phongle/Downloads/chromedriver_linux64/chromedriver"
     
    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)
     
    # opening the website  in chrome.
    driver.get(url)
     
    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element_by_id(
        "id_username").send_keys(username)
     
    # find the password by inspecting on password input
    driver.find_element_by_id(
        "myInput").send_keys(password)
     
    # click on submit
    driver.find_element_by_css_selector(
        "body > div.general > div.section.group > div > a > img").click()
 
 
# Driver Code
# Enter below your login credentials
username = "20175956"
password = "Asdzxc1231"
 
# URL of the login page of site
# which you want to automate login.
url = "https://bknet7.hust.edu.vn/"

hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)

while True:
    if (response != 0):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
    #call for bot
        print("Loging in at: " + current_time)
        startBot(username, password, url)
        time.sleep(10800) #delay 1 hours
    else:
    	time.sleep(3600)
