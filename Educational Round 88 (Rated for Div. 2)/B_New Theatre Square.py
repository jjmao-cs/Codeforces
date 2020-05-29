import math
num = int(input())
for i in range(num):
    n, m, x, y = [int(x) for x in input().split()]
    # graph = []
    cost = 0
    for j in range(n):
        a = input()
        # graph.append(a)
        if y > 2*x:
            cost = cost + a.count('.')*x
        else:
            flag = False
            twice = 0
            once = 0
            for k in range(m):
                if a[k] == '*':
                    continue
                if not flag:
                    if k+1 > m-1:
                        once += 1
                        continue
                    elif a[k+1] == '.':
                        flag = True
                    else:
                        once += 1
                else:
                    twice += 1
                    flag = False
            cost = cost + twice *y + once*x
    print(cost)