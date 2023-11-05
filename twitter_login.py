import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TwitterLogin:
    

    def __init__(self): 

        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_argument("start-maximized")
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_option)

        self.twitter_url = "https://twitter.com/"        
        self.wait = WebDriverWait(self.driver, 10)

    def twitter_login(self, username, password):
        self.driver.get(self.twitter_url)
        time.sleep(2)
        sign_in_button = self.driver.find_element(by=By.LINK_TEXT, value="Sign in")
        sign_in_button.click()

        # Wait for the Username element to be present on the page
        username_css_selector = 'input[autocomplete="username"]'
        username_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, username_css_selector)))

        # Check if the username input field is empty
        if not username_input.get_attribute("value"):
            username_input.send_keys(username)

        time.sleep(2)    
        username_input.send_keys(Keys.ENTER)

        password_css_selector = 'input[autocomplete="current-password"]'
        password_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, password_css_selector)))
        # Check if the password input field is empty
        if not password_input.get_attribute("value"):
            password_input.send_keys(password)

        time.sleep(2)    
        password_input.send_keys(Keys.ENTER)

    def compose_twitter(self, message):
       tweet_css_selector = "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div"
       tweet_input = self.wait.until(EC.presence_of_element_located((By.XPATH, tweet_css_selector)))
       
       # Check if the tweet input field already contains text
       if tweet_input.get_attribute("value"):
            tweet_input.clear()  # Clear the existing text
       
       tweet_input.send_keys(message)
       time.sleep(2)

       post_selector = "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span"
       post_tweet = self.wait.until(EC.presence_of_element_located((By.XPATH, post_selector)))
       post_tweet.click()
       time.sleep(2)
       
    def close_browser(self):
        self.driver.quit()     




