import io

import fitz
import os

import PIL.Image as Image

path = 'D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据/Python源程序/program1/DataA（text）'
for work in os.listdir(path):
    work_name = work
    work = os.path.join(path, work)
    if not os.path.isdir(work):
        continue

    image_dir = os.path.join(work, 'image')
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    task2_3 = os.path.join(work, 'task2_3.pdf')
    if not os.path.exists(task2_3):
        continue

    doc = fitz.open(task2_3)
    image_num = 1
    for i in range(len(doc)):
        page = doc[i]
        image_list = doc.get_page_images(i)
        if not image_list:
            continue
        for image_idx, img in enumerate(image_list, start=1):
            xref = img[0]
            image = doc.extract_image(xref)
            image_bytes = image["image"]
            image_ext = image["ext"]
            image = Image.open(io.BytesIO(image_bytes))
            img_path = os.path.join(work, 'image', f'{work_name}_{image_num}.png')
            image.save(open(img_path, "wb"))
            image_num += 1
