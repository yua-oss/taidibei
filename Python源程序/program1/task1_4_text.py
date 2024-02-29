import fitz
import time
import re
import os


# 1.使用正则表达式查找PDF中的图片
def pdfTOpic(path, pic_path):  # path:pdf的路径，pic_path:图片保存的路径
    t0 = time.perf_counter()  # python 3.8已经不支持time.clock了
    # 使用正则表达式来查找图片
    checkXO = r"/Type(?= */XObject)"
    checkIM = r"/Subtype(?= */Image)"
    # 打开pdf
    doc = fitz.open(path)
    # 图片计数
    imgCount = 0
    lenXREF = doc.xref_length()

    # 打印pdf的信息
    print("文件名:{},页数:{},对象:{}".format(path, len(doc), lenXREF - 1))

    # 遍历每一个对象
    for i in range(1, lenXREF):
        # 定义对象字符串
        text = doc.xref_object(i)
        # print(i,text)

        isXObject = re.search(checkXO, text)
        # 使用正则表达式查看是否是图片
        isImage = re.search(checkIM, text)
        # 如果不是对象也不是图片，则continue
        if not isXObject or not isImage:
            continue
        imgCount += 1
        # 根据索引生成图像
        pix = fitz.Pixmap(doc, i)
        # 根据pdf的路径生成图片的名称
        new_name = path.replace('\\', '_') + "_img{}.png".format(imgCount)
        new_name = new_name.replace(':', '')
        print('text1:', os.path.join(pic_path, new_name))
        # 如果pix.n<5，可以直接存为png
        if pix.n < 5:
            pix.writePNG(os.path.join(pic_path, new_name))
        # 否则先转换CMYK
        else:
            pix0 = fitz.Pixmap(fitz.csRGB, pix)
            pix0.writePNG(os.path.join(pic_path, new_name))
            pix0 = None
        # 释放资源
        pix = None
        t1 = time.perf_counter()
        print("运行时间:{}s".format(t1 - t0))
        print("提取了{}张图片".format(imgCount))


if __name__ == '__main__':

    list_DataA = os.listdir('./DataA（text）')
    path_wj = []
    for st in list_DataA:
        path = './DataA（text）' + '/' + st
        path_wj.append(path)
    print(path_wj)
    # file_path = r'C:\xxx\xxx.pdf' # PDF 文件路径
    # dir_path = r'C:\xxx' # 存放图片的文件夹
    file_path = path_wj[0] + '/task2_3.pdf'
    dir_path = path_wj[0] + '/' + 'image'
    print(os.listdir(dir_path))

    m = pdfTOpic(file_path, dir_path)
