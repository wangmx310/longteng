#txt文件
import os

# basedir = __file__
# print(__file__)
# print(os.path.dirname(__file__))
# print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

file_path = os.path.join(basedir,'data','1.text')
print(filr_path)
f=open('../data/1.txt')
data = f.readlines()
print(data[0].strip())
# data = [item.strip() for item in f.readlines()]  #去掉空格
# print(data)
f.(ciose)


#__file__  当前文件
# os.path.abspath 获取当前目录的绝对路径
# os.path.dirnam  获取当前目录的上级目录
# os.path.join               路径连接