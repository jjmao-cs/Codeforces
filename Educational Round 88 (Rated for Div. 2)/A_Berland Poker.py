import math
num = int(input())
for i in range(num):
    n, m, k = [int(x) for x in input().split()]
    avg = int(n/k)
    if avg >= m:
        print(m)
        continue
    left = m - avg
    if left > (k-1):
        other_max = math.ceil(left/(k-1))
        print(avg - other_max)
        continue
    print(avg - 1)
    
    