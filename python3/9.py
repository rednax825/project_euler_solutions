def get_special_triple_prod():
    c, m = 0, 2

    while True:
        for n in range(1, m):
            a = m*m-n*n
            b = 2*m*n
            c = m*m+n*n
            if a + b + c == 1000:
                print(a)
                print(b)
                print(c)
                return a*b*c
        m += 1

print(get_special_triple_prod())