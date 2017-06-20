# -*- coding: utf-8 -*- 

f = open('texts_for_tests\\bit.txt', 'r')
s = f.read()
s = s.replace(',', '')
s = s.replace('.', '')
sp = s.lower().split(' ')
count = 0
for a in sp:
    
    if a == 'и':
        count = count + 1

print(sp)

input()
