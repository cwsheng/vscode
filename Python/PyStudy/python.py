# -*- coding: utf-8 -*-
import pprint
import random
import weahter
import math

def sayNum():
    num = int(random.uniform(1, 10))
    print 'Guess that I think?'
    bingo = False
    while bingo == False:
        answer = input()
        bingo = isEqual(answer, num)


def isEqual(answer, num):
    if answer < num:
        print 'too small!'
        return False
    elif answer > num:
        print 'too big!'
        return False
    else:
        print 'BINGO'
        return True


l = [365, 'everyday', 0.618, True]

l.append('Python')

print l

del l[1]
print l

print l[-3]

print l[1:-1]

print ';'.join(['apple', 'pear', 'orange'])

f = file("a.txt")
lines = f.readlines()
f.close()

#and-or 技校(三元操作符?:)

a = input()
print a>10 and 'big' or 'small'
#元组，类似c# Tuple 类
#print '%s is %d years old' % ('Mike', 23)

try:
    results = []
    for line in lines:
        data = line.split()
        sum = 0
        for score in data[1:]:
            sum += int(score)
        result = '%s\t: %d\n' % (data[0], sum)
        results.append(result)
    print results
except:
    print 'Error'
else:
    print 'ELSE'
finally:
    print 'finally'

f = file("data.txt", 'a')
f.writelines('study python')
f.close()

sourceinfos = {'萧峰': 95, '段誉': 97, '虚竹': 89}

print sourceinfos['虚竹']
#获取网页内容
#weahter.openurl('http://www.baidu.com')

print math.pi


#计算一元二次方程
def CalcFun(a,b,c):
    x = (-b+math.sqrt(math.pow(b,2)-(4*a*c)))/(2*b)
    x1 = (-b -math.sqrt(math.pow(b,2)-(4*a*c)))/(2*b)
    print x 
    print x1

print '请是输入一元二次方程a值：'
a = input()
print '请是输入一元二次方程b值：'
b = input()
print '请是输入一元二次方程c值：'
c = input()
CalcFun(a,b,c)