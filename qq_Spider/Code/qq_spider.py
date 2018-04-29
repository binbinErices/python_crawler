#!usr/bin/env python  
# -*- coding: UTF-8 -*- 
""" 
@author:binbinzhang
@file: qq_spider.py 
@time: 2018/04/29 
@email:binbin_Erices@163.com
@function： 进行QQ空间动态爬取
"""

# coding:utf-8
import time
from selenium import webdriver
from lxml import etree
import xlwt



# 这里一定要设置编码格式，防止后面写入文件时报错


class crawler():

    def __init__(self):
        self.friend = ''  # 朋友的QQ号，朋友的空间要求允许你能访问
        self.user = 'acount'  # 你的QQ号
        self.pw = 'Password'  # 你的QQ密码

        self.__count = 1
        self.__createSheet()
        service_args = [].append('--load-images=false')  ##关闭图片加载
        self.driver = webdriver.PhantomJS(executable_path="./phantomjs", service_args=service_args)
        # 浏览器窗口最大化
        self.driver.maximize_window()

    def __del__(self):
        self.driver.close()
        print("QQ_Crawler is ending...")


    def __createSheet(self):
        # 创建工作簿
        self.__f = xlwt.Workbook()
        self.__sheet = self.__f.add_sheet("QQZone", cell_overwrite_ok=True)
        rowTitle = ['Number','Name', 'Time', 'Content']
        for i in range(0, len(rowTitle)):
            self.__sheet.write(0, i, rowTitle[i])

    # 保存数据到excel中
    def __saveDataToExcel(self, Name, Time, Content):
        jobs = []
        jobs.append(self.__count)
        jobs.append(Name)
        jobs.append(Time)
        jobs.append(Content)

        for j in range(0, len(jobs)):
            self.__sheet.write(self.__count, j, jobs[j])
        self.__f.save('QQZone'+self.friend+'.xls')
        self.__count += 1

    def getData(self):
        # 浏览器地址定向为qq登陆页面
        self.driver.get("http://i.qq.com")

        # 所以这里需要选中一下frame，否则找不到下面需要的网页元素
        self.driver.switch_to.frame("login_frame")

        # 自动点击账号登陆方式
        self.driver.find_element_by_id("switcher_plogin").click()

        # 账号输入框输入已知qq账号
        self.driver.find_element_by_id("u").send_keys(self.user)

        # 密码框输入已知密码
        self.driver.find_element_by_id("p").send_keys(self.pw)

        # 自动点击登陆按钮
        self.driver.find_element_by_id("login_button").click()
        time.sleep(4)

        # 让webdriver操纵当前页
        self.driver.switch_to.default_content()

        # 跳到说说的url, friend你可以任意改成你想访问的空间
        self.driver.get("http://user.qzone.qq.com/{}/311".format(self.friend))

        next_num = 0  # 初始“下一页”的id
        while True:

            # 下拉滚动条，使浏览器加载出动态加载的内容，
            # 我这里是从1开始到6结束 分5 次加载完每页数据
            for i in range(1, 6):
                height = 20000 * i  # 每次滑动20000像素
                # scroIIBy9() 把内容滚动到指定的像素数
                # str() 将变量转化为字符串类型
                strWord = "window.scrollBy(0," + str(height) + ")"
                # 选定加载位置
                self.driver.execute_script(strWord)
                time.sleep(4)

            # 很多时候网页由多个<frame>或<iframe>组成，webdriver默认定位的是最外层的frame，
            # 所以这里需要选中一下说说所在的frame，否则找不到下面需要的网页元素
            self.driver.switch_to.frame("app_canvas_frame")
            selector = etree.HTML(self.driver.page_source)
            divs = selector.xpath('//*[@id="msgList"]/li/div[3]')

            # 这里使用 a 表示内容可以连续不清空写入
            with open('QQZone'+self.friend+'.log', 'a') as f:
                for div in divs:
                    qq_name = div.xpath('./div[2]/a/text()')
                    qq_content = div.xpath('./div[2]/pre/text()')
                    qq_time = div.xpath('./div[4]/div[1]/span/a/text()')

                    qq_name = ''.join(qq_name).encode('gbk', 'ignore').decode('gbk')
                    qq_content = ''.join(qq_content).encode('gbk', 'ignore').decode('gbk')
                    qq_time = ''.join(qq_time).encode('gbk', 'ignore').decode('gbk')

                    print(qq_name, qq_time, qq_content)
                    self.__saveDataToExcel(qq_name,qq_time,qq_content)
                    f.write(qq_content + "\n")

                    # 当已经到了尾页，“下一页”这个按钮就没有id了，可以结束了
            if self.driver.page_source.find('pager_next_' + str(next_num)) == -1:
                break

                # 找到“下一页”的按钮，因为下一页的按钮是动态变化的，这里需要动态记录一下
            self.driver.find_element_by_id('pager_next_' + str(next_num)).click()

            # “下一页”的id
            next_num += 1
            time.sleep(1)

            # 因为在下一个循环里首先还要把页面下拉，所以要跳到外层的frame上
            self.driver.switch_to.default_content()

    #程序启动入口
    def start(self):

        print("QQ_Crawler is running...")
        #需要抓取的qq
        qq = input('请输入需要抓取的QQ：')
        self.friend = str(qq)

        self.getData()


if __name__ == "__main__":
    crawler().start()
