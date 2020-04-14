#-*- coding: utf-8 -*-
from urllib.error import HTTPError
import json as js
from pandas.io import json
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import datetime

#headless mode
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')
# chrome_options.add_argument("--disable-gup")
# chrome_options.add_argument("lang=ko_KR")

url = 'https://finance.daum.net/domestic'
chrome_options = Options()
chrome_options.add_argument('Content-Type=application/json; charset=utf-8')
driver = webdriver.Chrome('D:\Downs\chromedriver\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)
driver.get(url)

investors = {}
investors['foreign'] = driver.find_element_by_css_selector('#boxDashboard > div > div:nth-child(1) > div > div.txtB > dl:nth-child(2) > dd:nth-child(2) > a > p').text
investors['institution'] = driver.find_element_by_css_selector('#boxDashboard > div > div:nth-child(1) > div > div.txtB > dl:nth-child(2) > dd:nth-child(4) > a > p').text
investors['person'] = driver.find_element_by_css_selector('#boxDashboard > div > div:nth-child(1) > div > div.txtB > dl:nth-child(2) > dd:nth-child(3) > a > p').text
investors['program'] = driver.find_element_by_css_selector('#boxDashboard > div > div:nth-child(1) > div > div.txtB > dl:nth-child(2) > dd:nth-child(5) > a > p').text
print(investors)


categoryhigh = {}
driver.implicitly_wait(60)
categoryhigh['1name'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(1) > table > tbody > tr.first > th:nth-child(1) > a').text
categoryhigh['1up'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td > span').text
categoryhigh['2name'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > th:nth-child(1) > a').text
categoryhigh['2up'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > td > span').text
categoryhigh['3name'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > th:nth-child(1) > a').text
categoryhigh['3up'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > td > span').text
categoryhigh['4name'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > th:nth-child(1) > a').text
categoryhigh['4up'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > td > span').text
categoryhigh['5name'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(1) > table > tbody > tr.last > th:nth-child(1) > a').text
categoryhigh['5up'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(1) > table > tbody > tr.last > td > span').text
print(categoryhigh)

stockhigh = {}
driver.implicitly_wait(60)
stockhigh['1name'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(1) > table > tbody > tr.first > th:nth-child(1) > a').text
stockhigh['1up'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td > span').text
stockhigh['2name'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > th:nth-child(1) > a').text
stockhigh['2up'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > td > span').text
stockhigh['3name'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > th:nth-child(1) > a').text
stockhigh['3up'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > td > span').text
stockhigh['4name'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > th:nth-child(1) > a').text
stockhigh['4up'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > td > span').text
stockhigh['5name'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(1) > table > tbody > tr.last > th:nth-child(1) > a').text
stockhigh['5up'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(1) > table > tbody > tr.last > td > span').text
print(stockhigh)


foreignbuy = {}
driver.implicitly_wait(60)
foreignbuy['1name'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr.first > th:nth-child(1) > a').text
foreignbuy['1up'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td > span').text
foreignbuy['2name'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > th:nth-child(1) > a').text
foreignbuy['2up'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > td > span').text
foreignbuy['3name'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > th:nth-child(1) > a').text
foreignbuy['3up'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > td > span').text
foreignbuy['4name'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > th:nth-child(1) > a').text
foreignbuy['4up'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > td > span').text
foreignbuy['5name'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr.last > th:nth-child(1) > a').text
foreignbuy['5up'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr.last > td > span').text
print(foreignbuy)


institutionbuy = {}
driver.implicitly_wait(60)
institutionbuy['1name'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr.first > th:nth-child(1) > a').text
institutionbuy['1up'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td > span').text
institutionbuy['2name'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > th:nth-child(1) > a').text
institutionbuy['2up'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > td > span').text
institutionbuy['3name'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > th:nth-child(1) > a').text
institutionbuy['3up'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > td > span').text
institutionbuy['4name'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > th:nth-child(1) > a').text
institutionbuy['4up'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > td > span').text
institutionbuy['5name'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr.last > th:nth-child(1) > a').text
institutionbuy['5up'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(1) > table > tbody > tr.last > td > span').text
print(institutionbuy)


driver.find_element_by_xpath('//*[@id="boxSectorsPriceChange"]/div[1]/ul/li[2]/a').click()
# driver.implicitly_wait(60)
categoryrow = {}
categoryrow['1name'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(2) > table > tbody > tr.first > th:nth-child(1) > a').text
categoryrow['1up'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(2) > table > tbody > tr.first > td > span').text
categoryrow['2name'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(2) > th:nth-child(1) > a').text
categoryrow['2up'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(2) > td > span').text
categoryrow['3name'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(3) > th:nth-child(1) > a').text
categoryrow['3up'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(3) > td > span').text
categoryrow['4name'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(4) > th:nth-child(1) > a').text
categoryrow['4up'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(4) > td > span').text
categoryrow['5name'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(2) > table > tbody > tr.last > th:nth-child(1) > a').text
categoryrow['5up'] = driver.find_element_by_css_selector('#boxSectorsPriceChange > div.box_contents > div:nth-child(2) > table > tbody > tr.last > td > span').text
print(categoryrow)

driver.find_element_by_xpath('//*[@id="boxUpDownItems"]/div[1]/ul/li[2]/a').click()
driver.implicitly_wait(60)
stocklow = {}
stocklow['1name'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(2) > table > tbody > tr.first > th:nth-child(1) > a').text
stocklow['1up'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(2) > table > tbody > tr.first > td > span').text
stocklow['2name'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(2) > th:nth-child(1) > a').text
stocklow['2up'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(2) > td > span').text
stocklow['3name'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(3) > th:nth-child(1) > a').text
stocklow['3up'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(3) > td > span').text
stocklow['4name'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(4) > th:nth-child(1) > a').text
stocklow['4up'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(4) > td > span').text
stocklow['5name'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(2) > table > tbody > tr.last > th:nth-child(1) > a').text
stocklow['5up'] = driver.find_element_by_css_selector('#boxUpDownItems > div.box_contents > div:nth-child(2) > table > tbody > tr.last > td > span').text
print(stocklow)

driver.find_element_by_xpath('//*[@id="boxForeignNetFlow"]/div[1]/ul/li[2]/a').click()
driver.implicitly_wait(60)
foreignsell = {}
foreignsell['1name'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr.first > th:nth-child(1) > a').text
foreignsell['1up'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr.first > td > span').text
foreignsell['2name'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(2) > th:nth-child(1) > a').text
foreignsell['2up'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(2) > td > span').text
foreignsell['3name'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(3) > th:nth-child(1) > a').text
foreignsell['3up'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(3) > td > span').text
foreignsell['4name'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(4) > th:nth-child(1) > a').text
foreignsell['4up'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(4) > td > span').text
foreignsell['5name'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr.last > th:nth-child(1) > a').text
foreignsell['5up'] = driver.find_element_by_css_selector('#boxForeignNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr.last > td > span').text
print(foreignsell)

driver.find_element_by_xpath('//*[@id="boxInstitutionNetFlow"]/div[1]/ul/li[2]/a').click()
driver.implicitly_wait(60)
institutionsell = {}
institutionsell['1name'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr.first > th:nth-child(1) > a').text
institutionsell['1up'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr.first > td > span').text
institutionsell['2name'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(2) > th:nth-child(1) > a').text
institutionsell['2up'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(2) > td > span').text
institutionsell['3name'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(3) > th:nth-child(1) > a').text
institutionsell['3up'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(3) > td > span').text
institutionsell['4name'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(4) > th:nth-child(1) > a').text
institutionsell['4up'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr:nth-child(4) > td > span').text
institutionsell['5name'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr.last > th:nth-child(1) > a').text
institutionsell['5up'] = driver.find_element_by_css_selector('#boxInstitutionNetFlow > div.box_contents > div:nth-child(2) > table > tbody > tr.last > td > span').text
print(institutionsell)

list = [investors, categoryhigh, categoryrow, stockhigh, stocklow, foreignbuy, foreignsell, institutionbuy, institutionsell]
print(list)
with open('C:\\Users\\hong\\Documents\\GitHub\\Java_Spring\\toojaatte\\toojaatte\\src\\main\\resources\\com\\toojaatte\\stock\\crawlingtest\\stockmain.json',
          'w', encoding='utf-8') as f:
    f.write(js.dumps(list, ensure_ascii=False))
