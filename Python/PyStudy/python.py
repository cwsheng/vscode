import pprint
import random
 
def sayNum():
    num = int(random.uniform(1, 10))
    print 'Guess that I think?'
    bingo = False
    while bingo == False:
        answer = input()
        bingo= isEqual(answer,num)

def isEqual(answer,num):
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

f = file('data.txt')
data =  f.readlines()
print data
f.close()

f = file("a.txt")
lines = f.readlines()
f.close()

try:
    results = []
    for line in lines:
        data = line.split()
        sum = 0
        for score in data[1:]:
            sum+=int(score)
        result = '%s\t: %d\n' % (data[0], sum) 
        results.append(result)
    print results
except :
    print 'Error'
else:
    print 'ELSE'
finally:
    print 'finally'


f = file("data.txt",'a')
f.writelines('study python')
f.close()

