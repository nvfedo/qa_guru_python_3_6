from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os

# url = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png'
# response = requests.get(url=url)
# content = response.content

resourses_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resourses\pdf_test.pdf')))

url = 'https://freetestdata.com/wp-content/uploads/2021/09/Free_Test_Data_100KB_PDF.pdf'
r = requests.get(url, stream = True)

with open(resourses_dir, 'wb') as pdf_file:
    pdf_file.write(r.content)