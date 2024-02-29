import io
import fitz
import os
import pandas as pd
import PIL.Image as Image

base = 'D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据/Python源程序/program1'
sheet = pd.DataFrame(columns=['作品号', '图片编号', '保存路径', '图片分辨率', '图片文件大小'])
path = os.path.join(base, 'DataA（text）')

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
            pil_image = Image.open(io.BytesIO(image_bytes))
            img_path = os.path.join(work, 'image', f'{work_name}_{image_num}.png')
            pil_image.save(open(img_path, "wb"))
            width = image['width']
            height = image['height']
            sheet.loc[len(sheet.index)] = [work_name, f'{work_name}_{image_num}',
                                           os.path.abspath(img_path), f'{width}*{height}',
                                           f'{len(image_bytes)//1024}KB']
            image_num += 1

writer = pd.ExcelWriter(os.path.join(base, 'summary', 'result1_4.xlsx'), engine='xlsxwriter')
sheet.to_excel(writer, sheet_name='Sheet1', index=False)
workbook = writer.book
worksheet = writer.sheets['Sheet1']
merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': 2})

for work_num in sheet['作品号'].unique():
    # find indices and add one to account for header
    u = sheet.loc[sheet['作品号'] == work_num].index.values + 1
    if len(u) >= 2:
        worksheet.merge_range(u[0], 0, u[-1], 0, sheet.loc[u[0],'作品号'], merge_format)
writer.save()
