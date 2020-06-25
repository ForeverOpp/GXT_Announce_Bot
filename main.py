# /html/body/form/div[3]/div[4]/div[2]/div/table/tbody/tr[2]/td[3]
import requests
from lxml import etree
from MessageSender import MessageSender
import time

__header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
__domain = "http://gxt.nmg.gov.cn/Xinxigongkai/GongkaiMulu/"
__index = "newGongkaiMulu.aspx?e=tz"
__sleepTime = 10 * 60
m = MessageSender("Bark")
m.config({'apikey': "gpKSL4RQYEZyTiKyz9vtEe", 'linkMode': True})
announce = {'title': ""}
while True:
    try:
        html = requests.get(__domain + __index).text
        data = etree.HTML(html)
        title = str(data.xpath('//*[@id="GVData"]/tr[2]/td[3]/a//text()')[0])
        t = str(data.xpath('//*[@id="GVData"]/tr[2]/td[4]/span/text()')[0])
        link = __domain + str(data.xpath('//*[@id="GVData"]/tr[2]/td[3]/a/@href')[0])
    except:
        continue
    else:
        tmpAnnounce = {'title': title, 'content': "发布日期：" + t + "，点击查看", 'link': link}
        if tmpAnnounce['title'] == announce['title']:
            time.sleep(__sleepTime)
            continue
        announce = tmpAnnounce.copy()
        while m.send(announce) != 200:
            continue
        time.sleep(__sleepTime)
