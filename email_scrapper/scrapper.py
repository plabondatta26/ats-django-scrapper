# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# import json
# from datetime import datetime
# from multiprocessing import Process, Queue, Pool, Manager
# import time
# import json
#
#
# timst = round(datetime.now().timestamp())
# username = "contactus@ihclosing.com"
# password = "Opozee991!"
#
#
# def inspect_scrapper(location, get_result):
#     html_data = None
#     try:
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         url = "https://www.ciranet.com/ClosingPortal/user/login"
#         url2 = "https://www.ciranet.com/ClosingPortal/newrequest"
#         driver.get(url)
#         driver.find_element_by_xpath("//input[@type='text']").send_keys(username)
#         driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
#         btn = driver.find_element_by_xpath("//dx-button[@icon='user']")
#         btn.click()
#
#         sleep(5)
#
#         driver.get(url2)
#         # data = location_engineering(location)
#         driver.find_element_by_xpath("//input[@type='text']").send_keys(data[0])
#         btn = driver.find_element_by_xpath("//dx-button[@text='Search']")
#         btn.click()
#         sleep(10)
#
#         parent_of_data = driver.find_element_by_class_name('dx-datagrid-rowsview')
#         html_data = parent_of_data.get_attribute('innerHTML')
#         driver.close()
#         data = data_formatter(html_data, "ciranet")
#         get_result.append({"ciranet": data})
#     except:
#         html_data = {"message": "No data found"}
#         driver.close()
#         return get_result.append({"ciranet": html_data})
