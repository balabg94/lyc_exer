def breakdown(n, d):
#    d= { 2000: 3, 500: 2, 200: 2, 100: 1, 50: 0, 20: 0, 10: 0, 1: 1}
    denominations = [ 2000, 500, 200, 100, 50, 20, 10, 5, 1]
    balance = {}
    for i in denominations:
        if i not in d:
            d[i] = 0
        else:
            continue
    count_2000 = 0
    count_500 = 0
    count_200 = 0
    count_100 = 0
    count_50  = 0
    count_20  = 0
    count_10  = 0
    count_5  = 0
    count_1 = 0
    while n:
        if n-2000 >=0 and d[2000]>0:
            count_2000 += 1
            n -= 2000
            d[2000] -= 1
            # print(n)
            balance[2000] = count_2000
            continue       
        elif n-500 >=0 and d[500]>0:
            count_500 += 1
            n -= 500
            d[500] -= 1
            #print(n)
            balance[500] = count_500
            continue
        elif n-200 >=0 and d[200]>0:
            count_200 +=1
            n -= 200
            d[200] -= 1
            #print(n)
            balance[200] = count_200
            continue
        elif n-100 >=0 and d[100]>0:
            count_100 +=1
            n -= 100
            d[100] -= 1
            #print(n)
            balance[100] = count_100
            continue
        elif n-50 >=0 and d[50]>0:
            count_50 +=1
            n -= 50

            d[50] -= 1
            #print(n)
            balance[50] = count_50
            continue
        elif n-20 >=0 and d[20]>0:
            count_20 +=1
            n -= 20
            d[20] -= 1
            #print(n)
            balance[20] = count_20
            continue
        elif n-10 >=0 and d[10]>0:
            count_10 +=1
            n -= 10
            d[10] -= 1
            #print(n)
            balance[10] = count_10
            continue
        elif n-5 >=0 and d[5]>0:
            count_5 +=1
            n -= 5
            d[5] -= 1
            #print(n)
            balance[5] = count_5
            continue
        elif n-1 >=0 and d[1]>0:
            count_1 +=1
            n -= 1
            d[1] -= 1
            #print(n)
            balance[1] = count_1
            continue
        else:
            break
    left =  n
#    print(f"Balance:{left}")
#    print(f"{balance}")
    return left, balance
