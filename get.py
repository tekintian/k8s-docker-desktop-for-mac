#! /usr/bin/python3
# 获取最新版本的k8s
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# from lxml import etree
# import re, requests
 
# html = urlopen("https://hub.docker.com/v2/repositories/gotok8s/kube-scheduler/tags/?page_size=5&page=1&ordering=last_updated")
# bsObj = BeautifulSoup(html, "html.parser")
# images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
# for image in images: 
#     print(image["src"])

# selector = etree.HTML(html)
# links = selector.xpath('//*[@id="mainContainer"]/div/div/div[3]/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/a')
# for link in links:
#   print(link)

from urllib.request import urlopen
import json

resp = urlopen("https://hub.docker.com/v2/repositories/gotok8s/kube-scheduler/tags/?page_size=5&page=1&ordering=last_updated")
data = json.loads(resp.read())
# json_data = json.dumps(data)
print ("JSON 对象：", data['results'][0]['name'])
