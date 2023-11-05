import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class SpeedTest:

    def __init__(self):

        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_argument("start-maximized")
        self.chrome_option.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_option)
        self.speedtest_url = "https://www.speedtest.net/"
        

    def get_internetspeed(self):
        
        self.driver.get(self.speedtest_url)
        time.sleep(2)
        speed_test = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a span.start-text")
        speed_test.click()
        time.sleep(40)

        # Get the download speed
        download_speed = self.driver.find_element(By.CSS_SELECTOR, value="span.download-speed")
        down_speed = download_speed.text

        # Get the upload speed
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, value="span.upload-speed")
        up_speed = upload_speed.text

        return down_speed, up_speed   
        
    
    def close_browser(self):
        self.driver.quit()



    





