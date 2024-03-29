# -*- coding: utf8 -*-

"""
cron: 30 5,8,12,15,18 * * *
new Env('福利吧签到');
"""

import requests
import re
import os, sys
from sendNotify import send


def start(cookie, username):
    try:
        s = requests.session()
        # 永久地址已可正常访问
        temp_addr = "https://www.wnflb2023.com/"
        if s.get(temp_addr).status_code == 200:
            flb_url = "www.wnflb2023.com"
        else:
        # 使用永久地址获取到的论坛地址
            flb_url = get_addr()
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'Accept - Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'cache-control': 'max-age=0',
                   'Upgrade-Insecure-Requests': '1',
                   'Host': flb_url,
                   'Cookie': cookie,
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'}

        # 访问Pc主页
        print(flb_url)
        user_info = s.get('https://' + flb_url + '/forum.php?mobile=no', headers=headers).text
        user_name = re.search(r'title="访问我的空间">(.*?)</a>', user_info)
        if user_name:
            print("登录用户名为：" + user_name.group(1))
            print("环境用户名为：" + username)
        else:
            print("未获取到用户名")
        if user_name is None or (user_name.group(1) != username):
            raise Exception("【福利吧】cookie失效???????")
        # 获取签到链接,并签到
        qiandao_url = re.search(r'}function fx_checkin(.*?);', user_info).group(1)
        qiandao_url = qiandao_url[47:-2]
        print(qiandao_url)
        # 签到
        s.get('https://' + flb_url + '/' + qiandao_url, headers=headers).text

        # 获取积分
        user_info = s.get('https://' + flb_url + '/forum.php?mobile=no', headers=headers).text

        current_money = re.search(r'<a.*? id="extcreditmenu".*?>(.*?)</a>', user_info).group(1)
        sing_day = re.search(r'<div class="tip_c">(.*?)</div>', user_info).group(1)
        log_info = "{}当前{}".format(sing_day, current_money)
        print(log_info)
        send("签到结果", log_info)

    except Exception as e:
        print("签到失败，失败原因:"+str(e))
        send("签到结果", str(e))


def get_addr():
    pub_page = "http://fuliba2023-1256179406.file.myqcloud.com/"
    ret = requests.get(pub_page)
    ret.encoding = "utf-8"
    bbs_addr = re.findall(r'<a href=.*?><i>https://(.*?)</i></a>', ret.text)[1]
    return bbs_addr


if __name__ == '__main__':
    # cookie = "cookie"
    # user_name = "username"
    cookie = os.getenv("FUBA")
    user_name = os.getenv("FUBAUN")
    start(cookie, user_name)
