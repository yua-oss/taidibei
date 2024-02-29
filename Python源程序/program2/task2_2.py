import io

import fitz
import os
import pandas as pd
import PIL.Image as Image
import numpy as np

base='../../'
path = os.path.join(base, 'DataA')

id_name = '正式登记证号'

criteria = pd.read_excel(os.path.join(base, 'criteria2_2.xlsx'))
criteria_ids = set(criteria[id_name])
scores = []
for work in os.listdir(path):
    work_name = work
    work = os.path.join(path, work)
    if not os.path.isdir(work):
        scores.append(0)
        continue

    task22_path = os.path.join(work, 'task2_2.xlsx')
    if not os.path.exists(task22_path):
        print(work_name, 'no task2_2.xlsx')
        scores.append(0)
        continue

    task22 = pd.read_excel(task22_path, sheet_name=0)
    task22_ids = set(task22[id_name])

    common_ids = criteria_ids.intersection(task22_ids)
    criteria_names1 = np.str(criteria[criteria[id_name].isin(common_ids)]['无机标签'].to_numpy())
    criteria_names2 = np.str(criteria[criteria[id_name].isin(common_ids)]['有机标签'].to_numpy())
    criteria_names = '(' + criteria_names1 + ',' + criteria_names2 + ')'
    task22_names = task22[task22[id_name].isin(common_ids)]['分组标签'].to_numpy().astype(np.str)
    task22_names = np.char.replace(task22_names, ' ', '')

    # 2.2(1)
    s1 = (criteria_names != task22_names).sum()
    print(work_name, s1)

    # 2.2(2)
    s2 = len(criteria_ids - common_ids)

    # 2.2(3)
    s3 = len(task22_ids - common_ids)

    s = s1 + s2 + s3

    if s <= 5:
        scores.append(15)
    elif s <= 15:
        scores.append(10)
    elif s <= 30:
        scores.append(5)
    else:
        scores.append(0)

print(scores)