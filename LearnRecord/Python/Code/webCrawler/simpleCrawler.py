
import urllib.request
import os


# 1、爬一个图片
# picture_url = "https://www.baidu.com/img/bd_logo1.png"
# result = urllib.request.urlopen(picture_url)
# picture = result.read()
#
# pwd = os.getcwd()
# father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
# file_path = father_path + '/Temp/baidu_logo.png'
#
# with open(file_path, "wb") as f:
#     f.write(picture)


# f = open('/Users/michael/test.txt', 'w')
# f.write('Hello, world!')
# f.close()

# try:
#     f = open('/path/to/file', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()


# #当前文件的路径
# pwd = os.getcwd()
# #当前文件的父路径
# father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
# #当前文件的前两级目录
# grader_father=os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
# print(pwd, father_path, grader_father)



# 2、爬一个视频
# video_url = "http://113.113.73.41/r/baiducdngdct.inter.iqiyi.com/videos/other/20180212/07/5c/8747c90718618294a6d122f6b02ee090.f4v"
# result = urllib.request.urlopen(video_url)
# video = result.read()
#
# pwd = os.getcwd()
# father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
# file_path = father_path + '/Temp/ad.f4v'
#
# with open(file_path, "wb") as f:
#     f.write(video)

# 3、爬一个音频
# audio_url = "http://m10.music.126.net/20180302001718/2da3721ebef7f851cf8e39a9ebe30327/ymusic/cd72/f24d/bd25/ccd471214e64e65f541297a7bdf1cd62.mp3"
# result = urllib.request.urlopen(audio_url)
# audio = result.read()
#
# pwd = os.getcwd()
# father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
# file_path = father_path + '/Temp/change_word.mp3'
#
# with open(file_path, "wb") as f:
#     f.write(audio)



