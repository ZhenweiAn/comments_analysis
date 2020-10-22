import requests
from bs4 import BeautifulSoup
import os
def getbooks():
    url = 'http://www.jinyongwang.com/book/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    body = soup.body

    body = body.find('div',attrs = {'class':'pu_box','id':'pu_box'}).find('div',attrs = {'class':'main','id':'main'})
    body = body.find('div',attrs = {'class':'booklist'})
    content = body.find('ul',attrs={'class':'list'})
    books = content.find_all('p',attrs={'class':'title'})
    res = []
    for book in books:
        book_url = 'http://www.jinyongwang.com' + str(book.find('a')['href'])
        book_name = book.text
        res.append((book_url,book_name))
    return res
def getchapters(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    body = soup.body
    body = body.find('div',attrs = {'class':'pu_box','id':'pu_box'}).find('div',attrs = {'class':'main'})
    content = body.find('ul',attrs={'class':'mlist'})
    chapters = content.find_all('li')
    res = []
    for chapter in chapters:
        chapter_url = 'http://www.jinyongwang.com' + str(chapter.find('a')['href'])
        chapter_name = chapter.text
        res.append((chapter_url,chapter_name))
    return res

def getcontent(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    body = soup.body
    body = body.find('div',attrs = {'id':'box','class':'vertical'})
    body = body.find('div',attrs = {'class':'vcon','id':'vcon'})
    paras = body.find_all('p')
    res = ''
    for para in paras:
        res += para.text + '\n'
    return res

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
        file_name = 'jinyongbooks/' + book_name + '.txt'
        file = open(file_name,'w',encoding='utf-8')
        file.write(book_txt)

