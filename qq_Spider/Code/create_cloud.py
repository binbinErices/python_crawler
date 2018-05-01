#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:binbinzhang
@file: create_cloud.py
@time: 2018/04/30 
@email:binbin_Erices@163.com
@version: 1.0.3
@function： 实现生产词云的功能
"""

from os import path
import random
from scipy.misc.pilutil import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

stopwords={}

class Create_word():

    def importStopword(self,filename=''):

        f = open(filename, 'r', encoding='gbk')
        line = f.readline().rstrip()

        while line:
            stopwords.setdefault(line, 0)
            stopwords[line] = 1
            line = f.readline().rstrip()

        f.close()

    def processChinese(self,text):
        seg_generator = jieba.cut(text)  # 使用结巴分词，也可以不使用

        seg_list = [i for i in seg_generator if i not in stopwords]

        seg_list = [i for i in seg_list if i != u' ']

        seg_list = r' '.join(seg_list)

        return seg_list

    def startcloud(self,file = ''):
        print("Wordcloud is running...")
        # img = input("请输入读取的文件名：")
        self.importStopword(filename='./Log/QQZone{}.log'.format(file))
        # self.importStopword(filename=file)

        # 获取当前文件路径
        # __file__ 为当前文件, 在ide中运行此行会报错,可改为
        # d = path.dirname('.')
        d = path.dirname(__file__)

        text = open(path.join(d, './Log/QQZone{}.log'.format(file)), encoding='gbk').read()

        # 如果是中文
        # text = processChinese(text)#中文不好分词，使用Jieba分词进行
        # read the mask / color image
        # taken from http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010

        # 随机设置背景图片
        # random.randint(1, 10)
        back_coloring = imread(path.join(d, "./img/{}.jpg".format(str(random.randint(1, 7)))))
        # back_coloring = imread(path.join(d, "./img/1.jpg"))

        wc = WordCloud(font_path='C:/Windows/Fonts/STZHONGS.TTF',  # 设置字体
                       background_color="black",  # 背景颜色
                       max_words=2000,  # 词云显示的最大词数
                       mask=back_coloring,  # 设置背景图片
                       max_font_size=100,  # 字体最大值
                       random_state=42,
                       )
        # 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
        wc.generate(text)
        # wc.generate_from_frequencies(txt_freq)
        # txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
        # 从背景图片生成颜色值
        image_colors = ImageColorGenerator(back_coloring)

        plt.figure()
        # 以下代码显示图片
        plt.imshow(wc)
        plt.axis("off")

        # 绘制词云
        # plt.show()  #可以选择关闭显示

        # 保存图片
        wc.to_file(path.join(d, "./Pic/{}.png".format(file)))

        print("Create Wordcloud Successful...")


# if __name__ == "__main__":
#     Create_word().startcloud()
