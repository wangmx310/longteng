import xlrd
import yaml

from utils.path import DATA_FILE
class Excel(object):
    def __init__(self,file_path):
       self.wb = xlrd.open_workbook(file_path)



    def get_sheet(self,sheet_name):
        sh= self.wb.sheet_by_name(sheet_name)
        title= sh.row_values(0)
        print(title)
        data=[]
        for row in range(1,sh.nrows):
            case_data = sh.row_values(row)
            data.append(dict(zip(title,case_data)))
            print(data)


def get_data():
    with open(DATA_FILE,encoding='utf-8') as f:
        return yaml.loads(f)    #把yaml文件转为字典格式



if __name__ == '__main__':
     excel= Excel('data.xls')
     excel.get_sheet('执行用例')