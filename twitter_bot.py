from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Making a twitter class 
class TwitterBot:
    # Initialize a function for your twitter username and password
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # Using FireFox webdriver which is Geckgo to control FireFox browser in our system!
        self.bot = webdriver.Firefox()
    
    # Instead of logging in every time, we make a login function to DRY(Don't Repeat Yourself)    
    def login(self):
        # Using FireFox Webdriver to open and control the browser
        bot = self.bot
        # Open up the page that you want
        bot.get("https://twitter.com")
        # Actually the time to wait for loading twitter pages(It's up to you)
        time.sleep(3)
    
    
user1 = 