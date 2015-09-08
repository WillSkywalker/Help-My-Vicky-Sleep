#!/usr/bin/env python
# Help My Vicky Sleep

import requests
import time
import cookielib
import urllib2

global header_info
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
    }

def get_page(url=None):
    s = requests.session()
    # login_data = {'email': 'cxbats@gmail.com', 'password': '3026954', }
    # print s.post('http://www.zhihu.com/login', login_data, headers=header_info)

    r = s.get(url) if url else s.get('http://www.zhihu.com/people/ji-rou-wei-de-e-yu-pi-dai') #s.get('http://www.zhihu.com/people/ji-rou-wei-de-e-yu-pi-dai')
    # print r.content

    return r.content


def main():
    old_page = get_page()
    fhand = open('times.txt', 'r+')
    while True:
        new_page = get_page()
        if new_page == old_page:
            print 'Nothing new...'
        else:
            old_page = new_page
            print 'A new status detected at: [%s]' % time.ctime()
            fhand.write(time.ctime()+'\n')
        time.sleep(30)



if __name__ == '__main__':
    main()




