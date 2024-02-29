"""
function:   批量解压缩
detail:     批量解压缩
author:     w.royee
date:       2021-08-29
"""

import os
# import rarfile
import shutil
from unrar import rarfile
import zipfile


class Uncompress:
    def __init__(self):
        self.abs_path = os.getcwd()  # 工作目录的绝对路径
        self.compress_path = os.path.join(self.abs_path, '压缩包目录')
        self.umcompress_path = os.path.join(self.abs_path, '解压缩目录')
        # walk出来的结果是递归的目录结构，demo只处理当前目录下的文件，不处理子文件夹下的文件，因此取结果中的第一条
        for path_, dir_, self.filenames in os.walk(self.compress_path):
            break

    def unrar(self):
        """
        rar格式解压缩
        :param
        :return:
        """
        for filename in self.filenames:
            name, ext = os.path.splitext(filename)
            if '.rar' == ext:
                print('解压缩文件：', filename)
                file = os.path.join(self.compress_path, filename)
                rar = rarfile.RarFile(file)
                # 设置解压缩指定目录
                outdir = os.path.join(self.umcompress_path, name)
                if os.path.isdir(outdir):
                    pass
                else:
                    os.makedirs(outdir)
                # 解压缩到指定目录
                rar.extractall(outdir)

    def unzip(self):
        """
        zip格式解压缩
        :param
        :return:
        """
        for filename in self.filenames:
            file = os.path.join(self.compress_path, filename)
            # 重新定位到工作目录，否则ZipFile实现使用open找不到源文件
            os.chdir(self.compress_path)
            # 判断是否zip压缩格式
            if zipfile.is_zipfile(filename):
                print('解压缩文件：', filename)
                # 设置解压缩指定目录
                outdir = os.path.join(self.umcompress_path, os.path.splitext(filename)[0])
                # 解压目录如果存在，先递归删除，重新创建，否则重复运行程序rename会存在同名文件报错
                if os.path.exists(outdir):
                    shutil.rmtree(outdir)
                os.makedirs(outdir)
                # 解压缩到指定目录
                zip = zipfile.ZipFile(file)
                zip.extractall(outdir)
                zip.close()
                # 解压后重命名文件，修复中文乱码
                self.rename(outdir)

    def rename(self, curr_dir):
        """
        重命名文件夹或文件名
        :param curr_dir: 目录
        :return:
        """
        os.chdir(curr_dir)
        for name in os.listdir():
            # 使用cp437对文件名进行解码还原后转为可读格式
            new_name = name.encode('cp437').decode('gbk')
            os.rename(name, new_name)
            # 递归调用
            if os.path.isdir(new_name):
                self.rename(new_name)
                # 处理完要回到上级目录
                os.chdir('..')


if __name__ == '__main__':
    Uncompress = Uncompress()
    # print('包括压缩包如下：')
    # for each in Uncompress.filenames:
    #     print(each)
    # input('输入回车开始解压缩')
    Uncompress.unrar()
    # Uncompress.unzip()
