import pandas as pd
import os

base = 'D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据/Python源程序/program1'
path = os.path.join(base, 'DataA（text）')
list_DataA = os.listdir(base + '/DataA（text）')


def chaz(path_name):
    if 'task3.xlsx' not in os.listdir(base + '/DataA（text）' + '/' + path_name):
        return None
    else:
        task3_path = os.path.join(path, path_name, 'task3.xlsx')
        if not os.path.exists(task3_path):
            exit(0)

        criteria = pd.read_excel(
            os.path.join('D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据/', 'criteria3.xlsx'))
        task3 = pd.read_excel(task3_path)

        criteria_ids = set(criteria.iloc[:, 0])
        task3_ids = set(task3.iloc[:, 0])

        # 3.2(1)
        s1 = len(criteria_ids - task3_ids)
        # print(s1)

        # 3.2(2)
        s2 = len(task3_ids - criteria_ids)
        # print(s2)
        print(s1+s2)
        return s1 + s2


task3_2_score0 = []
task3_2_score = []
for x in list_DataA:
    task3_2_score0.append(chaz(x))
print(task3_2_score0)
for s in task3_2_score0:
    if s is None:
        s = 0
    elif s == 0:
        s = 15
    elif 1 <= s <= 2:
        s = 10
    elif 3 <= s <= 5:
        s = 5
    else:
        s = 0
    task3_2_score.append(s)
print(task3_2_score)
print(len(task3_2_score))
