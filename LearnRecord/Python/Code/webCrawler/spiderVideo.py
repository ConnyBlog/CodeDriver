import urllib.request
#视频url,就下载下人人车的广告视频吧（因为它比较小）
video_url = "http://113.113.73.41/r/baiducdngdct.inter.iqiyi.com/videos/other/20180212/07/5c/8747c90718618294a6d122f6b02ee090.f4v"
result = urllib.request.urlopen(video_url)
video = result.read()
#创建视频文件
with open("ad.f4v", "wb") as f:
    #写入二进制数据
    f.write(video)