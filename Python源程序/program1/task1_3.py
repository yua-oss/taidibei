import os

# 读取DataA里面文件的路径
list_DataA = os.listdir('./DataA（text）')
path_wj = []
for st in list_DataA:
    path = './DataA（text）'+'/'+st
    path_wj.append(path)
print(path_wj)
# 统计DataA文件子文件目录里面的分数。
# 统计规则为，1、以task1_2.py程序的基础上，统计除了'image'文件的个数
#           2、将统计的个数*2，即为分数。
score = []
for x in path_wj:
    sc = len(os.listdir(x))-1
    score.append(sc*2)
print(score)  # 打印输出**
print(len(score))