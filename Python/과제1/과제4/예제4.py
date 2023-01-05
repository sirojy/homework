# 예제 1
# 딕셔너리 코드

dict_variable = {}
dict_variable["이름"] = "정우영"
dict_variable["생년월일"] = "19000101"
dict_variable["회사"] = "하이퍼그로스"

print(dict_variable["이름"]) #  정우영
print(dict_variable["생년월일"]) #  19000101
print(dict_variable["회사"]) #  하이퍼그로스

# 예제 2
# 딕셔너리 코드

dict_variable = {"a": "A", "B": "b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"

print(dict_variable["a"]) # A
print(dict_variable["D"]) # d
print(dict_variable["B"]) # b


# 예제 3
# 딕셔너리 코드
dict_variable = {}
dict_variable["apple"] = 5000
dict_variable["banana"] = 3000
dict_variable["apple"] = 2000
dict_variable["banana"] = dict_variable["banana"] + 1000

print(dict_variable["apple"] + dict_variable["banana"]) # 6000


# 예제 4 
# 딕셔너리 반복문 코드

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key in dict_variable:
    print(key, dict_variable[key])

"""
이름 정우영
생년월일 19000101
회사 하이퍼그로스
"""


# 예제 5
# 딕셔너리 반복문 코드

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key, value in dict_variable.items():
    print(key, value)

"""
이름 정우영
생년월일 19000101
회사 하이퍼그로스
"""

# 예제 6
# 딕셔너리 코드

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

print("나이" in dict_variable) # False

# 예제 7
# 딕셔너리 조건문 코드

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

if "거주지" not in dict_variable:
    dict_variable["거주지"] = "서울특별시"
    # 위 조건문의 조건식이 무엇을 의미하는지 작성하세요.
    # ?
    
print(dict_variable) 
# {'이름': '정우영', '생년월일': '19000101', '회사': '하이퍼그로스', '거주지': '서울 특별시'}


# 예제 8
# 에러가 발생한 원인을 작성하세요.
# 리스트 예외처리 코드

list_variable = []

try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
에러가 발생했습니다.
에러의 원인은 무엇인가요?
"""

# 예제 9
# 에러가 발생한 원인을 작성하세요.
# 코드

try:
    number = 1
    if number == 1:
        print(number)
    
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
에러가 발생했습니다.
에러의 원인은 무엇인가요?

""" 

# 예제 10
# 리스트 조건문 코드

n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2
    elif number % 2 == 1:
        total += number + 1 * 3

print(total) # ?

n = 10
total = 0

for number in range(0, n + 1): # 0 ~ 11
    if number % 2 == 0: # 짝수 2 4 6 8 10
        total += number * 2 # 4 8 12 16 20 
    elif number % 2 == 1: # 홀수 1 3 5 7 9 
        total += number + 1 * 3 # 6 12 18 24 30

print(total) # 100