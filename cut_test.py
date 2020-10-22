from pyltp import Segmentor, Postagger
import sys
import os
from tqdm import tqdm

LTP_DATA_DIR = '../Law_Sea/ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
segmentor = Segmentor()  # 初始化实例
segmentor.load(cws_model_path)  # 加载模型

postagger = Postagger() # 初始化实例
postagger.load(pos_model_path)  # 加载模型

texts = open('wangyiyun.txt','r',encoding='utf-8').readlines()
f=open('newwangyiyun.txt','w',encoding='utf-8')

for text in tqdm(texts):
    newt = segmentor.segment(text)
    postags = postagger.postag(newt)
    for i in range(len(postags)):
        if postags[i] in ['a']:
            f.write(newt[i] + ' ')


