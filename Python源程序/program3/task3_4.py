import pandas as pd
import os
import numpy as np
base = 'D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据/Python源程序/program1'
path = os.path.join(base, 'DataA（text）')
list_DataA = os.listdir(base + '/DataA（text）')


def check_symmetric(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)


def chaz4(path_name):
    if 'task3.xlsx' not in os.listdir(base + '/DataA（text）' + '/' + path_name):
        return 0
    else:
        task3_path = os.path.join(path, path_name, 'task3.xlsx')
        if not os.path.exists(task3_path):
            exit(0)

        task3 = pd.read_excel(task3_path)
        G = task3.iloc[:, 1:]
        G = G.values
        G_T = G.T
        print(G)
        print(G_T)
        if G == G_T:
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



chaz4(list_DataA[26])

task3_2_score0 = []
for x in list_DataA:
    task3_2_score0.append(chaz4(x))
print(task3_2_score0)
print(len(task3_2_score0))

