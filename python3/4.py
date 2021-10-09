def is_palendrome(num):
    str1 = str(num)
    str2 = str(num) [::-1]
    return str1 == str2

a = 0
for i in range(100,999):
    for j in range(i, 999):
        b = i * j
        if is_palendrome(b) and b > a:
            a = b

print(a)