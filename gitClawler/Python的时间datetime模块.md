# Python的时间模块
[TOC]

## datetime模块
datetime模块用于是date和time模块的合集，datetime有两个常量，MAXYEAR和MINYEAR，分别是9999和1.

datetime模块定义了5个类，分别是

1.datetime.date：表示日期的类

2.datetime.datetime：表示日期时间的类

3.datetime.time：表示时间的类

4.datetime.timedelta：表示时间间隔，即两个时间点的间隔

5.datetime.tzinfo：时区的相关信息


#### 1.datetime.date类：

date类有三个参数,datetime.date(year,month,day)，返回year-month-day

方法：

1.datetime.date.ctime(),返回格式如 Sun Apr 16 00:00:00 2017

2.datetime.date.fromtimestamp(timestamp),根据给定的时间戮，返回一个date对象；datetime.date.today()作用相同

3.datetime.date.isocalendar():返回格式如(year，month，day)的元组,(2017, 15, 6)

4.datetime.date.isoformat()：返回格式如YYYY-MM-DD

5.datetime.date.isoweekday()：返回给定日期的星期（0-6），星期一=0，星期日=6

6.datetime.date.replace(year,month,day)：替换给定日期，但不改变原日期

7.datetime.date.strftime(format):把日期时间按照给定的format进行格式化。

8.datetime.date.timetuple()：返回日期对应的time.struct_time对象

time.struct_time(tm_year=2017, tm_mon=4, tm_mday=15, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=105, tm_isdst=-1)

9.datetime.date.weekday()：返回日期的星期




#### 2.datetime的time类

time类有5个参数，datetime.time(hour,minute,second,microsecond,tzoninfo),返回08:29:30

1.datetime.time.replace()

2.datetime.time.strftime(format):按照format格式返回时间

3.datetime.time.tzname()：返回时区名字

4.datetime.time.utcoffset()：返回时区的时间偏移量

 

#### 3.datetime的datetime类

datetime类有很多参数，datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])，返回年月日，时分秒

datetime.datetime.ctime()

datetime.datetime.now().date()：返回当前日期时间的日期部分

datetime.datetime.now().time()：返回当前日期时间的时间部分

datetime.datetime.fromtimestamp()

datetime.datetime.now()：返回当前系统时间

datetime.datetime.replace()

datetime.datetime.strftime()：由日期格式转化为字符串格式
datetime.datetime.now().strftime('%b-%d-%Y %H:%M:%S')
'Apr-26-2018 21:01:35'

datetime.datetime.strptime():由字符串格式转化为日期格式

datetime.datetime.strptime('Apr-26-2018 21:01:35', '%b-%d-%Y %H:%M:%S')
2018-04-26 21:01:35

#### 4.datetime的timedelta类

datetime.datetime.timedelta用于计算两个日期之间的差值，例如：
```
>>> a=datetime.datetime.now()
>>> b=datetime.datetime.now()
>>> a
datetime.datetime(2017, 4, 16, 21, 21, 20, 871000)
>>> b
datetime.datetime(2017, 4, 16, 21, 21, 29, 603000)

>>> b-a
datetime.timedelta(0, 8, 732000)
>>> (b-a).seconds
8

或者

time1 = datetime.datetime(2016, 10, 20)
time2 = datetime.datetime(2015, 11, 2)

"""计算天数差值"""
print(time1-time2).days

"""计算两个日期之间相隔的秒数"""
print (time1-time2).total_seconds()
```

## strftime()和strptime()的使用

strftime()函数是用来格式化一个日期、日期时间和时间的函数，支持date、datetime、time等类，把这些日期、日期时间或时间通过格式字符要求格式为字符串表示。相反strptime()函数就是从字符串表示的日期时间按格式化字符串要求转换为相应的日期时间。

对于time对象来说，格式化字符串不要使用年、月、日相关的字符，因为time对象没有相应的值。如果不幸使用了，只能默认输出为0值。

对于date对象来说，格式化字符串不要使用时、分、秒和微秒相关的字符，因为date对象没有相应的值。如果使用了，只能默认输出为0值
 
由于strftime()函数是调用C语言lib库来实现的，所以在不同平台都支持，具体特定平台支持的细节，需要在平台上查看strftime文档说明。
###常见符号格式

