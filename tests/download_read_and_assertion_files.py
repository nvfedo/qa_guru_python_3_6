from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os

# Создание файла pdf
resourses_pdf_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', r'resourses\pdf_test.pdf')))

pdf_url = 'https://freetestdata.com/wp-content/uploads/2021/09/Free_Test_Data_100KB_PDF.pdf'
response = requests.get(pdf_url, stream = True)

with open(resourses_pdf_dir, 'wb') as pdf_file:
    pdf_file.write(response.content)

# Создание файла xlsx
resourses_xlsx_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', r'resourses\xlsx_test.xlsx')))

xlsx_url = 'https://download.samplelib.com/xls/sample-simple-1.xls'
response = requests.get(xlsx_url, stream = True)

with open(resourses_xlsx_dir, 'wb') as xlsx_file:
    xlsx_file.write(response.content)

# Создание файла csv
resourses_csv_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', r'resourses\csv_test.csv')))

csv_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv'
response = requests.get(csv_url, stream = True)

with open(resourses_csv_dir, 'wb') as csv_file:
    csv_file.write(response.content)

#Добавление файлов в архив
#tbd