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

sum = 0
for i in gen_primes():
    if i > 2000000:
        break
    sum += i

print(sum)