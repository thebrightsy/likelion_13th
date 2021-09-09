from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time

#페이지 소스 가져오기 및 파싱
url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=195970&target=after&page=1"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

## 1~50페이지 가져오기
basic_url = 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=195970&target=after&page='

comment_50=[]
for i in range(1,51,1):
    real_url = basic_url + str(i)
    page = urlopen(real_url)
    soup = BeautifulSoup(page, 'html.parser')
    comment_all = soup.find_all('td', class_ = 'title')
   # print(len(comment_all))

for one in comment_all:
    temp = list(one.children)[6].strip()
    # print(temp)
    comment_50.append(temp)
    time.sleep(1)
    print(comment_50)

dict_dat = {"영화댓글":comment_50}
dat = pd.DataFrame(dict_dat)
print(dat)
dat.to_csv("댓글_과제.csv", index=False)
dat.to_excel("댓글_과제.xlsx", index=False)

import wordcloud
from wordcloud import WordCloud
from matplotlib import rc
print(wordcloud.__version__)

## 파일 읽기 함수 - open()

f = open("댓글_과제.csv", encoding='utf-8')
text = f.read()
print(text)
f.close()
rc('font', family="NanumGothic")

wcloud=WordCloud('./data/D2coding.ttf',
		        max_words=1000,
		        relative_scaling=0.2).generate(text)

import matplotlib.pyplot as plt
plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis('off')
plt.show()