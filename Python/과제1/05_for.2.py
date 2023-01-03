a = 'apple'


# 'apple' => 0~4 : len('apple')-1
# 'pineapple' => 0~8 : len('pineapple')-1
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print('===============')

for char in a:
    print(char)

for index in range(5):
    print(a[i])

# 1.
# 반복 가능한객체 : 각 요소가 필요할 때
for char in a:
    print(char)
print('===============')
# 2.
# 반복 가능한 객체: 인덱스가 필요할 때
