# beautifulSoup的select方法
```
 1 html = """
 2 <html><head><title>The Dormouse's story</title></head>
 3 <body>
 4 <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
 5 <p class="story">Once upon a time there were three little sisters; and their names were
 6 <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
 7 <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
 8 <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
 9 and they lived at the bottom of a well.</p>
10 <p class="story">...</p>
11 """
 
```
**我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list**

## 1.通过标签名查找
 

*print (soup.select('title') )*

```
[<title>The Dormouse's story</title>]
```

 
*print (soup.select('a'))*

```
[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

print soup.select('b')

```
#[<b>The Dormouse's story</b>]
```


## 2.通过类名查找
 
print soup.select('.sister')

```
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```


## 3.通过 id 名查找

*print (soup.select('#link1'))*

```
[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```


## 4.组合查找

组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开

*print (soup.select('p #link1'))*

```
[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```

**直接子标签查找**

*print (soup.select("head > title"))*

```
[<title>The Dormouse's story</title>]
```


## 5.属性查找

查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。

*print (soup.select('a[href="http://example.com/elsie"]'))*

```
[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```

同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格

*print (soup.select('p a[href="http://example.com/elsie"]'))*

```
[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```

## 源程序

```
#!usr/bin/env python  
# -*- coding: UTF-8 -*- 
""" 
@author:binbinzhang
@file: 1.py 
@time: 2018/04/28 
@email:binbin_Erices@163.com
@function： 
"""

from bs4 import BeautifulSoup

html = """
  <html><head><title>The Dormouse's story</title></head>
 <body>
 <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
 <p class="story">Once upon a time there were three little sisters; and their names were
 <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
 <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
 <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
 and they lived at the bottom of a well.</p>
 <p class="story">...</p>
"""
soup = BeautifulSoup(html,"lxml")

print (soup.select('title'))
print (soup.select('#link2'))
print (soup.select('p #link1'))
print (soup.select("head > title"))
print (soup.select('a[href="http://example.com/elsie"]'))
print (soup.select('p a[href="http://example.com/elsie"]'))
```

```
运行结果：
[<title>The Dormouse's story</title>]
[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
[<title>The Dormouse's story</title>]
[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```

