import io

import fitz
import os
import pandas as pd
import PIL.Image as Image

base='../../'
path = os.path.join(base, 'DataA')

id_name = '正式登记证号'

criteria = pd.read_excel(os.path.join(base, 'criteria2_1.xlsx'))
print("criteria: ",criteria)
criteria_ids = set(criteria[id_name])
print('criteria_ida: ', criteria_ids)
scores = []
for work in os.listdir(path):
    work_name = work
    work = os.path.join(path, work)
    if not os.path.isdir(work):
        scores.append(0)
        continue

    task21_path = os.path.join(work, 'task2_1.xlsx')
    if not os.path.exists(task21_path):
        print(work_name, 'no task2_1.xlsx')
        scores.append(0)
        continue

    task21 = pd.read_excel(task21_path, sheet_name=0)
    task21_ids = set(task21[id_name])

    common_ids = criteria_ids.intersection(task21_ids)
    criteria_names = criteria[criteria[id_name].isin(common_ids)]['产品通用名称']
    task21_names = task21[task21[id_name].isin(common_ids)]['产品通用名称']

    # 2.1(1)
    s1 = (criteria_names.to_numpy() != task21_names.to_numpy()).sum()
    print(work_name, s1)

    # 2.1(2)
    s2 = len(criteria_ids - common_ids)

    # 2.1(3)
    s3 = len(task21_ids - common_ids)

    s = s1 + s2 + s3

    if s == 0:
        scores.append(15)
    elif s <= 10:
        scores.append(10)
    elif s <= 20:
        scores.append(5)
    else:
        scores.append(0)

print(scores)