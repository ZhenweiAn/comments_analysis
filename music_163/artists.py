"""
获取所有的歌手信息
"""
import requests
from bs4 import BeautifulSoup
import sql
import sys
from selenium import webdriver


# 打开chrome浏览器（需提前安装好chromedriver）


def save_artist(group_id, initial):
    browser = webdriver.Chrome(executable_path=r'/Users/yongbutingxidegunshi/Downloads/chromedriver')
    params = {'id': group_id, 'initial': initial}
    url = 'http://music.163.com/discover/artist/cat?id=' + str(params['id']) + '&initial=' + str(params['initial'])

    browser.get(url)
    browser.switch_to.frame("g_iframe")

    # 网页解析
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    body = soup.body

    hot_artists = body.find_all('a', attrs={'class': 'msk'})
    for artist in hot_artists:
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        artist_name = artist['title'].replace('的音乐', '')
        print(artist_name)
        try:
            sql.insert_artist(artist_id, artist_name)
        except Exception as e:
            # 打印错误日志
            print(e)

gg = 1001

#save_artist(gg, 0)


for i in range(65, 91):
    save_artist(1001, i)
for i in range(65, 91):
    save_artist(1002, i)
