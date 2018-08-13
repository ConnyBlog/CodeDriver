
import urllib.request
#图片url，我们百度首页logo下载下来
picture_url = "https://www.baidu.com/img/bd_logo1.png"
result = urllib.request.urlopen(picture_url)
picture = result.read()
#创建图片文件
with open("baidu_logo.png", "wb") as f:
    #写入二进制数据
    f.write(picture)



# import urllib.request
# #歌曲url，我们就下载一首王力宏的改变世界吧
# audio_url = "http://m10.music.126.net/20180302001718/2da3721ebef7f851cf8e39a9ebe30327/ymusic/cd72/f24d/bd25/ccd471214e64e65f541297a7bdf1cd62.mp3"
# result = urllib.request.urlopen(audio_url)
# audio = result.read()
# #创建mp3文件
# with open("change_word.mp3", "wb") as f:
#     #写入二进制数据
#     f.write(audio)