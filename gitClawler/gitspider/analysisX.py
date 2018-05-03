#!usr/bin/env python  
# -*- coding: UTF-8 -*- 
""" 
@author:binbinzhang
@file: analysis.py 
@time: 2018/05/03 
@email:binbin_Erices@163.com
@function： 
"""

from openpyxl import load_workbook

def anay():
    file = input("  请输入需要分析的文件名(输入q!退出程序)：\n")
    if file == "q!":
        print("欢迎下次继续使用GitHub数据分析...")
        exit(0)
    try:
        wb = load_workbook("./Excel/{}.xlsx".format(file))
    except:
        print("文件名不存在，请输入正确的文件名称...")
        return

    '''
    namedict = {u"基础开发部":["张三","王五","李四"],
                u"平台开发部":["张三","王五","李四"],
                u"应用开发部": ["张三","王五","李四"],
                u"产品部": ["张三","王五","李四"]
                }
    '''
    namedict = {
        u"基础开发部": [],
        u"平台开发部": [],
        u"应用开发部": [],
        u"产品部": []
        }
    with open("./anayName.json", "r") as obj:
        namedict[u"基础开发部"] = obj.readline()
        namedict[u"平台开发部"] = obj.readline()
        namedict[u"应用开发部"] = obj.readline()
        namedict[u"产品部"] = obj.readline()
        obj.close()

    sheet = wb["Sheet"]
    all = 0
    res = {}
    records = ['        {}       \n\n'.format(file)]
    for x in range(2, sheet.max_row + 1):
        if not res.get(sheet[x][3].value):
            res[sheet[x][3].value] = {}
        if not res[sheet[x][3].value].get(sheet[x][1].value):
            res[sheet[x][3].value].update({sheet[x][1].value: 1})
        else:
            res[sheet[x][3].value][sheet[x][1].value] += 1
    s1 = ''
    s2 = ''
    s3 = ''
    s4 = ''

    for pro, names in res.items():
        count = 0

        for name, num in names.items():
            count += num
            if name in namedict[u'基础开发部']:
                s1 += "\t"+ name + u" 提交 " + str(num) + u"次\n"
            if name in namedict[u'平台开发部']:
                s2 +="\t"+ name + u" 提交 " + str(num) + u"次\n"
            if name in namedict[u'应用开发部']:
                s3 += "\t"+ name + u" 提交 " + str(num) + u"次\n"
            if name in namedict[u'产品部']:
                s4 += "\t"+ name + u" 提交 " + str(num) + u"次\n"
        all += count

    print(u'基础开发部:\n' + s1 )
    print(u'平台开发部:\n' + s2)
    print(u'应用开发部:\n' + s3)
    print(u'产品部:\n' + s4)

    record = u'基础开发部:\n' + s1+'\n'+u'平台开发部:\n' + s2+'\n'+u'应用开发部:\n' + s3+'\n'+u'产品部:\n' + s4+'\n'

    records.append(record)

    all = u"代码提交总数："+str(all)+'\n\n\n'
    records.append(all)
    print("*" * 40+" "*4+ str(all))

    #写入文件
    with open("./gitResults.txt","a") as f:
        f.writelines(records)

    print("Analysis is ending...\n")

if __name__ == "__main__":
    print(" *********************************************************************************")
    print(" *                                                                               *")
    print(" *                                                                               *")
    print(" *                      欢迎使用GitHub数据分析                                   *")
    print(" *                                                                               *")
    print(" *                                                                               *")
    print(" *********************************************************************************\n")
    while True:
        anay()





