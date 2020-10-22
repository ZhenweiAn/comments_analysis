import requests
from bs4 import BeautifulSoup
import os
def getbooks():
    url = 'http://zhangailing.zuopinj.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    body = soup.body
    body = body.find('div',attrs = {'class':'content'}).find('div',attrs = {'class':'box'})
    content = body.find('div',attrs={'class':'books section-cols','id':'cols-1'})
    books = content.find_all('div',attrs={'class':'bk'})
    res = []
    for book in books:
        book = book.find('h3').find('a')

        book_url = str(book['href'])
        book_name = book.text
        res.append((book_url,book_name))
    return res
def getchapters(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    body = soup.body
    body = body.find('div',attrs = {'class':'content'}).find_all('div',attrs = {'class':'section'})[1]
    content = body.find('div',attrs={'class':'book_list'})
    chapters = content.find_all('li')
    res = []
    for chapter in chapters:
        chapter_url = str(chapter.find('a')['href'])
        chapter_name = chapter.find('a').text
        res.append((chapter_url,chapter_name))
    return res

def getcontent(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    body = soup.body
    body = body.find('div',attrs = {'class':'content'})
    body = body.find('div',attrs = {'class':'ncon','id':'articleContent'})

    body = body.find('div',attrs = {'class':'nc_l','id':'jsnc_l'})
    body = body.find('div',attrs = {'class':'contentbox','id':'htmlContent'})
    paras = body.find('p').text
    return paras

if __name__ == "__main__":
    books = getbooks()

    for book_url, book_name in books:
        book_txt = book_name + '\n'
        chapters = getchapters(book_url)
        for chapter_url,chapter_name in chapters:
            book_txt += chapter_name + '\n'
            try:
                book_txt += getcontent(chapter_url)
            except:
                book_txt += getcontent(chapter_url)
        file_name = 'zhangailingbooks/' + book_name + '.txt'
        file = open(file_name,'w',encoding='utf-8')
        file.write(book_txt)

