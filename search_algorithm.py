

"""НОД"""
a = 81
b = 100
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(a + b)

"""ПОИСК НАИБОЛЬШЕНО ЧИСЛА В МАССИВЕ"""

a = [1,2,3,4,5,6,7,8,9,10]
low = a[0]
for i in range(0,len(a)):
    if a[i] > low:
        low = a[i]
print(low)


"""Бинарный поиск числа в сортированном массиве"""
x = 49
b = [1,5,3,7,48,49,3,4,5,99,0,2]
l = 0
h = len(b) - 1
mid = len(b) // 2
while b[mid] != x and l <= h:
    if x > b[mid]:
        l = mid + 1
    else:
        h = mid - 1
    mid = (l + h) // 2
if l > h:
    print(False)
else:
    print("ID=", mid)








