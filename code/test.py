#!usr/bin/env python  
# -*- coding: UTF-8 -*- 
""" 
@author:binbinzhang
@file: test.py 
@time: 2018/04/27 
@email:binbin_Erices@163.com
@function：测试使用webdriver拿网页数据
"""

import datetime
from selenium import webdriver
from openpyxl import load_workbook

service_args = [].append('--load-images=false')  ##关闭图片加载
driver = webdriver.PhantomJS(executable_path="./phantomjs", service_args=service_args)
driver.get('http://maoyan.com/films/246433')

# text2 = driver.find_element_by_class_name("dra").text
# print(text2)

# actor = driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/div/ul/li/div/a')
# actors =""
# for i in range(len(actor)):
#      str = actor[i].text +" "
#      actors += str
#      print(actors)
# print(actors)

str = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/img[@class="avatar"]').get_attribute('src')
print(str)


