#!/usr/bin/Python
# -*- coding: utf-8 -*-
from os import path
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud



d = path.dirname(__file__)
f = open(path.join(d, 'news.txt'),'r',encoding='utf-8').read()
text = f

stopwords = []
s_f = open('baidu_stopwords.txt','r',encoding='utf-8')
for w in s_f.readlines():
    stopwords.append(w[:-1])
print(stopwords)
wc = WordCloud(  
    font_path=r'Arial Unicode.ttf',  
    background_color="white", 
    stopwords = stopwords,  
    max_words=2000)  
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "jinyong_result.jpg"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
