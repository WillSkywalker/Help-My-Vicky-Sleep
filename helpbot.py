#!/usr/bin/env python
# Help My Vicky Sleep

import requests
import time
import webbrowser
import urllib2
from bs4 import BeautifulSoup

header_info = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.1581.2 Safari/537.36',
    'Host':'www.zhihu.com',
    'Origin':'http://www.zhihu.com',
    'Referer': 'http://www.zhihu.com/question/20899988',
    'Connection':'keep-alive',
    'Referer':'http://www.zhihu.com/people/Luke-Skywalker',
    'Content-Type':'application/x-www-form-urlencoded',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2,es;q=0.2',
    'Cache-Control':'max-age=0',
    'X-Requested-With': "XMLHttpRequest",
    }

def login_zhihu(s, password):
    r = s.get('http://www.zhihu.com/')
    soup = BeautifulSoup(r.content, "html.parser")
    xsrf = soup.input['value']
    webbrowser.open('http://www.zhihu.com/captcha.gif')
    login_data = {'email': 'cxbats@gmail.com', 'password': password, '_xsrf': xsrf, 'captcha': raw_input('Captcha: ')}
    print s.post('http://www.zhihu.com/login/email', login_data, headers=header_info)

def get_page(s, id_name=None):
    # s = requests.session()
    # login_data = {'email': 'cxbats@gmail.com', 'password': '', }
    # print s.post('http://www.zhihu.com/login', login_data, headers=header_info)

    r = s.get('http://www.zhihu.com/people/'+id_name) if id_name else s.get('http://www.zhihu.com/people/ji-rou-wei-de-e-yu-pi-dai') #s.get('http://www.zhihu.com/people/Luke-Skywalker')
    # print r.content
    soup = BeautifulSoup(r.content, 'html.parser')
    timestamp = soup('span','zm-profile-setion-time zg-gray zg-right')[0].contents[0]
    title = soup('a','question_link')[0].contents[0]
    content = soup('div','zh-summary summary clearfix')[0].get_text(strip=True)
    # fhand = open('example.htm', 'w')
    # fhand.write(r.content)
    # fhand.close
    return (timestamp, title, content)


def main():
    s = requests.session()
    # passwd = raw_input('Password: ')
    # login_zhihu(s, passwd)
    old_page = get_page(s)
    fhand = open('times.txt', 'r+')
    while True:
        new_page = get_page(s)
        if new_page[-1] == old_page[-1]:
            print 'Nothing new...'
        else:
            old_page = new_page
            print 'A new status detected at: [%s]' % time.ctime()
            fhand.write(time.ctime()+'\n'+'\n'.join(new_page)+'\n==================================\n\n\n')
        time.sleep(30)



if __name__ == '__main__':
    main()
    # s = requests.session()
    # login_data = {'email': 'cxbats@gmail.com', 'password': '3026954' }
    # print s.post('http://www.zhihu.com/login/email', login_data, headers=header_info)
    # r = s.get('http://www.zhihu.com/', headers=header_info)
    # # s.get('http://www.zhihu.com/people/ji-rou-wei-de-e-yu-pi-dai') #s.get('http://www.zhihu.com/people/Luke-Skywalker')
    # print r
    # fhand = open('example.htm', 'w')
    # fhand.write(r.content)
    # fhand.close




