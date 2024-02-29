import datetime
import os

import fitz  # fitz就是pip install PyMuPDF

#  D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据/Python源程序/program1/DataA（text）
path_Data = 'D:/Desktop/泰迪杯数据分析技能赛/A题：竞赛作品的自动评判数据/Python源程序/program1/DataA（text）'


def pyMuPDF_fitz(pdfPath, imagePath):
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    print('pdfDoc: ', pdfDoc)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        # zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        # zoom_y = 1.33333333
        zoom_x = zoom_y = 10
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建

        pix.writePNG(imagePath + '/' + 'images_%s.png' % pg)  # 将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)


if __name__ == "__main__":

    list_DataA = os.listdir('./DataA（text）')
    path_wj = []
    for st in list_DataA:
        path = './DataA（text）' + '/' + st
        path_wj.append(path)
    print(path_wj)
    # file_path = r'C:\xxx\xxx.pdf' # PDF 文件路径
    # dir_path = r'C:\xxx' # 存放图片的文件夹
    pdfPath = path_wj[0] + '/task2_3.pdf'
    print('pdfPath', pdfPath)
    imagePath = path_wj[0] + '/' + 'image'
    print(os.listdir(imagePath))

    pyMuPDF_fitz(pdfPath, imagePath)
