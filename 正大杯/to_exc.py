# f_path=r'data1.txt'
# with open(f_path) as f:
#     for line in f:
#         for i in line:

import xlwt
def writeinexcel():
 
    f = open('data4.txt','r',encoding='utf-8') #打开数据文本文档，注意编码格式的影响
    wb = xlwt.Workbook(encoding = 'utf-8') #新建一个excel文件
    ws1 = wb.add_sheet('first') #添加一个新表，名字为first
    ws1.write(0,0,'名称')
    row = 1 #写入的起始行
    col = 0 #写入的起始列
    #通过row和col的变化实现指向单元格位置的变化
    k = 1
    for lines in f: 
        a = lines #txt文件中每行的内容按逗号分割并存入数组中
        k+=1
        # for i in range(len(a)):
        #     ws1.write(row, col ,a[i])#向Excel文件中写入每一项
        #     col += 1
        ws1.write(row, col ,a)
        row += 1
        col = 0
    
    wb.save("neww.xls") 
if __name__ == "__main__":
    writeinexcel()
