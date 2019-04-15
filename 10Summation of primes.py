'''
142913828922
311.00499987602234 sec
'''

# import time
# t = time.time()
# i=2
# sum=0
# import math
# while(i<=2000000):
#     prime=True
#     for j in range(2,int(math.sqrt(i))+1):
#         if (i%j==0):
#             prime=False
#     if prime:
#         sum+=i
#     i+=1
# print(sum)
# timer = time.time() - t
# print(timer, "sec")

'''
142913828922
311.00499987602234 sec
'''

a=2*10**6+1
b=int(a**.5)+1
c=list(range(a+1))
c[1]=0
for i in range(b+1):
    if c[i]:
        for j in range(2*i, a+1, i):
            c[j]=0
print(sum(c))
