def breakdown(n):
    out = {2000:0, 500:0, 200:0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0}
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
        if n%2000 == 0:
            count_2000 += 1
            n -= 2000
            continue
        elif n%500 == 0:
            count_500 += 1
            n -= 500
            continue
        elif n%200 == 0:
            count_200 +=1
            n -= 200
            continue
        elif n%100 == 0:
            count_100 +=1
            n -= 100 
            continue
        elif n%50 == 0:
            count_50 +=1
            n -= 50 
            continue
        elif n%20 == 0:
            count_20 +=1
            n -= 20 
            continue
        elif n%10 == 0:
            count_10 +=1
            n -= 10 
            continue
        elif n%5 == 0:
            count_5 +=1
            n -= 5 
            continue
        elif n%1 == 0:
            count_1 +=1
            n -= 1 
            continue
        else:
            break


    out[2000] = count_2000
    out[500] = count_500
    out[200] = count_200
    out[100] = count_100
    out[50] = count_50
    out[20] = count_20
    out[10] = count_10
    out[5] = count_5
    out[1] = count_1       
    return out
    
        #  print(f"2000 = {count_2000}, 500 = {count_500}, 200 = {count_200}, 100 = {count_100}, 50 = {count_50}, 20 = {count_20}, 10 = {count_10}, 5 = {count_5} 1 = {count_1}")
