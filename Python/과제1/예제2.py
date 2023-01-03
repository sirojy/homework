# 비교 연산자

a = 1
b = 1
print(a < b) # False

# 비교 연산자

a = bool("")
b = False
print(a == b) # True

# 비교 연산자/ 조건문

a = 1
result = ""
if a == 1:
    result = True
else:
    result = False

print(result) # True

# 비교 연산자/ 조건문

a = 90

if a == 90:
    a = a + 10

elif a == 100:
    a = a + 10

elif a ==110:
    a = a + 10

else:
    a = a + 10

print(a) # 100

# 리스트 반복문

string = "hello world!"

for element in string:
    print(element) # 
"""
h
e
l
l
o

w
o
r
l
d
!
"""

# 리스트 반복문

list_variable = [0, 1, 2, 3, 4, 5, 6]

for element in list_variable:
    print(element, end=" ")

"""
0 1 2 3 4 5 6
"""
# range 반복문

n = 10

for element in range(-n, n):
    print(element, end=" ")

"""
?
"""


# range 반복문

n = 10
for element in range (1, n + 1, 3):
    print(element, end=" ")


# 리스트 반복문

list_variable = [6, 5, 4, 3, 2, 1, 0]
for index, element in enumerate(list_variable):
    print(index, element)

# enumerate

# 조건문 range 반복문

n = 10

for element in range(n, -n, -1):
    print(element, end=" ")
    if n < 0:
        break


# 조건문 리스트 반복문

list_variable = [ -1, 3, 5, -2, 1, 9, 21, -3, -5]

for element in list_variable:
    if element < 0:
        continue

    print(element, end=" ")


# range 중첩 반복문

N = 3
M = 4

for n in range(N):
    for m in range(M):
        print(f"{n},{m}")
        



