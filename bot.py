from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

url = 'https://csgoempire.com/withdraw#730'




sessionID = ''
minValue = 20
pin = 9053
bundleDisabled = True



def findItem():
    lastItem = ''
    print('Scanning...')

    while True:
        item = driver.find_element_by_xpath('//*[@id="page-scroll"]/div/section/div/div[2]/div/div/div[1]/div[1]')

        if item != lastItem:
            lastItem = item

            # Getting the value
            coinElem = item.find_element_by_xpath('//*[@id="page-scroll"]/div/section/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/span')
            value = float(coinElem.get_attribute('innerText').replace(',',''))
            print(value)
            # Getting the ITEM BUNDLE string
            headingElem = item.find_element_by_xpath('//*[@id="page-scroll"]/div/section/div/div[2]/div/div/div[1]/div[1]/div[1]/div[3]/div[1]')
            headingStr = headingElem.get_attribute('innerText')

            # Skips bundles if "bundleDisabled == True" 
            if bundleDisabled and headingStr.startswith('ITEM BUNDLE'):
                continue

            if value > minValue:
                item.click()
                driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div[3]/div/button').click()
                tradeLinksWindowBtn = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[7]/div/div/div[2]/div[2]/div/div[3]/div[2]/button')))
                tradeLinksWindowBtn.click()
            
                
                # Waits for the pin input to show then fills it in
                try:
                    pinInput = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[7]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/input')))
                    pinInput.send_keys(pin)
                    driver.find_element_by_xpath('//*[@id="app"]/div[7]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/button').click()
                except TimeoutException:
                    print('Something went wrong...')


                input("Press Enter to begin scanning...")
                print('Scanning...')
            print('Items updated...')
            
        time.sleep(0.01)








if __name__ == '__main__':
    # Launch Chrome and log in
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    driver.add_cookie({"name": "do_not_share_this_with_anyone_not_even_staff", "value" : sessionID})
    driver.refresh()

    # Navigate to instant(CSGO) and no custom prices
    csgoInstant = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="page-scroll"]/div/section/div/div[1]/div[1]/div[2]/div[1]/div[1]/button')))
    csgoInstant.click()
    driver.find_element_by_xpath('//*[@id="page-scroll"]/div/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]').click()

    time.sleep(10)
    findItem()




    
