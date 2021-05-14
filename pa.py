from os import name
from bs4.builder import HTML
import requests
from bs4 import BeautifulSoup
import mysql.connector

conn = mysql.connector.connect(host='localhost',
                         database='rusprofile',
                         user='sammy',
                         password='Password1.')
cursor = conn.cursor()



URL = 'https://www.rusprofile.ru/codes/89220'
HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15'}

def get_data(url):
    data = requests.get(url, headers=HEADERS)
    return data


b = list()
c = list()


def pars():
    html = get_data(URL).text
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find_all('div', class_='company-item')
    for data in item:
        items = data.find('div', class_='company-item__title').get_text()
        b.append(items.strip())
        if data.find_all('span', class_='attention-text'):
            c.append('В процессе ликвидации')
        elif data.find_all('span', class_='warning-text'):
            c.append('Ликвидирована')
        else:
            c.append('Действующая')
        it = data.find_all('div', class_='company-item-info')
        for i in it[1::4]:
            red = i.find_all('dl')
            for j in red:
                x = red[0].find('dd').get_text()
                x1 = red[1].find('dd').get_text()
                x2 = red[2].find('dd').get_text()
                try:
                    x3 = red[3].find('dd').get_text()
                except:
                    x3 = 'None'
            sql1 = (f"INSERT INTO profiles(names, ogrn, okpo, statuses, dates, kapital) VALUES ('{b[-1]}', '{x}', '{x1}', '{c[-1]}', '{x2}', '{x3}')")
            cursor.execute(sql1)
            conn.commit()

URL1 = 'https://www.rusprofile.ru/codes/429110'


def get_data1(url):
    data = requests.get(url, headers=HEADERS)
    return data

def pars1():
    html = get_data1(URL1).text
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find_all('div', class_='company-item')
    for data in item:
        items = data.find('div', class_='company-item__title').get_text()
        b.append(items.strip())
        if data.find_all('span', class_='attention-text'):
            c.append('В процессе ликвидации')
        elif data.find_all('span', class_='warning-text'):
            c.append('Ликвидирована')
        else:
            c.append('Действующая')
        it = data.find_all('div', class_='company-item-info')
        for i in it[1::4]:
            red = i.find_all('dl')
            for j in red:
                x = red[0].find('dd').get_text()
                x1 = red[1].find('dd').get_text()
                x2 = red[2].find('dd').get_text()
                try:
                    x3 = red[3].find('dd').get_text()
                except:
                    x3 = 'None'
            sql1 = (f"INSERT INTO profiles(names, ogrn, okpo, statuses, dates, kapital) VALUES ('{b[-1]}', '{x}', '{x1}', '{c[-1]}', '{x2}', '{x3}')")
            cursor.execute(sql1)
            conn.commit()

URL2 = 'https://www.rusprofile.ru/codes/429110/2/'


def get_data1(url):
    data = requests.get(url, headers=HEADERS)
    return data

def pars2():
    html = get_data1(URL2).text
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find_all('div', class_='company-item')
    for data in item:
        items = data.find('div', class_='company-item__title').get_text()
        b.append(items.strip())
        if data.find_all('span', class_='attention-text'):
            c.append('В процессе ликвидации')
        elif data.find_all('span', class_='warning-text'):
            c.append('Ликвидирована')
        else:
            c.append('Действующая')
        it = data.find_all('div', class_='company-item-info')
        for i in it[1::4]:
            red = i.find_all('dl')
            for j in red:
                x = red[0].find('dd').get_text()
                x1 = red[1].find('dd').get_text()
                x2 = red[2].find('dd').get_text()
                try:
                    x3 = red[3].find('dd').get_text()
                except:
                    x3 = 'None'
            sql1 = (f"INSERT INTO profiles(names, ogrn, okpo, statuses, dates, kapital) VALUES ('{b[-1]}', '{x}', '{x1}', '{c[-1]}', '{x2}', '{x3}')")
            cursor.execute(sql1)
            conn.commit()


pars()
pars1()
pars2()