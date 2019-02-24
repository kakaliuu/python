###edi by liurun 20190224
##to move files to one other files
import os
import shutil
path='E:\Python_3\git_python\mygitresp\python\problem2_files'
#将路径转化为当前文件所在路径
#os.makedirs(path + '/image')
#os.makedirs(path +  '/document')
image_suffix=['jpg','png','gif']
doc_suffix=['doc','docx','ppt','md']

for i in image_suffix:
    cur_path=path +'/'+ i
    files=os.listdir(cur_path)
    for f in files:
        #移动文件夹，将docx下的文件移动至document目录下
        shutil.move(cur_path + '/' + f,path + '/image')
    os.removedirs(cur_path)

for d in doc_suffix:
    cur_path=path +'/'+ d
    files=os.listdir(cur_path)
    for f in files:
        #移动文件夹，将docx下的文件移动至document目录下
        shutil.move(cur_path + '/' + f,path + '/document')
    os.removedirs(cur_path)





