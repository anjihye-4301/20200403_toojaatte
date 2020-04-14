import json
import os
from datetime import datetime
import time
from bs4 import BeautifulSoup as bs
import requests

start = time.time()
#네이버뉴스 리스트에 접속해서 뉴스 기사 1개씩의 url 긁어오기
def getURL(date, page):
    # 링크 저장할 배열
    href = []

    for i in range(1, page+1):
        baseURL = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=258&sid1=101&date="+date+"&page=" + str(i)

        req = requests.get(baseURL)
        # print(req)

        soup = bs(req.text, 'lxml')
        # print(soup)

        # ul tag의 class가 두개로 나뉨
        headline = soup.find('ul', {'class': 'type06_headline'})
        # print(headline)
        aTag = headline.select('li > dl > dt > a')
        # print(aTag)
        # print(len(aTag))

        for a in aTag:
            link = a.attrs['href']
            # print(link)
            href.append(link)

        noHeadline = soup.find('ul', {'class': 'type06'})
        aTag2 = noHeadline.select('li > dl > dt > a')

        for a in aTag2:
            link = a.attrs['href']
            href.append(link)

    href = list(set(href))
    # print(href)
    # print(len(href))
    return href


def getnews(date, page):
    newslist = []  # json에 저장할 뉴스 리스트
    url = getURL(date, page)

    for u in url:
        # 1개 뉴스의 정보 dictionary(key,value)
        dict = {}

        baseURL = u
        # print(u)

        req = requests.get(baseURL)
        soup = bs(req.text, 'lxml')
        # print(soup)

        # 기사 원본 링크
        dict['url'] = baseURL
        # print(baseURL)

        # 언론사 정보(링크, 사진, 회사명) 소스 통째로
        press = soup.find('a', {'class': 'nclicks(atp_press)'})
        # print(press)
        dict['press'] = str(press)

        # 제목
        title = soup.find('title').string
        pos = title.index(':')  # ':네이버뉴스' 잘라내기
        title = title[:pos]
        # print(title)
        dict['title'] = title

        # 작성일
        write_date = soup.find('span', {'class':'t11'}).string
        # print(write_date)
        dict['write_date'] = write_date

        # # 이미지+캡션 (null일수도 있음)
        # image = soup.find('span', {'class':'end_photo_org'})
        # print(image)

        # 내용 (이미지 포함하여 html 소스로 통째로 가져온다.)
        content = soup.select('div#articleBodyContents')
        # print(content)
        dict['content'] = str(content)

        # print(dict)
        newslist.append(dict)  # 뉴스를 리스트에 추가
        # break

    print(newslist)

    date = datetime.today().strftime("%Y%m%d")
    with open(os.path.join('.',
        'C:\\Users\\hong\\Documents\\GitHub\\Java_Spring\\toojaatte\\toojaatte\\src\\main\\resources\\com\\toojaatte\\stock\\'
        'crawlingtest\\news'+date+'.json'), 'w', encoding='utf-8') as f:
        json.dump(newslist, f, ensure_ascii=False, indent='\t')

    # # #파일 append할때
    # with open(os.path.join('.', 'crawled\\news.json'), 'a', encoding='utf-8') as f:
    #     #★ json파일 append하면 [][] 리스트뒤에 바로 리스트붙어서 오류남
    #     #손코딩으로 ]삭제하여 붙여주고 ,붙이고 ]붙임.
    #     f.seek(0, os.SEEK_END)
    #     f.seek(f.tell() - 1, os.SEEK_SET)
    #     f.truncate()
    #     f.write(',')
    #     json.dump(newslist, f, ensure_ascii=False, indent='\t')
    # #     # f.write(']')



# 함수호출-----------------------------------------------------------------------
date = datetime.today().strftime("%Y%m%d")
# date = '20200326'
# print(date)
page = 5
getnews(date, page)  # 뉴스리스트 url에 들어갈 날짜와 페이지번호
print("걸린시간 :", time.time() - start)
