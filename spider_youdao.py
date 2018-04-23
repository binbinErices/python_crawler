#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:binbinzhang
@file: spider_youdao.py 
@time: 2018/04/23 
@email:binbin_Erices@163.com
@func: 利用爬虫实现接入有道翻译
"""

"""

MIT License

Copyright (c) 2018 binbinzhang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""




#使用urllib库
# from urllib import request
# from urllib import parse
# import json
#
# def Translate():
#     #对应上图的Request URL
#     #Request_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'  ##这里面不能加_o 否则得不到结果
#     Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#
#     vocabulary = input('Please Enter finded things:')
#     if(len(vocabulary)==0):
#         print("你输入的内容为空，请重新输入")
#     if(vocabulary =="q!"):
#         print("exit...")
#         exit()
#     if len(vocabulary) != 0:
#         # 创建Form_Data字典，存储上图的Form Data
#         Form_Data = {}
#         Form_Data['i'] = vocabulary
#         Form_Data['from'] = 'AUTO'
#         Form_Data['to'] = 'AUTO'
#         Form_Data['smaetresult'] = 'dict'
#         Form_Data['client'] = 'fanyideskweb'
#         Form_Data['salt'] = '1521187067166'
#         Form_Data['sign'] = '46541121b8a322c66455ba313c67ae08'
#         Form_Data['doctype'] = 'json'
#         Form_Data['version'] = '2.1'
#         Form_Data['keyfrom'] = 'fanyi.web'
#         Form_Data['action'] = 'FY_BY_REALTIME'
#         Form_Data['typoResult'] = 'false'
#
#         # encode是将Unicode的编码转换成utf-8编码h
#         # 使用urlencode方法转换标准格式
#         data = parse.urlencode(Form_Data).encode('utf-8')
#         # 传递Request对象和转换完格式的数据
#         response = request.urlopen(Request_URL, data)
#         html = response.read().decode('utf-8')
#         # 使用JSON loads反序列化为Python可以解析的dict list
#         translate_results = json.loads(html)
#         # 找到翻译结果
#         translate_results = translate_results["translateResult"][0][0]['tgt']   #{'type': 'EN2ZH_CN', 'errorCode': 0, 'elapsedTime': 0, 'translateResult': [[{'src': 'i love python', 'tgt': '我喜欢python'}]]}
#         # 打印翻译信息
#
#         print("翻译的结果是：%s" % translate_results)
#
# def main():
#     Translate();
#
#
# if __name__ == "__main__":
#     while(1):
#         main()
#


#使用requests库

import requests

formdata = {
    "type":"AUTO",
    "i":"i love python",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"false"
}

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

response = requests.post(url, data = formdata, headers = headers)

print (response.text)

# 如果是json文件可以直接显示
print (response.json())

# {"type":"EN2ZH_CN","errorCode":0,"elapsedTime":0,"translateResult":[[{"src":"i love python","tgt":"我喜欢python"}]]}
#{'type': 'EN2ZH_CN', 'errorCode': 0, 'elapsedTime': 0, 'translateResult': [[{'src': 'i love python', 'tgt': '我喜欢python'}]]}
