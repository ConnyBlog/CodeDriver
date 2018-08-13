import urllib.request
#爬取百度网页html
baidu_url = "http://www.baidu.com"
result = urllib.request.urlopen(baidu_url)
#读取
html = result .read()
#解码并打印出来
print(html.decode('utf-8'))


# url中包含汉字是不符合URL标准的，需要进行编码
# 编码后：http%3A//www.%E7%88%AC%E8%99%AB.com
urllib.request.quote('http://www.爬虫.com') 

# 解码后：http://www.爬虫.com
urllib.request.unquote('http%3A//www.%E7%88%AC%E8%99%AB.com') 