# vmgirls 精美私房写真

import requests

from lxml import etree

import re

# 要请求的url
baseUrl = 'https://www.vmgirls.com/'

# 指定爬取的图片存储的位置
basePath = '/Users/daixin/desktop/Grirls写真'

# pattern = re.compile(r'https:.*jpeg', re.S)

# 发送请求
# res = requests.get(baseUrl)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    # 'cookies': 'dy_did=aba21abd121e7351e6e5433300051501; acf_did=aba21abd121e7351e6e5433300051501; PHPSESSID=5pdm1nejmcmc1gsoaj615haik5; acf_uid=375135143; acf_username=375135143; acf_nickname=Kris7248; acf_own_room=0; acf_groupid=1; acf_phonestatus=0; acf_avatar=https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar%2Fdefault%2F02_; acf_ct=0; acf_ltkid=49676269; acf_biz=1; acf_auth=f034tDnaA545KZnor1fO3YodmODFwOLiv2OfVLVUI%2FG%2FvLlyUBkj2k0uydNm6e1%2FsnGFysWYYMPTCkmkjVTs7Ee7vr5Ec%2BsSCWqASv6a7P%2F7XIEXRPIM8IE; dy_auth=e4bf9uMvD%2B2D67zLQIGXQRjzAQllamvhxvnFn1Xb2DSJZ6pnWGzugzZaPVPPQMCuNUaRtVuU7lAxHdG%2Bru2C%2BjhUynjux1ldFwIia0lNbDhmKDAYN5WtH5M; wan_auth37wan=b8dea5a564b6oNirKTBCHaGAia29b24RLHXmTkiyIlpPFV0lQBpRAnkblSY0Goj94TQbQaPDGUjTIXlve%2Bp5ch67ClDD820YbjhxJGePqxN7wZmK4UE; acf_stk=acb42826682f9e8a'
}

res = requests.request('GET', url=baseUrl, headers=headers)

element = etree.HTML(res.text)

pic_list = element.xpath('//div[@class="container"]/div[contains(@class, "row")]/div[contains(@class, "col-6")]')

print('爬取开始...')

for pic in pic_list:
    img_url = pic.xpath('.//div[contains(@class, "media") and contains(@class, "media-16x9")]/a[@class="media-content"]/@data-bg')
    title = pic.xpath('.//div[contains(@class, "media") and contains(@class, "media-16x9")]/a[@class="media-content"]/@title')
    # 判断img_url 是否为空list
    if(img_url and title):
        # 正则表达式来获取指定的image url
        new_img_url = re.search(r'https:.*jpeg', img_url[0]).group(0)

        # 获取tile
        new_title = title[0]
        # 请求获取 image 内容, 注意必要要加header, 否则爬取的图片内容将会失败
        res1 = requests.get(new_img_url, headers=headers)

        with open('{0}/{1}.png'.format(basePath, new_title), 'wb') as f:
            f.write(res1.content)
    print(new_title + " 图片保存完成")

print('爬取结束....')