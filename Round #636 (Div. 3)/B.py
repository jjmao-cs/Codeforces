a = input()
for i in range(int(a)):
    n = int(input())
    if (n / 2) % 2 == 1:
        print('NO')
        continue
    n = int(n/2)
    print('YES')
    print(*range(2, 2*(n+1),2), end=' ')
    print(*range(1, 1+2*(n-1),2), end= ' ')
    print(sum(range(2, 2*(n+1),2)) - sum(range(1, 1+2*(n-1),2)))