# # 문제1

# # 정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요.
# # 두 정수가 같으면 False를 출력하세요.

# a = int(input('첫번째 정수를 입력하세요 >")'))
# b = int(input('두번째 정수를 입력하세요 >")'))
# if a > b:
#     print(a)

# elif a < b :
#     print(b)

# else:
#     a = b
#     print("False")


# # 문제2
# # 정수 한 개를 입력 받고,
# # 해당 정수가 1 보다 크고, 10보다 작다면 True
# # 아니면 False를 출력하세요.

# number = int(input("정수를 입력하세요 >"))

# if number > 1:
#     if number < 10 :
#         print("True")
 
# else:
#     number > 10
#     print("False")


# # 문제3
# # 정수 한 개를 입력 받고 0 보다 크고, 짝수라면 True
# # 아니면 False를 출력하세요.

# number = int(input("정수를 입력하세요 >"))

# if number > 0:
#     if number%2 == 0:
#         print("True")
# else:
#     print("False")


# 문제4
# 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.
# 값이 100 초과 / 0 미만이면 "에러" 출력
# 값이 60 이상이면 "합격" 출력
# 값이 60 미만이면 "불합격" 출력

# n = int(input("정수를 입력하세요 >"))

# if n > 100:
#     print("에러")
# elif n < 0:
#     print("에러")
# elif n >= 60:
#     print("합격")
# elif n < 60:
#     print("불합격")



# 문제5
# 문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.
# 힌트 : 문자열 역슬라이싱

s1 = input("문자열을 입력하세요>")

for s1 in s1:
    print(s1)



# 문제6
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.
# 두 값이 같으면 False를 출력하세요

a = int(input("첫 번째 정수를 입력하세요"))
b = int(input("두 번째 정수를 입력하세요"))

print(list(range(b + 1, a)))

if a == b:
    print("False")


# 문제7
# 정수 두 개를 입력 받고, 
# 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.
# 두 값이 같으면 False를 출력하세요








    







