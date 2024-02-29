from pyunpack import Archive
import os
# D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据
path = 'D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据'

listdir = os.listdir()
print(listdir)

if 'DataA' not in listdir:
    os.mkdir('DataA')
Archive(path+"/DataA.rar").extractall("DataA")


list_DataA = os.listdir('DataA')
for i in range(len(list_DataA)):
    str1 = list_DataA[i]
    str1_name = str1[0:4]

    # print(str1, str1[0:4])
    # print(os.listdir('./DataA'))
    # if str1_name not in os.listdir('./DataA'):
    #     os.mkdir('./DataA/'+str1_name)
    #     print('true')
    res = Archive('./DataA/'+str1)
    res.extractall('./DataA/'+str1_name) # 解压缩
    print('已解压到', str1_name)
    if i == len(list_DataA):
        print('win!')