|格式字符 |意义 |例子|注意事项|
|---------|-----|----|--------|
|%a|星期几的英语缩写|Sun, Mon, ..., Sat(en_US); So, Mo, ..., Sa(de_DE)| |
|%A|星期几的英语全称|Sunday, Monday, ..., Saturday(en_US)| |
|%w|星期几采用数字表示，0表示星期日，6表示星期六|0，1，...，6| |
|%d|用0补充的两位日期数字 |01，02，...，31| |
|%b|月份采用缩写字符表示 |Jan, Feb,..., Dec(en_US) |  |
|%B|月份采用全名称表示|January, February, ...,December(en_US)| |
|%m|月份采用0补充的两位数表示|01，02，...，12 | |
|%y|年份采用0补充的两位数表示|00，01，...，99| |
|%Y|采用四位数表示的年份|0001，0002，...，2013，2014，2015，...，9998，9999| |
|%I|以0补充的12小时表示的小时|00，01，...，12| |
|%p|本地时间是上午还是下午|AM，PM(en_US)| |
|%M|以0补充的分钟表示|00，01，...，59| |
|%S|以0补充的秒表示|00，01，...，59| |
|%f|以0补充的微秒表示|000000，000001，...，999999| |
|%z|UTC偏移表示为+HHMM或-HHMM|(empty)，+0000,-0400,+1030| |
|%Z|时区名称|(empty)，UTC，EST，CST| |
|%j|以0补充的年的天数|001，002，...，366| |
|%U|一年里第几周，星期日作为一周开始|00，01，...，53| |
|%W|一年里第几周，星期一作为一周开始|00，01，...，53| |
|%c|采用本地合适日期和时间表示|Tue Aug 16 21:30:00 1988(en_US)| |
|%x|采用本地合适日期表示|08/16/88(None);08/16/1988(en_US)| |
|%%|输出百分号%|%| |

## 代码实例

```
#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:binbinzhang
@file: time.py
@time: 2018/04/26 
@email:binbin_Erices@163.com
@function：python中的时间处理模块
"""

import datetime
# 获取当前时间
d1 = datetime.datetime.now()
print (d1)
# 当前时间加上半小时
d2 = d1 + datetime.timedelta(hours=8)
print (d2)
# 格式化字符串输出
d3 = d2.strftime('%Y-%m-%d %H:%M:%S')
print (d3)
# 将字符串转化为时间类型
date = str("30 Apr 18")
d4 = datetime.datetime.strptime(date,'%d %b %y')
print (d4)
'''
2018-04-26 20:25:06.238218
2018-04-27 04:25:06.238218
2018-04-27 04:25:06
2018-04-30 00:00:00
'''

def first_day_of_month():
  '''
  获取本月第一天
  :return:
  '''
  return datetime.date.today() - datetime.timedelta(days=datetime.datetime.now().day - 1)
def first_day_of_week():
  '''
  获取本周第一天
  :return:
  '''
  return datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday())
if __name__ == "__main__":
  this_week = first_day_of_week()
  last_week = this_week - datetime.timedelta(days=7)
  this_month = first_day_of_month()
  last_month = this_month - datetime.timedelta(days=(this_month - datetime.timedelta(days=1)).day)
  print (this_week)
  print (last_week)
  print (this_month)
  print (last_month)
  """
  datetime的功能强大
  能支持0001年到9999年
  """
  """
  当前时间
  返回的是一个datetime类型
  now方法有个参数tz，设置时区类型。如果没有和方法today的效果一样
  """
  now = datetime.datetime.now()
  # UTC时间
  datetime.datetime.utcnow()
  attrs = [
      ("year", "年"), ('month', "月"), ("day", "日"), ('hour', "小时"), ('minute', "分"), ('second', "秒"),
      ('microsecond', "毫秒"), (
          'min', "最小"), ('max', "最大"),
  ]
  for k, v in attrs:
      "now.%s = %s #%s" % (k, getattr(now, k), v)

  # 返回一个time结构
  now.timetuple()

  # 返回一个date类型
  now.date()

  # 返回一个time类型
  now.time()

  # 当前星期几。星期一是0，星期于是6,这里是方法不是属性
  now.weekday()

  # 当前星期几。星期一是1，星期于是7 这里是方法不是属性
  now.isoweekday()
 
  # 修改当前时间。比如修改成当月1号
  now.replace(day=1)
  past = datetime.datetime(2010, 11, 12, 13, 14, 15, 16)
  
  # 进行比较运算
  # 返回的是timedelta类型
  now - past


```

