from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_options)
    for i in range(40, 269):
        driver.get("https://www.yousxs.com/player/17403_" + str(i) + ".html")
        url = driver.execute_script("return ap.audio.src")
        os.system("curl " + url + " -o " + "{:03d}".format(i) + '.mp3')
