import pandas as pd
import os

base = 'D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据/Python源程序/program1'
path = os.path.join(base, 'DataA（text）')
list_DataA = os.listdir(base + '/DataA（text）')


def chaz0(path_name):
    if 'task3.xlsx' not in os.listdir(base + '/DataA（text）' + '/' + path_name):
        return None
    else:
        task3_path = os.path.join(path, path_name, 'task3.xlsx')
        if not os.path.exists(task3_path):
            exit(0)

        criteria = pd.read_excel(
            os.path.join('D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据/', 'criteria3.xlsx'))
        task3 = pd.read_excel(task3_path)

        if len(criteria) == len(task3):
            return 5
        else:
            return 0


task3_2_score0 = []
for x in list_DataA:
    task3_2_score0.append(chaz0(x))
print(task3_2_score0)
print(len(task3_2_score0))