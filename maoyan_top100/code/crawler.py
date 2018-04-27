#!usr/bin/env python  
# -*- coding: UTF-8 -*- 
""" 
@author:binbinzhang
@file: crawler.py 
@time: 2018/04/27 
@email:binbin_Erices@163.com
@function： 爬取猫眼电影top100
@version：1.0.0
"""
import datetime
from selenium import webdriver
from openpyxl import load_workbook


class crawler():

    def __init__(self):
        self.len_count = 2
        service_args = [].append('--load-images=false')  ##关闭图片加载
        self.driver = webdriver.PhantomJS(executable_path="./phantomjs", service_args=service_args)
        self.wb = load_workbook("./template.xlsx")
        self.logs = "[INFO]:"+str(datetime.datetime.now())+" [ADDRESS]:"+" http://maoyan.com/board/4"+"[STATUS]:"+" TREU\n"
        self.title = "猫眼电影Top100"


    def __del__(self):
        with open("log.txt", "a", encoding="utf8") as f:
            f.writelines(self.logs + "\n")
        self.wb.save("./" + self.title + ".xlsx")
        self.driver.quit()
        print("Movies_Crawler is ending...")

    def start(self):
        print("Movies_Crawler is running...")
        movie = self.get_movie()
        for moviehref in movie:
            print("*"*60)
            print(moviehref)
            self.driver.get(moviehref)
            name_z = self.driver.find_element_by_class_name("name").text
            name_e = self.driver.find_element_by_class_name("ellipsis").text
            type = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1][@class="ellipsis"]').text
            time = self.driver.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[1]/ul/li[3][@class="ellipsis"]').text
            score = self.driver.find_element_by_class_name("stonefont").text
            plan = self.driver.find_element_by_class_name("dra").text
            actor = self.driver.find_elements_by_xpath(
                '//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/div/ul/li/div/a')
            actors = ""
            for i in range(len(actor)):
                str = actor[i].text + " "
                actors += str
            image = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/img[@class="avatar"]').get_attribute('src')
            self.savexlsx(name_z,name_e,type,time,score,plan,actors,image)


    def get_movie(self):
        moves = []
        for i in range(10):
            url = "http://maoyan.com/board/4?offset="+str(10*i)
            print(url)
            self.driver.get(url)
            movename = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a')
            for i in range(len(movename)):
                name = movename[i].get_attribute("href")
                print(name)
                moves.append(name)
        return moves




    def savexlsx(self,name_z,name_e,type,time,score,plan,actors,image):
        sheet = self.wb["Sheet1"]
        sheet["A" + str(self.len_count)] = name_z
        sheet["B" + str(self.len_count)] = name_e
        sheet["C" + str(self.len_count)] = type
        sheet["D" + str(self.len_count)] = time
        sheet["E" + str(self.len_count)] = score
        sheet["F" + str(self.len_count)] = plan
        sheet["G" + str(self.len_count)] = actors
        sheet["H" + str(self.len_count)] = image
        self.len_count = self.len_count + 1

if __name__ == "__main__":
    crawler().start()