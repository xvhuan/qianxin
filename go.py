import json
import execjs
import requests
from geetest import get_validate

account="11111111111"
password="111111"

headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Cookie': 'next=http%3A//forum.butian.net/btlogin%3FredirectPath%3Dhttps%3A//forum.butian.net/; wzws_sessionid=gjA1NjM4N6Bll33vgTljMWNlMoAyNDA4OjgyMTU6NzIxOToxZTUwOjk1ZDpkYjhlOjhlYzk6ODgzZA==; User-Center=3e7f3775-4f57-46d8-91ec-91adcb46b0bd; User-Center=3e7f3775-4f57-46d8-91ec-91adcb46b0bd',
  'Pragma': 'no-cache',
  'Referer': 'https://user.skyeye.qianxin.com/user/sign-in?next=http://forum.butian.net/btlogin?redirectPath=https://forum.butian.net/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}
def get_pem():
    url = "https://user.skyeye.qianxin.com/api/v1/encrypt/public-key"
    response = requests.request("GET", url, headers=headers)
    return response.json()["public_key"]

yzm = eval(requests.get("https://www.illusory.cn/api/qianxin.php").text)
with open("1.js","r",encoding="utf-8") as f:
    file_data = f.read()
cxk = execjs.compile(file_data)
short = cxk.call("short")

pwd = cxk.call("password",password,short)
key = cxk.call("key_iv",get_pem(),short)
# exit()
url = "https://user.skyeye.qianxin.com/api/v1/sign-in"

payload = json.dumps({
  "account": account,
  "password": pwd,
  "geetest_challenge": yzm[1],
  "geetest_validate": json.loads(yzm[0])["validate"],
  "geetest_seccode": json.loads(yzm[0])["validate"]+"|jordan",
  "next": "http://forum.butian.net/btlogin?redirectPath=https://forum.butian.net/",
  "custom_callback_params": {
    "redirectPath": "https://forum.butian.net/"
  },
  "key_iv": key,
  "csrf_token": "1704457269##ffcf2ba524ba000e09ef4decc5bd632b7720f622"
})
headers = {
  'Accept': 'application/json',
  'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Cookie': 'next=http%3A//forum.butian.net/btlogin%3FredirectPath%3Dhttps%3A//forum.butian.net/; wzws_sessionid=gjA1NjM4N6Bll33vgTljMWNlMoAyNDA4OjgyMTU6NzIxOToxZTUwOjk1ZDpkYjhlOjhlYzk6ODgzZA==; User-Center=3e7f3775-4f57-46d8-91ec-91adcb46b0bd; User-Center=3e7f3775-4f57-46d8-91ec-91adcb46b0bd;csrf_token=1704457269##ffcf2ba524ba000e09ef4decc5bd632b7720f622',
  'Origin': 'https://user.skyeye.qianxin.com',
  'Pragma': 'no-cache',
  'Referer': 'https://user.skyeye.qianxin.com/user/sign-in?next=http://forum.butian.net/btlogin?redirectPath=https://forum.butian.net/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("POST", url, headers=headers, data=payload)
res = response.json()
if res["status"]==200:
  result=requests.get(res["redirect"], headers=headers)
  print(result.cookies)
  with open('cookies.json', 'w') as cookie_file:
    json.dump(result.cookies.get_dict(), cookie_file)

