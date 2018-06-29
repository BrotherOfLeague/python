#!/usr/bin/env python3
#coding:utf-8

import re
import os
import sys
import requests
from bs4 import BeautifulSoup

cookies = {
		'Cookie':'NTESSTUDYSI=163d9e7a8b0342b9bf0e2f9df11a83bf; EDUWEBDEVICE=4ddd60430ba24d3cae8da0cc90de34af; utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly93d3cuYmFpZHUuY29tL2xpbms/dXJsPWRZcEoxcnVzVTRyalVJbXlGRWlIeGR3SEhPZ1E0MFVCaGlJbG5VRXljTU8md2Q9JmVxaWQ9OWVlYTc3YWUwMDAwY2U2NjAwMDAwMDA2NWFmOTllZDA=; __f_=1526308565315; _ntes_nnid=64e66c4f7fa805ff7c2f62bb28215a2b,1526308546872; _ntes_nuid=64e66c4f7fa805ff7c2f62bb28215a2b; STUDY_INFO=A4CBF69253E936633819A2E772C5B807|4|1017253490|1526308591080; STUDY_SESS="cdQiMkHxjgM2g1a8+nGLxvW/S9rHBvqWQ9d2/F/Iswd1SsMmOtwZq0ZLr8is17d3qHiHb3csHPbhGWIzezlInokLXq+FiD/fDa0zp6fkzsU6WCZ2Oggpp2O5LfS8kRQ5YxFHjfsseVsiMapRgbdjS/x5pJnN6BQekm4gPcN3+WrdNz5i9lFcIuPSeV3m+gdggAd9uMV3AXu6jiU0a69PwA=="; STUDY_PERSIST="DhADfXy6Rdc49pG3ugDYdA0eQ/sddhDSDyj//I+0nfCcwAJosApYZSQh51LLCP4ULGLGANnMZdxhuHMwA6VZaWzNXg5fDP1piBNj/8/cui8z+oM1FaHBxarpbNZak5qTzysDjxic8TPMFqyQzyvHUdUSSTbbZkN0a139NYJxVWhoAz5rxcfapAwDdUXQMZONI0f2VTFzD+aF4EVJIV6IcTO448lOV8V7ewmTqLW5HHBm1qaJZ4DNwobZ7X76taGMo715LQWdFWnunKzE3cO8yZb7By9sL3t1+Lz3aQPZ79s="; NETEASE_WDA_UID=1017253490#|#1463721041349; NTES_STUDY_YUNXIN_ACCID=s-1017253490; NTES_STUDY_YUNXIN_TOKEN=e8ee331e5dab7f16718126323d206d74; __utma=129633230.170383641.1526308545.1526308545.1526308545.1; __utmb=129633230.15.9.1526308592055; __utmc=129633230; __utmz=129633230.1526308545.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'

}

headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
}
url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=64k%B3%AC%B8%DF%C7%E5%B7%D6%B1%E6%C2%CA%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000'
def getHtmlTree(url):
	# time.sleep(3)
	tmp = requests.get(url,cookies = cookies,headers = headers)
	tmp = requests.get(url,headers = headers)
	if 200 != tmp.status_code:
		print('请求异常，返回码为%s'%tmp.status_code)
		exit()
	tmp.encoding='utf-8'
	text = tmp.text
	htmlTree = BeautifulSoup(text,'html.parser')
	return htmlTree
def getImgList(url):
	htmlTree = getHtmlTree(url)
	imgListTag = htmlTree.findAll('img')
	print(imgListTag)
	imgList = []
	# print(type(imgListTag))
	print(len(imgListTag))
	for line in imgListTag:
		print(line.attrs['src'])
	# print(imgList)
getImgList(url)

def isDefine(var):
	try:
		type(var)
	except NameError:
		print('变量%s未定义'%var)
	except:
		pass
