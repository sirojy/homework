word = 'banana'

# break : 반복 종료
for char in word:
    if char == 'a':
        print(1)
        breakpoint


print('===========')

# a를 제외하고 모두 출력
# continue : 다음 반복을 실행
for char in word:
    if char == 'a':
        continue
    print(char, end='')

