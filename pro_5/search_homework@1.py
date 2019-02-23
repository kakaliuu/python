import os
path='E:\Python_3\【课程代码】从零写Python练手项目：实用脚本\ScriptCourse\Project1\LessonCode\WindowsVersion\images'
files=os.listdir(path)
print(files)
for f in files:
    if(not f.endswith('.gif')) and ("project30" in f or 'commercial' in f):
        print('Foundit!' + f)


