# 采用selenium+phantomjs爬取猫眼电影top100的爬虫  

```
@author:binbinzhang
@time: 2018/04/27 
@email:binbin_Erices@163.com
@CSDN:https://blog.csdn.net/Erice_s

```

## 相关配置  
### 项目文件配置  
运行crawler时，必须要把template.xlsx和phantomjs放在项目目录下。由于代码中已经写死放在当前目录下，读者可以自行修改。  

---

### template.xlsx配置  
|电影中文名称(Move)|电影英文名称(Move)|类型(TYPE)|上映时间(TIME)|评分(score)|剧情(play)|主演(Actor)|电影封面(Image)|  
|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|  
|   |   |   |  |  |  |  |   |  


---

#### 抓取结果  
|电影中文名称(Move)|电影英文名称(Move)|类型(TYPE)|上映时间(TIME)|评分(score)|剧情(play)|主演(Actor)|电影封面(Image)|  
|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|  
|霸王别姬 |	Farewell My Concubine|	爱情,剧情	|content 具体内容|	陈凯歌 张国荣 张丰毅 巩俐 吕齐 |	http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@464w_644h_1e_1c|  



## 运行截图  
### 抓取结果  
![image1](https://github.com/binbinErices/python_crawler/blob/master/img/content.png?raw=true)  

---
### log模块
![image2](https://github.com/binbinErices/python_crawler/blob/master/img/log.png?raw=true)

## 其他说明  
crawler.py是最开始写的代码，其中只有业务的实现，没有进度条显示，电影评分格式有bug，crawler_.py进行了改进修改了上述的bug.  
