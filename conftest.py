# import requests
# import os
# from zipfile import ZipFile
# from openpyxl import Workbook
# import pytest

# Пробовал вынести создание файлов в предусловия
# @pytest.fixture()
# def download_pdf():
#     resourses_pdf_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', r'resourses\pdf_test.pdf')))

#     pdf_url = 'https://filesamples.com/samples/document/pdf/sample1.pdf'
#     response = requests.get(pdf_url, stream=True)

#     with open(resourses_pdf_dir, 'wb') as pdf_file:
#         pdf_file.write(response.content)

#     return resourses_pdf_dir


# @pytest.fixture()
# def download_csv():
#     resourses_csv_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', r'resourses\csv_test.csv')))
#
#     csv_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv'
#     response = requests.get(csv_url, stream=True)
#
#     with open(resourses_csv_dir, 'wb') as csv_file:
#         csv_file.write(response.content)


# @pytest.fixture()
# def download_xlsx():
#     resourses_xlsx_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', r'resourses\xlsx_test.xlsx')))
#
#     book = Workbook()
#     sheet = book.active
#
#     sheet['A1'] = 'Hello'
#     sheet['A2'] = 'World'
#     sheet['B1'] = 1
#     sheet['B2'] = 2
#
#     book.save(resourses_xlsx_dir)
