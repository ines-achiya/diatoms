import requests
import os #系统函数 linux
import re
from lxml import etree


url = 'https://diatoms.org/species/'

fp = open('didi.txt', encoding='utf-8')
data = fp.read()
proxies = {
  "http": "http://127.0.0.1:8001",
  "https": "http://127.0.0.1:8001",
}
list_ul = re.findall("<ul(.*?)</ul>", data) #通配符-(.*?)   .findall函数-查找所有符合条件自动生成list
# print(list_ul)
count=0
for ul in list_ul:
    # print(ul[90:])
    title = re.findall("\">(.*?)</a></h2>", ul[90:])[0]  #\-转义符
    title_2 = []
    title_2_url = []
    list_li = re.findall("<li>(.*?)</li>", ul)[1:]
    # print(list_li)
    for li in list_li:
        sub = re.findall(">(.*?)</a>", li)[0].strip(' ') #去空
        if "span" in sub:
            sub = re.findall("(.*?)<span", sub)[0].strip(' ')
        title_2.append(sub[3:])

        t_url = re.findall("href=\"(.*?)\"", li)[0]
        title_2_url.append(t_url)
        # print("a")
    for i in range(0, len(title_2_url)):
        r = requests.get(title_2_url[i],proxies=proxies)
        html = etree.HTML(r.text)
        p = '//*[@class="image-set"]/a/img/@src'
        aa=html.xpath(p)
        #print(list_img)
        k = 1
        for img in aa:
            if img[-4:] != '.jpg' and  img[-5:] != '.jpeg' and  img[-4:] != '.png':
                continue
                # print("b")
                # print(img)
            print(img)
            count+=1
                #print("c")
               #print("d")]

            print(count)
print(count)
