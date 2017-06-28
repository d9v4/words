# -*- coding: utf-8 -*- 

f = open('texts_for_tests\\bit.txt', 'r')
s = f.read()
f.close()

s = s.replace(',', '')
s = s.replace('.', '')
s = s.replace(';', '')
s = s.replace(':', '')
s = s.replace('-', '')
s = s.replace('(', '')
s = s.replace(')', '')
s = s.replace('?', '')
s = s.replace('!', '')
s = s.replace('\n', '')
s = s.replace('"', '')

sp = s.lower().split(' ')
print('Подготовка успешно')
count = 0
d = {}

for i in sp:
    print(count, 'из ', len(sp))
    count = count + 1
    if i in d:
        pass
    else:
        d[i] = 0
        for a in sp:
            if a == i:
                d[i] = d[i] + 1


lkey = []
lvalue = []
print('Посчитали!')
for t in d:
    lkey.append(t)
    lvalue.append(d[t])
    #print(t, ' ', d[t])
print('сортируем...')
c = 0
for i in range(len(lvalue)):
    print(c, 'из ', len(lvalue))
    c = c + 1
    for j in range(len(lvalue) - 1, i, -1):
        if lvalue[j] < lvalue[j-1]:
            lvalue[j], lvalue[j-1] = lvalue[j-1], lvalue[j] 
            lkey[j], lkey[j-1] = lkey[j-1], lkey[j]
print('Сохраняем...')    
f1 = open('texts_for_tests\\result.txt', 'w')
for a in range(len(lkey)):
    #print(lkey[a], ': ', lvalue[a])
    f1.write(str(lkey[a]) + ': ' + str(lvalue[a]) + '\n')
f1.close()    
input()
