#!usr/bin/env python  
# -*- coding: UTF-8 -*- 
""" 
@author:binbinzhang
@file: crawler_.py.py 
@time: 2018/04/27 
@email:binbin_Erices@163.com
@function：
@version：1.0.1
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
        self.infologs = []
        self.score = self.get_score() #定义电影评分list


    def __del__(self):
        with open("log.txt", "a", encoding="utf8") as f:
            f.writelines(self.logs + "\n")
            f.writelines(self.infologs)
        self.wb.save("./" + self.title + ".xlsx")
        self.driver.quit()
        print("Movies_Crawler is ending...")

    def start(self):
        print("Movies_Crawler is running...")
        movie = self.get_movie()
        count = 0
        for moviehref in movie:
            count += 1
            print('\n'+"*"*60)
            print(moviehref)
            info = str(datetime.datetime.now())+"\t"
            info += moviehref
            self.driver.get(moviehref)
            name_z = self.driver.find_element_by_class_name("name").text
            name_e = self.driver.find_element_by_class_name("ellipsis").text
            type = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1][@class="ellipsis"]').text
            time = self.driver.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[1]/ul/li[3][@class="ellipsis"]').text
            score = self.score[count-1]
            plan = self.driver.find_element_by_class_name("dra").text
            actor = self.driver.find_elements_by_xpath(
                '//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/div/ul/li/div/a')
            actors = ""
            for i in range(len(actor)):
                tempstr = actor[i].text + " "
                actors += tempstr
            image = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/img[@class="avatar"]').get_attribute('src')
            print("爬取总进度:{}%    ".format(round((count/100)*100, 2))+"="*int(40*count/100)) #设置完成加载为40*=
            info += "\t\t爬取总进度:{}%\t\t".format(round((count/100)*100, 2))+"="*int(40*count/100)
            self.infologs.append(info + '\n')
            self.savexlsx(name_z,name_e,type,time,score,plan,actors,image)


    def get_movie(self):
        moves = []
        count = 0
        for i in range(10):
            url = "http://maoyan.com/board/4?offset="+str(10*i)
            info = str(datetime.datetime.now())+"\t"
            info += url
            print(url)
            self.driver.get(url)
            movename = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a')
            for i in range(len(movename)):
                name = movename[i].get_attribute("href")
                print(name)
                moves.append(name)
                count += 1
                print("影片url装载进度:{}%\t\t".format(round((count / 100) * 100, 2))+"="*int(40*count/100))
                info += "\t影片url装载进度:{}%\t\t".format(round((count / 100) * 100, 2))+"="*int(40*count/100)
                self.infologs.append(info+'\n')
                info = str(datetime.datetime.now())+"\t"+url
        return moves

    def get_score(self):
        scores = []
        for i in range(10):
            url = "http://maoyan.com/board/4?offset=" + str(10 * i)
            self.driver.get(url)
            for j in range(10):
                p1 = '//*[@id="app"]/div/div/div[1]/dl/dd['+str(j+1)+']/div/div/div[2]/p/i[1]'
                p2 = '//*[@id="app"]/div/div/div[1]/dl/dd['+str(j+1)+']/div/div/div[2]/p/i[2]'
                score = self.driver.find_element_by_xpath(p1).text+self.driver.find_element_by_xpath(p2).text
                scores.append(score)
        return scores

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