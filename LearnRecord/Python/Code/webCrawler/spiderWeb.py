# coding:utf-8
from bs4 import BeautifulSoup
from bs4 import BeautifulStoneSoup
import urllib.request
import os
import re

# #爬取百度网页html
# # baidu_url = "http://www.kmf.com"
# baidu_url = "http://ke.kmf.com"
# result = urllib.request.urlopen(baidu_url)
# #读取
# html = result .read()
# #解码并打印出来
# print(html.decode('utf-8'))
#
# # url中包含汉字是不符合URL标准的，需要进行编码
# # 编码后：http%3A//www.%E7%88%AC%E8%99%AB.com
# urllib.request.quote('http://www.爬虫.com')
#
# # 解码后：http://www.爬虫.com
# urllib.request.unquote('http%3A//www.%E7%88%AC%E8%99%AB.com')


# def download(title, url):
#
#     req = request.Request(url)
#     response = request.urlopen(req)
#     response = response.read().decode('utf-8')
#     soup = BeautifulSoup(response, 'html.parser')
#     tag = soup.find('div', class_='sm-article-content')
#     if tag == None:
#         return 0
#     title = title.replace(':', '')
#     title = title.replace('"', '')
#     title = title.replace('|', '')
#     title = title.replace('/', '')
#     title = title.replace('\\', '')
#     title = title.replace('*', '')
#     title = title.replace('<', '')
#     title = title.replace('>', '')
#     title = title.replace('?', '')
#
#
#     pwd = os.getcwd()
#     father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
#     text_path = father_path + '/Temp/123.txt'
#     print(father_path)
#
#     with open(father_path + '/Temp/' + title + '.txt', 'w', encoding='utf-8') as file_object:
#         file_object.write('\t\t\t\t')
#         file_object.write(title)
#         file_object.write('\n')
#         file_object.write('该新闻地址：')
#         file_object.write(url)
#         file_object.write('\n')
#         file_object.write(tag.get_text())
#     print('正在爬取')


# def p(args):
#     pass


if __name__ == '__main__':

    for i in range(0, 7):

        url = 'http://www.kmf.com/'
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36", "cookie":"sn=3957284397500558579; _uc_pramas=%7B%22fr%22%3A%22pc%22%7D"}

        res = urllib.request.urlopen(url)
        req = res.read().decode('utf-8')
        soup = BeautifulSoup(req, 'html.parser')
        # print(soup)
        groups = soup.find_all('div', class_='teacher-tips')
        print(groups)

        pwd = os.getcwd()
        father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
        text_path = father_path + '/Temp/spiderWeb.txt'


        with open(text_path, 'w') as file_object:
            file_object.write('\n')

        for tag in groups:
            with open(text_path, 'a') as file_object:
                file_object.write(tag.h2.string)
                file_object.write('      ' + tag.span['title']+'\n\n')
            # print('正在爬取')