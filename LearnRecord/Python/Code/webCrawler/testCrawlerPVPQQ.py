# -*- coding: utf-8 -*-

import urllib.request
import json
import os

response = urllib.request.urlopen("http://pvp.qq.com/web201605/js/herolist.json")

hero_json = json.loads(response.read())
hero_num = len(hero_json)


# print(hero_json)
# print("hero_num : " , str(hero_num))


# # 打印部分数据
# hero_name = hero_json[0]['cname']
# skin_names = hero_json[0]['skin_name'].split('|')
# skin_num = len(skin_names)
#
# print('hero_name: ', hero_name)
# print('skin_names :', skin_names)
# print('skin_num: ' + str(skin_num))


# 文件保存
pwd = os.getcwd()
father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
save_dir = father_path + '/Temp/'

if not os.path.exists(save_dir):
    os.mkdir(save_dir)

for i in range(hero_num):
    # 获取英雄皮肤列表
    skin_names = hero_json[i]['skin_name'].split('|')

    for cnt in range(len(skin_names)):
        save_file_name = save_dir + str(hero_json[i]['ename']) + '-' +hero_json[i]['cname']+ '-' +skin_names[cnt] + '.jpg'
        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(hero_json[i]['ename'])+ '/' +str(hero_json[i]['ename'])+'-bigskin-' + str(cnt+1) +'.jpg'

        if not os.path.exists(save_file_name):
            urllib.request.urlretrieve(skin_url, save_file_name)