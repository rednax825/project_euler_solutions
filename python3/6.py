a = 0
b = 0
for i in range(101):
    a += i
    b += i*i
    
a *= a
print(a)
print(b)
print(a-b)