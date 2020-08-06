# 分析:
#      1. 返回的html 内容中不包含我们想要的节点
#      2. 豆瓣电影网页采用动态加载技术(jQuery) 来加载数据

import requests

import json

from lxml import etree

# URL you want to extract data
baseUrl = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=60"

basePath = 'C:/Users/krisd/Desktop/Beauty'

# response = requests.get(baseUrl)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Language': 'en-US,en;q=0.9'
}

cookies = {
    'Cookie': 'll="108231"; bid=vZ9FJ908Odw; ap_v=0,6.0; __utmc=30149280; __utmz=30149280.1596696247.1.1.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=223695111; __utmz=223695111.1596696247.1.1.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __yadk_uid=oVVy1K6MWsyAeyo6cnKK1Q0FOfq7JiRf; __gads=ID=1efa6a1d5817012b:T=1596696250:S=ALNI_MYLwTJNrgJjuMr9Z50PBv-aYMV2GQ; _vwo_uuid_v2=DAF6C4C7CD225FE4E734B92CB220D5894|4339a50c18b70f66aa41bb688c6aeede; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1596702409%2C%22https%3A%2F%2Fwww.bing.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.2021881981.1596696247.1596696247.1596702410.2; __utmb=30149280.0.10.1596702410; __utma=223695111.67539947.1596696247.1596696247.1596702410.2; __utmb=223695111.0.10.1596702410; dbcl2="159275176:4o9evdiHQRk"; ck=xrtr; _pk_id.100001.4cf6=413cdc323c26999b.1596696247.2.1596702764.1596696859.; push_doumail_num=0; push_noty_num=1'
}

print('爬取开始...')

response = requests.request('GET', baseUrl, headers=headers, cookies=cookies)

# print(response.text)


movie_dict = json.loads(response.text)

for movie_item in movie_dict['subjects']:
    movie_name = movie_item.get('title')
    movie_img = movie_item.get('cover')
    movie_rate = movie_item.get('rate')
    # print('movie name: ' + movie_name + ', movie image: ' +
    #       movie_img + ', movie rate: ' + movie_rate)

    res = requests.get(movie_img)

    with open('{0}/{1}.jpg'.format(basePath, movie_name), 'wb') as f:
        f.write(res.content)

print('爬取介绍...')

# element = etree.HTML(response.text)


# pic_list = element.xpath(
#     '//div[@class="list-wp"]//a[@class="item"]')

# print(pic_list)

# for pic in pic_list:
#     pic_path = pic.xpath('./div[@class="cover-wp"]/img/@src')
#     print(pic_path)