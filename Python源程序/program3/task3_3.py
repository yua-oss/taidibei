import pandas as pd
import os
import numpy as np


base = 'D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据/Python源程序/program1'
path = os.path.join(base, 'DataA（text）')
list_DataA = os.listdir(base + '/DataA（text）')


def chaz3(path_name):
    if 'task3.xlsx' not in os.listdir(base + '/DataA（text）' + '/' + path_name):
        return 0
    else:
        task3_path = os.path.join(path, path_name, 'task3.xlsx')
        if not os.path.exists(task3_path):
            exit(0)
        task3 = pd.read_excel(task3_path)
        G = task3.iloc[:, 1:]
        G = G.values
        res = np.diagonal(G, offset=0)
        z1 = np.ones(len(G))
        print(res)
        print(z1)
        if sum(res) == sum(z1):
            # print('get')
            return 5
        else:
            return 0
        # x = 0
        # for i in range(len(G)):
        #     if G.iloc[i][i] == 1:
        #         x = x+1
        #         # print('x:', x)
        #         if x == len(G):
        #             return 5



# ss = chaz3(list_DataA[0])
task3_2_score0 = []
for x in list_DataA:
    print('x:', chaz3(x))
    task3_2_score0.append(chaz3(x))
print(task3_2_score0)
print(len(task3_2_score0))
