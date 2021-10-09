def is_div(num):
    for i in range(1,20):
        if num % i != 0:
            return False
    return True

a = 1
for i in range(2, 20):
    a *= i

decreased = True
while decreased:
    decreased = False
    for i in range(2, 20):
        if is_div(a/i):
            a /= i
            decreased = True
            
print(a)
    