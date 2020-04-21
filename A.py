a = input()
for i in range(int(a)):
    n = int(input())
    for k in range(2,500000000):
        if not  n % (2**k - 1):
            print( int(n/ ((2**k) - 1)))
            break
        