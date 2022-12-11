dic = {'a' : 1, 'b': 2}

print(dic['a'])
if 'c' not in dic:
    print("no c in dic!")
else :
    print(dic['c'])

print(dic.pop('a'))
print(dic)