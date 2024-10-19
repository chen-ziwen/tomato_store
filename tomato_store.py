import requests

import json

import requests.cookies

# 读取cookie信息
with open("cookie.json", "r") as f:
    cookies = json.load(f)

# 创建一个 cookieJar对象
cookie_jar = requests.cookies.RequestsCookieJar()

# 将每个Cookie 添加到CookieJar中
for cookie in cookies:
    cookie_jar.set(
        cookie["name"], cookie["value"], domain=cookie["domain"], path=cookie["path"]
    )

# 发送请求
url = "https://kol.fanqieopen.com/api/platform/promotion/plan/create/v:version"

# 拼接url
params = {
    "app_id": 457699,
    "aid": 457699,
    "origin_app_id": 457699,
    "host_app_id": 457699,
    "msToken": "FTyWbjneHIjhzSa4NTMaXavH8mh0ItHNK5j2jOANowUvLosF145mPB_BDizKSohMxyQDlIpBfU3hfIbLreVHCSp6_dWRtHWy_zKbPjjp-9kNP1F1iMGtkQh_bnbWLSWv_zf9FfJMs5aX0RWqknqBJSbUhWUIpJMf",
    "a_bogus": "OJRh%2Ff8DDkdB6dR%2F5lILfY3quL6MYma70cyeMD2Wx6XSS639HMOZ9exEGz71%2Ff6jNT%2FdIeRj74hbTpO2rQAy03fUHWkLldQ2m6WZKleD5xSCs1XJtLhgrUsO5wsUSePdsv1AEcRkqXAezuRDAocJmhxATfoja3igyjkrPVnbZVyziKEMD5A0YzAW",
}

# 请求体参数
json_data = {
    "alias_name": "再次使用虚无之境敌了",
    "alias_type": 1,
    "book_id": "7394772248227220542",
    "metrics_data": {
        "app_id": "457699",
        "app_name": "fanqie_novel",
        "create_entrance": "book_list",
        "genre": "203",
        "is_recommend": "1",
        "sub_page_name": "爆款榜",
    },
}

response = requests.get(url, params=params, json=json_data)
print(response.url)  # 输出完整的 URL，包括查询字符串
print(response)
