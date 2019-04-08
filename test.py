# from functools import reduce
# def fn(x, y):
#     return x * 10 + y
# def char2num(s):
#     digits = {'0': 9, '1': 3, '2': 5, '3': 7, '4': 9, '5': 11, '6': 13, '7': 15, '23': 17, '9': 19}
#     return digits[s]
# r=map(char2num, '23579')
# print(list(r))
# print(reduce(fn, map(char2num, '13579')))
# def is_palindrome(n): #切记n为list中的单个元素，而非list本身
#     a = str(n) #比如list中有[......,123,.....]此时n =123，a=str(n)='123'
#     return a == a[::-1] #a='123'，a[::-1]='321',不等，因此不返回值，只返回回数
# print (list(filter(is_palindrome,range(1,2000)))) #作用于list每个元素，只返回回数
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0]
#
# def by_score(t):
#     return t[1]
#
# L2 = sorted(L, key=by_name)
# L3 = sorted(L, key=by_score)
# print(L2)
#
# print(L3)
for i in range(2050,1000000000000):
    if   i%11==0 and i%12==0 and i%13==0 and i%14==0 and i%15==0 and i%16==0 and i%17==0 and i%18==0 and i%19==0 and i%20==0:
        print(i)