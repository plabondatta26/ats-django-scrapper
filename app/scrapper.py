from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import json
from .data_handler import data_formatter, location_engineering
from datetime import datetime
timst = round(datetime.now().timestamp())
username = "contactus@ihclosing.com"
password = "Opozee991!"


def ciranet_crapper(location):
    html_data = None
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        url = "https://www.ciranet.com/ClosingPortal/user/login"
        url2 = "https://www.ciranet.com/ClosingPortal/newrequest"
        driver.get(url)
        driver.find_element_by_xpath("//input[@type='text']").send_keys(username)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        btn = driver.find_element_by_xpath("//dx-button[@icon='user']")
        btn.click()

        sleep(5)

        driver.get(url2)
        driver.find_element_by_xpath("//input[@type='text']").send_keys(location)
        btn = driver.find_element_by_xpath("//dx-button[@text='Search']")
        btn.click()
        sleep(10)

        parent_of_data = driver.find_element_by_class_name('dx-datagrid-rowsview')
        html_data = parent_of_data.get_attribute('innerHTML')
        driver.close()
    except:
        html_data = {"message": "Invalid Address"}
        return html_data
    return data_formatter(html_data, "ciranet")


def condocerts_scrapper(location):
    html_data = None
    driver = webdriver.Chrome(ChromeDriverManager().install())
    try:
        url = "https://secure.condocerts.com/resale/"

        driver.get(url)
        driver.find_element_by_name('email').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_id('loginButton').click()

        sleep(5)

        driver.find_element_by_id('orderNowButton').click()
        sleep(5)
        driver.find_element_by_xpath("//input[@value='u']").click()
        sleep(5)
        data = location_engineering(location)
        driver.find_element_by_id('inputStreet1').send_keys(data[0])
        driver.find_element_by_id('inputCity').send_keys(data[1])
        driver.find_element_by_id('inputState').send_keys(data[3])
        driver.find_element_by_id('inputZip').send_keys(data[2])
        driver.find_element_by_id('continue').click()
        sleep(5)
        parent_of_data = driver.find_element_by_class_name('AddrBox')
        html_data = parent_of_data.get_attribute('innerHTML')
        driver.close()
    except:
        driver.close()
        html_data = {"message": "Invalid Address"}
        return html_data
    return data_formatter(html_data, "condocerts")


def estoppels_scrapper(location):
    html_data = None
    driver = webdriver.Chrome(ChromeDriverManager().install())
    try:
        url = "https://estoppels.com/"
        driver.get(url)
        input_field = driver.find_element_by_class_name("select2-search__field")
        input_field.send_keys(location)
        input_field.send_keys(Keys.ARROW_DOWN)
        sleep(6)

        input_field.send_keys(Keys.ENTER)
        sleep(10)

        parent_of_data = driver.find_element_by_id('address-wrap')
        html_data = parent_of_data.get_attribute('innerHTML')
        driver.close()
    except:
        driver.close()
        html_data = {"message": "Invalid Address"}
        return html_data
    return data_formatter(html_data, "estoppels")


def first_finder_scraper(location):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    html_data = None
    try:
        url = "https://secure.welcomelink.com/resale/index.cfm?mg=KC"
        driver.get(url)
        sleep(5)
        driver.find_element_by_name("email").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_id('loginButton').click()
        sleep(10)
        driver.find_element_by_id('orderNowButton').click()

        sleep(10)
        data = location_engineering(location)
        driver.find_element_by_id('inputStreet1').send_keys(data[0])
        driver.find_element_by_id('inputZip').send_keys(data[2])
        driver.find_element_by_id('inputCity').send_keys(data[1])
        driver.find_element_by_id('inputState').send_keys(data[3])
        driver.find_element_by_id('continue').click()
        sleep(10)
        parent_of_data = driver.find_element_by_id('unitConfirmForm')
        html_data = parent_of_data.get_attribute('innerHTML')
        driver.close()
    except:
        driver.close()
        html_data = {"message": "Invalid Address"}
        return html_data
    return data_formatter(html_data, "ff")


def homewise_scrapper(location):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    html_data = None
    try:
        url = "https://www.homewisedocs.com/login"
        url2 = "https://www.homewisedocs.com/my-orders"

        driver.get(url)
        driver.find_element_by_name("username").send_keys("ihclosing")
        driver.find_element_by_name("password").send_keys("Opozee991!")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)

        driver.get(url2)

        input_field = driver.find_element_by_id("downshift-0-input")
        input_field.send_keys(location)
        sleep(1)

        input_field.send_keys(Keys.ARROW_DOWN)
        sleep(1)

        input_field.send_keys(Keys.ENTER)
        sleep(4)

        parent_of_data = driver.find_element_by_xpath("//div[@data-test='SearchResults']")
        html_data = parent_of_data.get_attribute('innerHTML')
        driver.close()
    except:
        driver.close()
        html_data = {"message": "Invalid Address"}
        return html_data
    return data_formatter(html_data, "homewise")


def sentry_crapper(location):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    html_data = None
    try:
        url = "https://sentry.welcomelink.com/resale/index.cfm"
        driver.get(url)
        driver.find_element_by_name('email').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_id('loginButton').click()
        sleep(10)
        driver.find_element_by_id('orderNowButton').click()
        sleep(5)
        data = location_engineering(location)
        driver.find_element_by_id('inputStreet1').send_keys(data[0])
        driver.find_element_by_id('inputZip').send_keys(data[2])
        driver.find_element_by_id('inputCity').send_keys(data[1])
        driver.find_element_by_id('inputState').send_keys(data[3])
        driver.find_element_by_id("continue").click()
        sleep(10)
        parent_of_data = driver.find_element_by_id('unitConfirmForm')
        html_data = parent_of_data.get_attribute('innerHTML')
        driver.close()
    except:
        driver.close()
        html_data = {"message": "Invalid Address"}
        return html_data
    return data_formatter(html_data, "sentry")


def marketplace_community(location):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    html_data = None
    try:
        url = "https://marketplace.communityarchives.com/login"

        driver.get(url)
        driver.find_element_by_xpath("//input[@type='email']").send_keys(username)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        driver.find_element_by_xpath("//button[@data-cy='login-button']").click()
        sleep(10)

        input_field = driver.find_element_by_xpath("//input[@aria-autocomplete='list']")
        input_field.send_keys(location)
        sleep(3)
        input_field.send_keys(Keys.ARROW_DOWN)
        sleep(2)

        input_field.send_keys(Keys.ENTER)
        sleep(2)

        parent_of_data = driver.find_element_by_class_name('content')
        html_data = parent_of_data.get_attribute('innerHTML')
        driver.close()
    except:
        driver.close()
        html_data = {"message": "Invalid Address"}
        return html_data
    return data_formatter(html_data, "market")


def scrapper_controller(loc):
    ciranet = ciranet_crapper(loc)
    condocert = condocerts_scrapper(loc)
    estoppel = estoppels_scrapper(loc)
    ff = first_finder_scraper(loc)
    homewise = homewise_scrapper(loc)
    sentry = sentry_crapper(loc)
    market = marketplace_community(loc)

    final_result = {
        "ciranet": ciranet,
        "condocert": condocert,
        "estoppel": estoppel,
        "first_finder": ff,
        "homewise": homewise,
        "sentry": sentry,
        "market": market
    }
    file_name = str(timst) + '.json'
    # json_object = json.dumps(final_result, indent=3)
    # with open(file_name, "w") as file:
    #     file.write(json_object)
    return final_result


