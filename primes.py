def prime(n):
    primes = {}
    out = []
    for i in range(2, n):
        primes[i] = True

    var = 2
    while ((var*var) <= n):
        if primes[var] == True:
            for x in range(var*2, n+1, var):
                primes[x] = False
        var+=1
        
    for y in range(2, len(primes)):
        if primes[y] == True:
            out.append(str(y))
    return ', '.join(out)
        
def test():
    return prime(10000)
