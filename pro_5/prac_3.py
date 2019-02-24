# coding:utf-8

import shutil
import os

path = './'
files = os.listdir(path)

for f in files:
    # f.png
    #./png
    # os.path.join()函数用来连接路径，与视频中的“+”号效果类似，但是前者可以避免不同操作系统对程序带来的影响
    folder_name = os.path.join('.',f.split('.')[-1])
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        shutil.move(f,folder_name)
    else:
        shutil.move(f,folder_name)


