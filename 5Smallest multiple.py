'''第一种方法是自己写的，第二种是看到别人写的，第三种是模仿写的，发现时间其实没多大差别。
自己的第一种方法的时间计算的时间太久，时间的显示是看的别人写的。后来发现加上步长就会迅速
降低时间的消耗。
'''
#---------------------FIRST SOLUTION------------------------------------
import time
t=time.time()
for i in range(2520,1000000000000,2520):
    if   i%11==0 and i%12==0 and i%13==0 and i%14==0 and i%15==0 and i%16==0 and i%17==0 and i%18==0 and i%19==0 and i%20==0:
        print(i)
        break
timer = time.time() - t
print(timer, "sec")
t = time.time()
#0.0279998779296875 sec
#---------------------SECOND SOLUTION------------------------------------
import time
t = time.time()
for i in range(2520,1000000000000,2520):
    if i % 11 == 0:
        if i % 13 == 0:
            if i % 16 == 0:
                if i % 17 == 0:
                    if i % 19 == 0:
                        print(i)
                        break
timer = time.time() - t
print(timer, "sec")
t = time.time()
#0.026000261306762695 sec
#---------------------THIRD SOLUTION------------------------------------
import time
t = time.time()
for i in range(2520,1000000000000,2520):
    if i%11==0:
        if i % 12 == 0:
            if i % 13 == 0:
                if i % 14 == 0:
                    if i % 15 == 0:
                        if i % 16 == 0:
                            if i % 17 == 0:
                                if i % 18 == 0:
                                    if i % 19 == 0:
                                        if i % 20 == 0:
                                            print(i)
                                            break
timer = time.time() - t
print(timer, "sec")
t = time.time()
#0.025999784469604492 sec
