from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import json
from .data_handler import data_formatter, location_engineering
from datetime import datetime
from multiprocessing import Process, Queue, Pool, Manager
import time
import json

timst = round(datetime.now().timestamp())
username = "contactus@ihclosing.com"
password = "Opozee991!"


def ciranet_crapper(location, get_result):
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
        data = location_engineering(location)
        driver.find_element_by_xpath("//input[@type='text']").send_keys(data[0])
        btn = driver.find_element_by_xpath("//dx-button[@text='Search']")
        btn.click()
        sleep(10)

        parent_of_data = driver.find_element_by_class_name('dx-datagrid-rowsview')
        html_data = parent_of_data.get_attribute('innerHTML')
        driver.close()
        data = data_formatter(html_data, "ciranet")
        get_result.append({"ciranet": data})
    except:
        html_data = {"message": "No data found"}
        driver.close()
        return get_result.append({"ciranet": html_data})


def condocerts_scrapper(location, get_result):
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
        if data == 'N/A':
            addr_for = {"message": "Invalid address format"}
            get_result.append({"condocerts": addr_for})
        else:
            driver.find_element_by_id('inputStreet1').send_keys(data[0])
            driver.find_element_by_id('inputCity').send_keys(data[1])
            driver.find_element_by_id('inputState').send_keys(data[3])
            driver.find_element_by_id('inputZip').send_keys(data[2])
            driver.find_element_by_id('continue').click()
            sleep(5)
            parent_of_data = driver.find_element_by_class_name('AddrBox')
            html_data = parent_of_data.get_attribute('innerHTML')
            driver.close()
            data = data_formatter(html_data, "condocerts")
            get_result.append({"condocerts": data})
            driver.close()
    except:
        driver.close()
        html_data = {"message": "No data found"}
        get_result.append({"condocerts": html_data})


def estoppels_scrapper(location, get_result):
    html_data = None
    driver = webdriver.Chrome(ChromeDriverManager().install())
    try:
        url = "https://estoppels.com/"
        driver.get(url)
        input_field = driver.find_element_by_class_name("select2-search__field")
        input_field.send_keys(location)
        input_field.send_keys(Keys.ARROW_DOWN)
        sleep(3)

        input_field.send_keys(Keys.ENTER)
        sleep(10)

        parent_of_data = driver.find_element_by_id('address-wrap')
        html_data = parent_of_data.get_attribute('innerHTML')
        driver.close()
        data = data_formatter(html_data, "estoppels")
        get_result.append({"estoppels": data})
    except:
        driver.close()
        html_data = {"message": "Invalid Address"}
        get_result.append({"estoppels": html_data})


def first_finder_scraper(location, get_result):
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
        if data == 'N/A':
            addr_for = {"message": "Invalid address format"}
            get_result.append({"condocerts": addr_for})
        else:
            driver.find_element_by_id('inputStreet1').send_keys(data[0])
            driver.find_element_by_id('inputZip').send_keys(data[2])
            driver.find_element_by_id('inputCity').send_keys(data[1])
            driver.find_element_by_id('inputState').send_keys(data[3])
            driver.find_element_by_id('continue').click()
            sleep(10)
            parent_of_data = driver.find_element_by_id('unitConfirmForm')
            html_data = parent_of_data.get_attribute('innerHTML')
            driver.close()
            data = data_formatter(html_data, "ff")
            get_result.append({"first_finder": data})
            driver.close()
    except:
        driver.close()
        html_data = {"message": "No data found"}
        data = get_result.append({"first_finder": html_data})


def homewise_scrapper(location, get_result):
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
        data = data_formatter(html_data, "homewise")
        get_result.append({"homewise": data})
    except:
        driver.close()
        html_data = {"message": "No data found"}
        data = get_result.append({"homewise": html_data})


def sentry_crapper(location, get_result):
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
        if data == 'N/A':
            addr_for = {"message": "Invalid address format"}
            get_result.append({"condocerts": addr_for})
        else:
            driver.find_element_by_id('inputStreet1').send_keys(data[0])
            driver.find_element_by_id('inputZip').send_keys(data[2])
            driver.find_element_by_id('inputCity').send_keys(data[1])
            driver.find_element_by_id('inputState').send_keys(data[3])
            driver.find_element_by_id("continue").click()
            sleep(10)
            parent_of_data = driver.find_element_by_id('unitConfirmForm')
            html_data = parent_of_data.get_attribute('innerHTML')
            driver.close()
            data = data_formatter(html_data, "sentry")
            get_result.append({"sentry": data})
            driver.close()
    except:
        driver.close()
        html_data = {"message": "No data found"}
        get_result.append({"sentry": html_data})


def marketplace_community(location, get_result):
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
        data = data_formatter(html_data, "market")
        get_result.append({"market": data})
    except:
        driver.close()
        html_data = {"message": "Invalid Address"}
        get_result.append({"market": html_data})


def scrapper_controller(loc):
    final_result = {}
    with Manager() as manager:
        get_result = manager.list()
        ciranet = Process(target=ciranet_crapper, args=[loc, get_result])
        condocert = Process(target=condocerts_scrapper, args=[loc, get_result])
        estoppel = Process(target=estoppels_scrapper, args=[loc, get_result])
        ff = Process(target=first_finder_scraper, args=[loc, get_result])
        homewise = Process(target=homewise_scrapper, args=[loc, get_result])
        sentry = Process(target=sentry_crapper, args=[loc, get_result])
        market = Process(target=marketplace_community, args=[loc, get_result])

        ciranet.start()
        condocert.start()
        estoppel.start()
        ff.start()
        homewise.start()
        sentry.start()
        market.start()

        ciranet.join()
        condocert.join()
        estoppel.join()
        ff.join()
        homewise.join()
        sentry.join()
        market.join()
        execution_time = time.perf_counter()
        for data in range(0, 6):
            for k, v in get_result[data].items():
                final_result[k] = v
        final_result["execution_time"] = execution_time
    return final_result

# file_name = str(timst) + '.json'
# json_object = json.dumps(final_result, indent=3)
# with open(file_name, "w") as file:
#     file.write(json_object)
# return final_result




