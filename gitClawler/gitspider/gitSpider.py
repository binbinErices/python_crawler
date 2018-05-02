#!usr/bin/env python  
# -*- coding: UTF-8 -*- 
""" 
@author:binbinzhang
@file: gitSpider.py 
@time: 2018/04/27 
@email:binbin_Erices@163.com
@function： 输入起始日期，输入爬取天数，自动爬取GitHub代码提交量
python -m pip install --upgrade pip==9.0.3 更换pip版本
"""
import datetime

from openpyxl import load_workbook
from selenium import webdriver


class crawler:
    def __init__(self):
        print("GitHub_Crawler is running...")
        # self.day_time = (datetime.datetime.now() - datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0)
        self.day_time = self.get_date()
        self.end_day = input("请输入需要采集的天数：")
        self.len_count = 2
        service_args = [].append('--load-images=false')  ##关闭图片加载
        self.driver = webdriver.PhantomJS(executable_path="./phantomjs", service_args=service_args)
        self.wb = load_workbook("./template.xlsx")
        self.err_num = 0
        self.errstr = '[INFO]：' + datetime.datetime.now().strftime("%Y/%m/%d  %H:%M:%S") + "  [ADDRESS]：目标基站https://github.com/BithumbCoin" + "  启动日志\n"
        self.name_list = self.load_name_list()

    def __del__(self):
        with open("err_log.txt", "a", encoding="utf8") as f:
            f.writelines(self.errstr + "\n")
        end_time = self.day_time + datetime.timedelta(int(self.end_day)-1)
        self.wb.save("./Excel/" + self.day_time.strftime('%Y-%m-%d')+"_"+end_time.strftime('%m-%d')+"_ulord"+".xlsx")
        self.driver.quit()
        print("GitHub_Crawler is ending...")


    def start(self):
        print("正在抓取 " + str(self.day_time.day) + "日 的提交记录")
        self.driver.get("https://github.com/UlordChain?tab=repositories")
        times = self.driver.find_elements_by_xpath('//*[@id="org-repositories"]/div[1]/div/li/div/relative-time')
        names = self.driver.find_elements_by_xpath('//*[@id="org-repositories"]/div[1]/div/li/div/h3/a')
        project_names = []
        print("\n获得已更新项目列表： ")
        for i in range(len(times)):
            time = times[i].get_attribute("datetime")
            time = self.formate_time(time)
            if time < self.day_time:
                break
            name = names[i].text
            project_names.append(name)
            print(name)
        print("\n开始顺序爬取：")
        for i, project_name in enumerate(project_names):
            print("开始爬取项目  " + project_name)
            self.do_project(project_name)
            #round函数 返回浮点数x的四舍五入值
            print("\n*** 总进度：" + str(round(((i + 1) / len(project_names))*100, 2)) + "%  ***\n\n")

    def do_project(self, project_name):
        branchs = self.get_branchs(project_name)
        commits = []
        all_commits = 0
        for branch in branchs:
            print("开始爬取 {} 分支提交记录".format(branch))
            commits = self.get_commit(project_name, branch)
            all_commits += len(commits)
            i = 0
            for commit in commits:
                i = i + 1
                self.do_commit(project_name, commit, branch)
                print("\r完成 {} {} 进度 {} %".format(project_name, branch, str(round(i / len(commits) * 100, 2))), end="")
        print("该项目总共 {} 次提交".format(str(all_commits)))

    def get_commit(self, project_name, branch):
        flag = False
        commits = []
        url = "https://github.com/UlordChain/" + project_name + "/commits/" + branch
        self.driver.get(url)
        while True:
            # names实际上取得是commit的描述字段
            # names = self.driver.find_elements_by_xpath(
            #     '//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/ol/li/div[1]/p/a[1]')
            names = self.driver.find_elements_by_xpath(
                '//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/ol/li/div[1]/p/a[1]')
            times = self.driver.find_elements_by_xpath(
                '//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/ol/li/div[1]/div/div[2]/relative-time')
            for i in range(len(times)):
                time = times[i].get_attribute("datetime")
                time = self.formate_time(time)
                if time < self.day_time:
                    flag = True
                    break
                days = int(self.end_day)
                if time > self.day_time + datetime.timedelta(days=days):
                    continue
                name = names[i].get_attribute("href")
                commits.append(name)
            if flag:
                break
            try:
                c = self.driver.find_element_by_xpath(
                    '//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[3]/div/a[2]')
                c.click()
            except:
                break
        return commits

    def do_commit(self, project_name, commit, branch):
        self.driver.get(commit)
        try:
            try:
                name = self.driver.find_element_by_xpath(
                    '//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[1]/div/div[2]/a')
            except Exception as err:
                name = self.driver.find_element_by_xpath(
                    '//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[1]/div/div[2]/span')
            name = name.text
            theme = self.driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[1]/p').text
            content = self.driver.find_element_by_xpath('//*[@id="toc"]/div[2]').text
            data = self.driver.find_element_by_xpath(
                '//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[1]/div/div[2]/relative-time')
            data = data.get_attribute("datetime")
            data = self.formate_time(data).strftime('%Y-%m-%d %H:%M')
            self.save(name, project_name, branch, theme, content, data)
        except TypeError as err:
            print("发现一个异常数据")
            self.err_num += 1
            self.errstr += "图片序号：" + str(self.err_num) + "  " + commit + "\n"
            self.driver.save_screenshot("err_log_image_" + str(self.err_num) + ".png")

    def save(self, name, project, branch, theme, content, data):
        sheet = self.wb["Sheet"]
        sheet["A" + str(self.len_count)] = data
        sheet["B" + str(self.len_count)] = self.name_list.get(name)
        sheet["C" + str(self.len_count)] = name
        sheet["D" + str(self.len_count)] = project
        sheet["E" + str(self.len_count)] = branch
        sheet["F" + str(self.len_count)] = theme
        sheet["G" + str(self.len_count)] = content
        self.len_count = self.len_count + 1

    def load_name_list(self):
        with open("./name_list.txt", "r", encoding="utf8") as f:
            data = f.readlines()
            res = {}
            for i in "".join(data).split("\n"):
                if i:
                    c_name, e_name = i.split("    ")
                    if c_name and e_name:
                        res[e_name] = c_name
                    else:
                        raise Exception("name_list.txt 有名字错误 英文：" + e_name + " 中文：" + c_name)
        print("名单文件载入成功")
        return res

    def formate_time(self, data):
        return datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%SZ') + datetime.timedelta(hours=8)

    def get_branchs(self, project_name):
        self.driver.get("https://github.com/UlordChain/" + project_name + "/branches")
        x = self.driver.find_elements_by_xpath(
            '//*[@id="branch-autoload-container"]/div/div/div/span[1]/a')
        res = []
        for i in range(len(x)):
            print(" 找到分支: " + x[i].text)
            txt = x[i].text

            res.append(txt)
        return res

    def get_date(self):
        x = datetime.datetime.now()
        day = str(input("输入需要爬取的日期2018-05-01：\n"))
        day = datetime.datetime.strptime(day,"%Y-%m-%d")
        if day > x:
            return x
        return day


if __name__ == '__main__':
    print(" *********************************************************************************")
    print(" *                                                                               *")
    print(" *                                                                               *")
    print(" *                      欢迎使用GitHub爬虫工具                                   *")
    print(" *                                                                               *")
    print(" *                                                                               *")
    print(" *********************************************************************************\n")
    crawler().start()
    # print(crawler().do_project("CrossChain"))
    # print(crawler().get_commit("CrossChain", "develop"))
    input("请按Enter结束爬取...")

