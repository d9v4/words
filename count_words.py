# -*- coding: utf-8 -*- 

f = open('texts_for_tests\\bit.txt', 'r')
s = f.read()
s = s.replace(',', '')
s = s.replace('.', '')
s = s.replace(';', '')
s = s.replace(':', '')
s = s.replace('-', '')
s = s.replace('(', '')
s = s.replace(')', '')
s = s.replace('?', '')
s = s.replace('!', '')
sp = s.lower().split(' ')
count = 0
d = {}

for i in sp:
    if i in d:
        pass
    else:
        d[i] = 1
        for a in sp:
            if a == i:
                d[i] = d[i] + 1


lkey = []
lvalue = []

for t in d:
    lkey.append(t)
    lvalue.append(d[t])
    #print(t, ' ', d[t])

for i in range(len(lvalue)):
    for j in range(len(lvalue) - 1, i, -1):
        if lvalue[j] < lvalue[j-1]:
            lvalue[j], lvalue[j-1] = lvalue[j-1], lvalue[j] 
            lkey[j], lkey[j-1] = lkey[j-1], lkey[j]
    
for a in range(len(lkey)):
    print(lkey[a], ': ', lvalue[a])

input()
