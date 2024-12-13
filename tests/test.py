import time

def test_strategy(driver):
    print()
    start_time = time.time()
    driver.get('https://letcode.in/test')
    end_time = time.time()
    print(f'skorost vipolnenia: {end_time - start_time}')

def test(driver):
    driver.get('https://the-internet.herokuapp.com/')
    time.sleep(5)

def test1(driver):
    locator = 'ul>li:first-child<a'
    locator2 = "//a[@href='/abtest']"
    driver.get('https://the-internet.herokuapp.com/')
    print(f' Main page: {driver.current_url}')
    # time.sleep(2)
    driver.find_element('xpath', locator2).click()
    print(f' New page: {driver.current_url}')
    # time.sleep(2)
    driver.back()
    print(f' Main page second time {driver.current_url}' )
    driver.forward()
    print(f' New page: {driver.current_url}')
    driver.refresh()

def test2(driver):
    print()
    driver.get('https://the-internet.herokuapp.com/')
    url = driver.current_url
    assert url == 'https://the-internet.herokuapp.com/'
    title = driver.title
    assert title == 'The Internet'

def test4(driver):
    username_loc = "input[data-test='username']"
    password_loc = "input[data-test='password']"
    login_btn_loc = "input[data-test='login-button']"
    username = 'standard_user'
    password = 'secret_sauce'
    check_url = 'https://www.saucedemo.com/inventory.html'
    check_title = 'Swag Labs'

    driver.get('https://saucedemo.com/')
    time.sleep(1)
    driver.find_element('css selector', username_loc).send_keys(username)
    time.sleep(1)
    driver.find_element('css selector', password_loc).send_keys(password)
    time.sleep(1)
    driver.find_element('css selector', login_btn_loc).click()
    time.sleep(1)
    print(driver.current_url)
    assert driver.current_url == check_url
    assert driver.title == check_title

def test5(driver):
    locator = "div[id='selectable']"
    driver.get = 'https://letcode.in/selectable'
    time.sleep(5)
    context = driver.find_elements('css selector', locator)
    time.sleep(5)
    for i in context:
        if i.text == 'Appium':
            time.sleep(5)
            i.click()
            break
    print(context)






