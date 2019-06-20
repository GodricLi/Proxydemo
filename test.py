# _*_ coding=utf-8 _*_


import requests

# proxy = 'username:password@60.186.9.233'
# proxies = {
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy
# }
# try:
#     res = requests.get('http://httpbin.org/get', proxies=proxies)
#     print(res.text)
# except requests.exceptions.ConnectionError as e:
#     print('error', e.args)


# chrome代理设置
# from selenium import webdriver
#
# proxy = '60.186.9.233'
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=http://' + proxy)
# browser = webdriver.Chrome(chrome_options=chrome_options)
# res = browser.get('http://httpbin.org/get')


# PhantomJs代理设置
from selenium import webdriver

service_args = [
    '--proxy=60.186.9.233',
    '--proxy-type=http',
    '--proxy-auth=username:password'
]
browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')
print(browser.page_source)
