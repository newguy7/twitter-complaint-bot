import os
from twitter_login import TwitterLogin
from speedtest import SpeedTest
from dotenv import load_dotenv

load_dotenv()

class InternetSpeedTwitterBot:

    TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
    TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
    TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")

    def __init__(self, up, down):
        
        self.up = up
        self.down = down

    def get_internet_speed(self):
        speed_test = SpeedTest()
        down, up = speed_test.get_internetspeed()

        return down, up  

    def tweet_at_provider(self, message):
        login = TwitterLogin()
        login.twitter_login(username=self.TWITTER_USERNAME, password=self.TWITTER_PASSWORD)

        # Compose and send the tweet
        login.compose_twitter(message)

        # Close the browser
        login.close_browser()
