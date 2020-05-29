import math
num = int(input())
for i in range(num):
    h,c,t = [int(x) for x in input().split()]
    prev_high = 999999999
    prev_low = 0
    total = 0
    cur = 0
    count = 0
    while True:
        
        # hot water
        total += h
        count += 1
        cur = total/count
        

        if cur == t:
            print(count)
            break
        if cur < t:
            if prev_high-t > t-cur:
                if t-prev_low > t-cur:
                    print(count)
                    break
                else:
                    print(count-1)
            else:
                if t-prev_low > prev_high -t:
                    print(count-2)
                    break
                else:
                    print(count -1)
                    break
                
        if cur > prev_high:
            print(count -1)
            break
        prev_high = cur

        # cold water
        total += c
        count += 1
        cur = total/count
        
        if cur > t and count ==2:
            print(count)
            break
        if cur == t and count != 0:
            print(count)
            break
        if cur > t:
            if cur-t > t-prev_low:
                print(count-2)
                break
            else:
                print(count)
                break
        if cur < prev_low:
            print(count -1)
            break
        prev_low = cur