"""
根据上一步获取的歌手的 ID 来用于获取所有的专辑 ID
"""
import requests
from bs4 import BeautifulSoup
import time
import sys
import sql
from selenium import webdriver


browser = webdriver.Chrome(executable_path=r'/Users/yongbutingxidegunshi/Downloads/chromedriver')


class Music(object):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '_ntes_nnid=7eced19b27ffae35dad3f8f2bf5885cd,1476521011210; _ntes_nuid=7eced19b27ffae35dad3f8f2bf5885cd; usertrack=c+5+hlgB7TgnsAmACnXtAg==; Province=025; City=025; NTES_PASSPORT=6n9ihXhbWKPi8yAqG.i2kETSCRa.ug06Txh8EMrrRsliVQXFV_orx5HffqhQjuGHkNQrLOIRLLotGohL9s10wcYSPiQfI2wiPacKlJ3nYAXgM; P_INFO=hourui93@163.com|1476523293|1|study|11&12|jis&1476511733&mail163#jis&320100#10#0#0|151889&0|g37_client_check&mailsettings&mail163&study&blog|hourui93@163.com; _ga=GA1.2.1405085820.1476521280; JSESSIONID-WYYY=fb5288e1c5f667324f1636d020704cab2f27ee915622b114f89027cbf60c38be2af6b9cbef2223c1f2581e3502f11b86efd60891d6f61b6f783c0d55114f8269fa801df7352f5cc4c8259876e563a6bd0212b504a8997723a0593b21d5b3d9076d4fa38c098be68e3c5d36d342e4a8e40c1f73378cec0b5851bd8a628886edbdd23a7093%3A1476623819662; _iuqxldmzr_=25; __utma=94650624.1038096298.1476521011.1476610320.1476622020.10; __utmb=94650624.14.10.1476622020; __utmc=94650624; __utmz=94650624.1476521011.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        'DNT': '1',
        'Host': 'music.163.com',
        'Pragma': 'no-cache',
        'Referer': 'http://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    def save_music(self, artist_id):
        params = {'id': artist_id}
        # 获取专辑对应的页面
        #r = requests.get('https://music.163.com/#/artist', params=params)
        url = 'https://music.163.com/#/artist?id=' + str(params['id'])
        browser.get(url)
        browser.switch_to.frame("g_iframe")
        # 网页解析
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        body = soup.body
        musics = body.find('tbody').find_all('span',attrs={'class':'txt'})  # 获取专辑的所有音乐
        for music in musics:
            music = music.find('a')
            music_id = music['href'].replace('/song?id=', '')
            music_name = music.find('b')['title']
            print(music_name)
            print(music_id)
            sql.insert_music(music_id, music_name, artist_id)

if __name__ == '__main__':
    artists = sql.get_all_artist()
    my_music = Music()

    for i in artists:
        try:
            my_music.save_music(i['ARTIST_ID'])
        except Exception as e:
            # 打印错误日志
            print(str(i) + ': ' + str(e))
            time.sleep(5)
