# 예제1
# 리스트 반복문

list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
list_variable.append(7)
list_variable.append(8)

for element in list_variable[2:]:
    print(element, end=" ")  # 2 3 4 5 7 8 


# 예제2
# range 반복문

for element in range(-2, 10, 2):
    print(element, end=" ") # -2, 0, 2, 4, 6, 8


# 예제3

# 조건문 반복문

a, b, c, d = 0, 0, 0, 0
n = 10 # 0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10

for number in range(n):
    if number % 2 == 0: # 2,4,6,8,10
        a = a + 1 # 3, 5, 7, 9, 11

    if number % 3 == 0: # 3, 6 , 9
        b = b + 1

    if number % 4 == 0:
        c = c + 1

    if number % 5 == 0:
        d = d + 1

print(a, b, c, d) # 5 4 3 2


# 예제 4
# 비교 연산자 반복문

i = 0
while i <= 10:
    print(i) 
    i = i + 1
"""
0
1
2
3
4
5
6
7
8
9
10
""" 

# 예제 5
# 비교 연산자 반복문
i = 0
while i <= 10:
    i = i + 1
    print(i)


# 예제 6

# 조건문 반복문

i = 0
while i <= 10:
    i = i + 2 
    print(i)

"""
2
4
6
8
10
12
"""


# 예제 7
# 조건문 반복문

i = 0
while True:
    print(i)
    i = i + 1
    if i > 10:
        break
"""
0
1
2
3
4
5
6
7
8
9
10
"""

# 예제 8
# 조건문 반복문
i = 0
while True:
    print(i)
    if i > 10: # 0 1 2 3 4 5 6 7 8 9 10 11
        break
    i = i + 1

"""
1
1
2
3
4
5
6
7
8
9
10
11
"""
    
# 예제 9
# 함수

list_variable = [ 0,1, 2, 3, 4, 5, 6]
print(len(list_variable)) # 7


# 예제 10
# 함수

list_variable = [0, 1, 2, 3, 4, 5, 6]
print(sum(list_variable)) # 21


# 예제 11
# 함수

list_variable = [3, 1, 4, -3, 9, 7]
print(min(list_variable) - max(list_variable)) # -12