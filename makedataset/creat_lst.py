#用于在制作cifar10数据集时输出lst文件
import os
import os.path

rootdir1 = "/rcc"
 
file_object = open('/data/images1.lst','w')
 
for parent,dirnames,filenames in os.walk(rootdir1):
	for filename in filenames:
		print  filename
		if ".png" in filename:
                 file_object.write(filename + 'rcc')
file_object.close()

rootdir2 = "/papillary"
 
file_object = open('/data/images2.lst','w')
 
for parent,dirnames,filenames in os.walk(rootdir1):
	for filename in filenames:
		print  filename
		if ".png" in filename:
                 file_object.write(filename + 'papillary')
file_object.close()

rootdir3 = "/notca"
 
file_object = open('/data/images3.lst','w')
 
for parent,dirnames,filenames in os.walk(rootdir1):
	for filename in filenames:
		print  filename
		if ".png" in filename:
                 file_object.write(filename + 'notca')
file_object.close()

# 合并多个lst
# 获取目标文件夹的路径
rootdir4 = "/data"
# 获取当前文件夹中的文件名称列表
filenames = os.listdir(rootdir4)
result = "image.lst"
# 打开当前目录下的result.txt文件，如果没有则创建
file = open(result, 'w+', encoding="utf-8")
# 向文件中写入字符
 
# 先遍历文件名
for filename in filenames:
    filepath = rootdir4 + '/'
    filepath = filepath + filename
    # 遍历单个文件，读取行数
    for line in open(filepath, encoding="utf-8"):
        file.writelines(line)
    file.write('\n')
# 关闭文件
file.close()