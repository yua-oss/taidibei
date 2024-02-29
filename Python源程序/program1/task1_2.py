import os

# 1、读取Python源程序文件的根目录并创建“summary”
# 2、读取DataA每一个子目录的路径
if 'summary' not in os.listdir():
    os.mkdir('summary')
    print('mk victory')
list_DataA = os.listdir('./DataA（text）')
print(list_DataA)
# 3、在每一个子目录路径下创建image
for st in list_DataA:
    path = './DataA（text）'+'/'+st + '/image'
    if not os.path.exists(path):
        os.makedirs(path)


