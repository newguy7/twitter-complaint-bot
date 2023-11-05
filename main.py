from twitter_bot import InternetSpeedTwitterBot
from selenium import webdriver

PROMISED_DOWN = 800
PROMISED_UP = 100


def main():

    twitter_bot = InternetSpeedTwitterBot(PROMISED_UP, PROMISED_DOWN)

    # get the upload and download speed
    down, up = twitter_bot.get_internet_speed()
    down = float(down)
    up = float(up)
    tweet_message = f"Hey @Xfinity, why is my internet speed {down}Mbps download/{up}Mbps upload when I pay for {PROMISED_DOWN}Mbps download/{PROMISED_UP} Mbps upload?"
    
    if up < PROMISED_UP or down < PROMISED_DOWN:
        twitter_bot.tweet_at_provider(message=tweet_message)
    



if __name__ == "__main__":
    main()
