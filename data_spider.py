# -*- coding: utf-8 -*-
import requests 
import sys
from bs4 import BeautifulSoup
import numpy as np
import sys

host = "http://www.lotto-8.com/"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
headers = { 'User-Agent' : user_agent }

def web_query(url):
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,"html.parser")
    number = [] 
    count = 0 
    for i in soup.select('td[style="border-bottom-style: dotted; border-bottom-color: #CCCCCC; font-size:36px;"]'):
        data = i.text.split()
        if(len(data)>1):
            while ',' in data:
                data.remove(',')
            number.append(data)
    return number

def get_data(kind,end):
    dataset = []
    for i in range(1,end): 
        query = kind+'.asp?indexpage='+str(i)+'&orderby=old'
        number = np.array(web_query(host+query)).astype('int8')
        dataset.append(number)

    dataset = np.array(dataset)
    page,item,_ = dataset.shape
    dataset = dataset.reshape(page*item,6)
    np.savetxt(kind+'.txt',dataset)
    return dataset

if __name__ == '__main__':
    data = get_data('listltobig',50)
    print('big lotto:\t',data.shape)
    print(data)
    data = get_data('listltohk',77)
    print('HK six:\t',data.shape)
    print(data)