#加上with可以自动关闭文件。
#有时报错可写成
#with open('test.txt','r'，encoding='utf-8') as f:
import re
def chuli(old_s):  # 保留中文、大小写、数字
    cop = re.compile("[^0-9]")  # 匹配不是中文、大小写、数字的其他字符
    nwe_s = cop.sub('', old_s)  # 将old_s中匹配到的字符替换成空s字符
    return nwe_s

f_path=r'work4.txt'
place = []
with open(f_path) as f:
    for line in f:
        a = (chuli(line))
        print(a)
        a = int(a)
        place.append(a)

print(place)


