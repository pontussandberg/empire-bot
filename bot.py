from selenium import webdriver

url = 'https://csgoempire.com/withdraw#730'
sessionID = ''

if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    driver.add_cookie({"name": "do_not_share_this_with_anyone_not_even_staff", "value" : sessionID})
    driver.refresh()
