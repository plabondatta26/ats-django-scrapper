# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# import json
# from datetime import datetime
# import time
# import json
#
# timst = round(datetime.now().timestamp())
#
#
# def email_scrapper():
#     username = ''
#     password = ''
#
#     url = 'https://accounts.google.com/signin/v2/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
#
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.get(url)
#     driver.find_element_by_name('identifier').send_keys('plabondatta26@gmail.com')
#     driver.find_element_by_class_name('VfPpkd-vQzf8d').click()
#     sleep(10)
#     driver.close()
# email_scrapper()

import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# account credentials
username = "angel800399@gmail.com"
password = "8003998882"
host = 'imap.gmail.com'

# server =smtplib.SMTP(host='imap.gmail.com', port=587)
mail = imaplib.IMAP4_SSL(host=host)
mail.login(username, password)
mail.select('inbox')
_, search_data = mail.search(None, 'UNSEEN')
# print(status)
# print(search_data)

for num in search_data[0].split():
    # print(num)
    print('ok')
    _, data = mail.fetch(num, ('RFC822'))
    print(data)
    _, b = data[0]
    msg = str(b)
    print(msg)
    print(b, 'b')
# x = server.ehlo()
# y = server.starttls()
# z = server.login(username, password)
# print(x)
# print(y)
# print(z)
# server.quit()


# with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
#     server.login(username, password)
