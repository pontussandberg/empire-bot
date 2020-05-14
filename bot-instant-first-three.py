from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

url = 'https://csgoempire.com/withdraw#730'




session_ID = '4763055_8QggvyC2VHGa7MCyGkcW4SWwuOhPovkcJdQ1TiWmzPGmj8vZVQq6Z91aGsut'
min_value = 100
max_value = 195
pin = 9053
bundle_disabled = True
gloves_disabled = True




def findItems():
    last_items = ''
    print('Scanning...')

    while True:
        items = driver.find_elements_by_class_name('item__inner')[:3]


        if items != last_items:
            print('\n==========================\n')
            last_items = items

            for item in items:


                # ---> Getting the ITEM BUNDLE string, if there's a special item(i.e vanilla knife) we handle the error that's gonna be thrown. <---
                item_bundle_str = ''
                try:
                    item_bundle_str = item.find_element_by_class_name('text-xxxs.font-bold.uppercase').get_attribute('innerText')
                except NoSuchElementException:
                    pass
                # ---> Skips bundles if "bundle_disabled == True" <---
                if bundle_disabled and 'ITEM BUNDLE' in item_bundle_str:
                    print('skipping due to BUNDLE')
                    continue


                # ---> Looks for Item title, if there's a special item(i.e vanilla knife) we handle the error that's gonna be thrown. <---
                item_title = ''
                try:
                    item_title = item.find_elements_by_class_name('text-xxxs.font-bold.uppercase')[1].get_attribute('innerText')
                except IndexError:
                    pass
                # ---> Skips gloves if "gloves_disabled == True" <---
                if ( 'GLOVES' in item_title or 'WRAPS' in item_title ) and gloves_disabled :
                    print('skipping due to GLOVES')
                    continue


                # ---> Getting the value <---
                coin_elem = item.find_element_by_class_name('text-sm.font-bold.text-light-grey-2')
                value = float(coin_elem.get_attribute('innerText').replace(',',''))

                # ---> Buys item if value > than min_value <---
                if value > min_value and value < max_value:
                    item.click()

                    driver.find_element_by_class_name('capitalize.button-primary.button-primary--gold.button-primary--large.w-full').click()
                    tradeLinksWindowBtn = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.v--modal-box.v--modal > div.p-4.md\:p-6.text-light-grey-2')))

                    tradeLinksWindowBtn.find_element_by_class_name('button-primary.button-primary--gold.button-primary--large.w-full').click()
                
                    
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
                    break
                else:
                    print('skipping due to VALUE OUT OF RANGE')
            print('Items has been updated...')
                
        time.sleep(0.01)




if __name__ == '__main__':
    # Launch Chrome and log in
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)

    input('Log in, navigate to csgo-instant and no custom prices. Then press enter...')


    # driver.add_cookie({"name": "do_not_share_this_with_anyone_not_even_staff", "value" : session_ID})
    # driver.refresh()

    
    # ---> Deposit pop up <---
    # try:
    #     deposit_popup = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS, 'mb-4.md:mb-6.button-primary.button-primary--gold.button-primary--large.w-full')))
    #     deposit_popup.click()
    # except TimeoutException:
    #     pass

    # time.sleep(5)

    # # Navigate to instant(CSGO) and no custom prices
    # csgoInstant = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="page-scroll"]/div/section/div/div[1]/div[1]/div[2]/div[1]/div[1]/button')))
    # csgoInstant.click()
    # driver.find_element_by_xpath('//*[@id="page-scroll"]/div/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]').click()

    # # Waiting for the itemss to be displayed in the broser before calling findItems() and beginning the scan.
    # WebDriverWait(driver, 60).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="page-scroll"]/div/section/div/div[2]/div/div/div[1]/div[1]')))

    findItems()




    
