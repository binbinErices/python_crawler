# 采用selenium+phantomjs爬取猫眼电影top100的爬虫  

## 相关配置  
运行crawler时，必须要把template.xlsx和phantomjs放在项目目录下。由于代码中已经写死放在当前目录下，读者可以自行修改。  

## 运行截图  
### 抓取结果  
![image1](https://github.com/binbinErices/python_crawler/blob/master/img/content.png?raw=true)  

---
### log模块
![image2](https://github.com/binbinErices/python_crawler/blob/master/img/log.png?raw=true)

## 其他说明  
crawler.py是最开始写的代码，其中只有业务的实现，没有进度条显示，电影评分格式有bug，crawler_.py进行了改进修改了上述的bug.  
