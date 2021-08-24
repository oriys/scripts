from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_options)
    for i in range(1, 269):
        driver.get("https://www.yousxs.com/player/17403_" + str(i) + ".html")
        skey = driver.execute_script("return skey")
        url = 'https://audio.yousxs.com:9002/mydate/%E5%8E%86%E5%8F%B2%E5%86%9B%E4%BA%8B/%E6%98%8E%E6%9C%9D%E9%82%A3%E4%BA%9B%E4%BA%8B%E5%84%BF_%E7%8E%8B%E6%9B%B4%E6%96%B0/%E6%98%8E%E6%9C%9D%E9%82%A3%E4%BA%9B%E4%BA%8B%E5%84%BF_' + "{:03d}".format(
            i) + '.mp3?skey=' + skey
        print(url)
        os.system("curl "+url+" -o "+"{:03d}".format(i) + '.mp3')
