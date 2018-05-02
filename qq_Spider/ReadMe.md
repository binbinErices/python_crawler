# 基于selenium抓取空间好友动态并生成词云  

## 运行结果  

![好友词云图1](https://github.com/binbinErices/python_crawler/blob/master/img/qq_spider3.png?raw=true)  

---
 
![好友词云图2](https://github.com/binbinErices/python_crawler/blob/master/img/qq_spider4.png?raw=true)  

| Tables  | Are | Cool  |	
| - |:-:| -:|	
| col 3 is      | right-aligned | $1600 |	
| col 2 is      | centered      |   $12 |	
| zebra stripes | are neat      |    $1 |


## 相关配置PyCharm+Anaconda  

### 需要配置Anaconda   

Anaconda 是一个可用于科学计算的 Python 发行版，支持 Linux、Mac、Windows系统，内置了常用的科学计算包。它解决了官方 Python 的两大痛点。  

1. 第一：提供了包管理功能，Windows 平台安装第三方包经常失败的场景得以解决。 
2. 第二：提供环境管理的功能，功能类似 Virtualenv，解决了多版本Python并存、切换的问题。  

**下载 Anaconda** 
直接在[官网下载](https://www.anaconda.com/download/)安装包， 选择 Python3.6 的安装包进行下载，下载完成后直接安装，安装过程选择默认配置即可，大约需要2G多的磁盘空间。  

**镜像源配置** 
Anaconda安装成功之后，我们需要修改其包管理镜像为国内源。  

[Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)  

简单来说就是在cmd中分别运行这两个命令就好了。  
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/  
conda config --set show_channel_urls yes  
```

在 Windows 上，会随 Anaconda 一起安装一批应用程序：  

Anaconda Navigator，它是用于管理环境和包的 GUI  
Anaconda Prompt 终端，它可让你使用命令行界面来管理环境和包  
Spyder，它是面向科学开发的 IDE  

为了避免报错，我推荐在默认环境下更新所有的包。打开 Anaconda Prompt （或者 Mac 下的终端），键入：  
> conda upgrade --all  


**conda 工具介绍**  
conda 是 Anaconda 下用于包管理和环境管理的工具，功能上类似 pip 和 vitualenv 的组合。安装成功后 conda 会默认加入到环境变量中，因此可直接在命令行窗口运行命令 conda  

conda 的环境管理与 virtualenv 是基本上是类似的操作。  

```
# 查看帮助
conda -h 
# 基于python3.6版本创建一个名字为python36的环境
conda create --name python36 python=3.6 
# 激活此环境
activate python36  
source activate python36 # linux/mac
# 再来检查python版本，显示是 3.6
python -V  
# 退出当前环境
deactivate python36 
# 删除该环境
conda remove -n python36 --all
# 或者 
conda env remove  -n python36

# 查看所以安装的环境
conda info -e
python36              *  D:\Programs\Anaconda3\envs\python36
root                     D:\Programs\Anaconda3
```

conda 的包管理功能可 pip 是一样的，当然你选择 pip 来安装包也是没问题的。

```
# 安装 matplotlib 
conda install matplotlib
# 查看已安装的包
conda list 
# 包更新
conda update matplotlib
# 删除包
conda remove matplotlib

```

在 conda 中 **anything is a package**。conda 本身可以看作是一个包，python 环境可以看作是一个包，anaconda 也可以看作是一个包，因此除了普通的第三方包支持更新之外，这3个包也支持。比如：  

```
# 更新conda本身
conda update conda
# 更新anaconda 应用
conda update anaconda
# 更新python，假设当前python环境是3.6.1，而最新版本是3.6.2，那么就会升级到3.6.2
conda update python

```

如果使用conda安装包的时候还是很慢，那么可以考虑使用pip来安装，同样把 pip 的镜像源地址也改成国内的，豆瓣源速度比较快。修改 ~/.pip/pip.conf (Linux/Mac) 或 C:\Users\当前用户名\pip\pip.ini (Windows) 配置：  

```
[global]
trusted-host =  pypi.douban.com
index-url = http://pypi.douban.com/simple
```
**Anacanda其他相关问题**   
[深入浅出Anacanda安装后的配置](https://blog.csdn.net/erice_s/article/details/80156334)    
[Anaconda找包，安装包时，遇到PackageNotFoundError： ''Package missing in current channels"](https://blog.csdn.net/erice_s/article/details/80156191)  
[python scipy安装失败的解决方法](https://blog.csdn.net/erice_s/article/details/80151977)  

### 运行环境配置
![env_setting](https://github.com/binbinErices/python_crawler/blob/master/img/qq_spider2.png?raw=true)  

**selenium建议使用2.X版本  3.X版本会有warning**  

```
 UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
 warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '
```

### 文件目录配置  

在项目文件中需要有Excel,Log,Pic,img文件夹  

|文件夹名称|作用|备注|  
|--------|-----|---|  
|Excel|存放生产的xls文件| |  
|Log|存放空间动态的文件| |  
|Pic|存放生产的词云图| |  
|img|存放用来生产词云图的背景图| |  

![本机文件结构图](https://github.com/binbinErices/python_crawler/blob/master/img/qq_spider1.png?raw=true)  
![本机文件结构图](https://github.com/binbinErices/python_crawler/blob/master/img/qq_spider5.png?raw=true)  

**因为使用无界面浏览器所以需要把phantomjs放入到项目目录下**  


