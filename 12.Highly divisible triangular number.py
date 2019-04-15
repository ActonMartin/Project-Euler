
import math
higher_than = 500
def count_divisors(n):
    num = 0
    sq = int(math.sqrt(n))
    for i in range(1, sq):
        if n % i == 0:
            num += 2
    if sq * sq == n:
        num += 1
    return num
i = 2
while True:
    number = i * (i + 1) // 2
    div = count_divisors(number)
    if div > higher_than:
        print(number)
        break
    i += 1
