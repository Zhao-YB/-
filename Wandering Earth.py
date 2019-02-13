#!/usr/bin/env python
# coding: utf-8

import requests
import jieba
import wordcloud
import re
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup as bs

get_ipython().run_line_magic('matplotlib', 'inline')


def clean_punctuations(corpus):
    corpus_list = []
    for word in corpus:
        if word not in ['，',',','：', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '--', '.', '..', '...', '......', '...................', './', '.一', '.数', '.日', '/', '//', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', '://', '::', ';', '<', '=', '>', '>>', '?', '@', 'A', 'Lex', '[', '\\', ']', '^', '_', '`', 'exp', 'sub', 'sup', '|', '}', '~', '~~~~', '·', '×', '×××', 'Δ', 'Ψ', 'γ', 'μ', 'φ', 'φ．', 'В', '—', '——', '———', '‘', '’', '’‘', '“', '”', '”，', '…', '……', '…………………………………………………③', '′∈', '′｜', '℃', 'Ⅲ', '↑', '→', '∈［', '∪φ∈', '≈', '①', '②', '②ｃ', '③', '③］', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '──', '■', '▲', '', '、', '。', '〈', '〉', '《', '》', '》），', '」', '『', '』', '【', '】', '〔', '〕', '〕〔', '㈧', '一', '一.', '一一',';']:
            corpus_list.append(word)
    return corpus_list


cookies = {'Cookie': 'bid=J8hpaGe6I_k; douban-fav-remind=1; ll="118151"; ap_v=0,6.0; __utmc=30149280; __utma=223695111.754411372.1543566701.1543567145.1550040949.3; __utmb=223695111.0.10.1550040949; __utmc=223695111; __utmz=223695111.1550040949.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.661833863.1543566694.1550040949.1550040950.3; __utmz=30149280.1550040950.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.3.10.1550040950; dbcl2="180200009:iFrqkzlt+/U"; ck=irB3; push_noty_num=0; push_doumail_num=0'}
content = requests.get('https://movie.douban.com/subject/26266893/comments?start=400&limit=20&sort=new_score&status=P',cookies=cookies).text
soup = bs(content)
soup.find_all(class_="short")[0].string
shorts_list = []
for page in range(0,500,20):
    url = 'https://movie.douban.com/subject/26266893/comments?start='+str(page)+'&limit=20&sort=new_score&status=P'
    print('正在爬取',url)
    content = requests.get(url,cookies=cookies).text
    soup = bs(content)
    shorts = soup.find_all(class_="short")
    
    for short in shorts:
        shorts_list.append(short.string)

print('+++++++++++++++++++++++已完成+++++++++++++++++++++++')

fenci = list(jieba.cut(shorts_list[0]))

corpus = []
for short in shorts_list:
    
    fenci = clean_punctuations(list(jieba.cut(short)))
    corpus.extend(fenci)
    
corpus
from wordcloud import WordCloud
space_corpus = ' '.join(corpus)

pic = WordCloud(font_path='nahan.TTF',width=800,height=400,max_words=50,max_font_size=200).generate(space_corpus)
plt.imshow(pic)
plt.grid('False')
plt.axis('off')
plt.show()
#出结果可视化，可保存