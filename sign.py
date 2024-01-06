import json

import requests
from lxml import etree

session = requests.Session()
url = "https://forum.butian.net/"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'referer': 'https://forum.butian.net/sign',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
with open('cookies.json', 'r') as cookie_file:
    cookies = json.load(cookie_file)
    session.cookies.update(cookies)
response = session.request("GET", url, headers=headers)

xx = etree.HTML(response.text)
xxx = xx.xpath('/html/head/meta[@name="csrf-token"]/@content')[0]
url = "https://forum.butian.net/sign"
response = session.request("POST", url, headers=headers, data='_token='+xxx)
print(response.text)
