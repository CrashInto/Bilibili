from multiprocessing.pool import Pool
from time import sleep
from bs4 import BeautifulSoup
import re
import pymongo
import requests


M_client = pymongo.MongoClient('localhost')
M_db = M_client['B站']
M_table = M_db['我的英雄学院弹幕']

DM_front = 'https://api.bilibili.com/x/v1/dm/list.so?oid='

url_front = ['https://www.bilibili.com/bangumi/play/ep1156','https://www.bilibili.com/bangumi/play/ep2058','https://www.bilibili.com/bangumi/play/ep2001']
total = [13,26,16]
start = [3,65,60]

def Create_episode_url(session_url,total,start):
    for each in range(start,start+total):
        if each < 10:
            rest = str(0)+str(each)
        else:
            rest = str(each)
        episode_url = session_url+rest
        Parse_episode(episode_url)

def Parse_episode(url):
    response = requests.get(url).text
    sleep(0.5)
    oid = re.search('"epInfo":{.*?cid":(.*?),', response).group(1)
    soup = BeautifulSoup(response,'lxml')
    e_name = soup.select('.header-info h1')[0].get_text()
    DM_url = DM_front + oid
    Get_danmu(DM_url,e_name)

def Get_danmu(url,title):
    result = requests.get(url).content.decode('utf-8')
    sleep(0.5)
    DM = re.findall('<d.*?>(.*?)</d>', result)
    info = {
        'e_name':title,
        'danmu':DM
    }
    Save_to_mongo(info)

def Save_to_mongo(info):
    try:
        M_table.insert(info)
        print(info['e_name'] + '   ' + '的弹幕存储成功！')
    except:
        print("--------"+ info['e_name'] + "   " + "保存至mongo失败...-------")

def main():
    for i in range(0,3):
        Create_episode_url(url_front[i],total[i],start[i])

if __name__ == '__main__':
    main()
