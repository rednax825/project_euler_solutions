def gen_primes():
    D = {}
    q = 2    
    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

count = 0
for i in gen_primes():
    count += 1
    print(str(count) + ": " + str(i))
    if(count > 10001):
        break
