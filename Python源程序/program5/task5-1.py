import shutil
from pyunpack import Archive
import os
import py7zr


path = 'D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据'

data = os.path.join(path, 'DataB')
# clear dir first
if os.path.exists(data):
    shutil.rmtree(data)
os.mkdir(data)
Archive(data + ".rar").extractall(data)

for work in os.listdir(data):
    if os.path.isdir(work):
        continue
    vec = work.split('.')
    if len(vec) != 2:
        continue
    dir_name = vec[0]
    work = os.path.join(data, work)
    work_dir = os.path.join(data, dir_name)
    os.mkdir(work_dir)
    if vec[1].lower() == '7z':
        archive = py7zr.SevenZipFile(work, mode='r')
        archive.extractall(path=os.path.abspath(work_dir))
        archive.close()
    else:
        Archive(work).extractall(work_dir)
    os.remove(work)