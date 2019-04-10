import time
t = time.time()
l=[]
i=2
import math
while(len(l)<10001):       #给出了第一项素数2，所以这里只需要小于10001项就可以的了。
    prime=True
    for j in range(2,int(math.sqrt(i))+1):
        if (i%j==0):
            prime=False
    if prime:
        l.append(i)
    i+=1
print(l[-1])
timer = time.time() - t
print(timer, "sec")

