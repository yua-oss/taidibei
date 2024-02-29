import io

import fitz
import os
import pandas as pd
import PIL.Image as Image
import numpy as np
import pdfplumber

base='../../'
path = os.path.join(base, 'DataA')

criteria1 = {'一': 7, '二': 6, '三': 5}
criteria2 = {'一': 2012, '二': 1501, '三': 1038}


def match(criteria, rank_row, target_row):
    ranks = rank_row[1:]
    sc = 0
    for i in range(len(ranks)):
        rank = ranks[i]
        if rank in criteria and criteria[rank] == int(target_row[i+1]):
            sc += 2
    return sc

scores = []
for work in os.listdir(path):
    work_name = work
    work = os.path.join(path, work)
    if not os.path.isdir(work):
        scores.append(0)
        continue

    task23_path = os.path.join(work, 'task2_3.pdf')
    if not os.path.exists(task23_path):
        print(work_name, 'no task2_3.pdf')
        scores.append(0)
        continue

    task2_3 = pdfplumber.open(task23_path)
    score = 0
    for page in task2_3.pages:
        tables = page.extract_tables()
        if tables is None or len(tables) == 0:
            continue
        for table in tables:
            if len(table) <= 1:
                continue
            # row 0
            if len(table[0]) <= 1:
                continue
            if table[0][0] != '排名':
                continue

            if table[1][0] == '分组标签':
                score += match(criteria1, table[0], table[1])
                if len(table) >= 3 and table[2][0] == '产品登记数量':
                    score += match(criteria2, table[0], table[2])
            elif table[1][0] == '产品登记数量':
                score += match(criteria2, table[0], table[1])
                if len(table) >= 3 and table[2][0] == '分组标签':
                    score += match(criteria1, table[0], table[2])
    scores.append(score)

print(scores)