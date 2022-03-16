"""
2. 구현 - 예제 4.3 왕실의 나이트
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로 나갈 수 없음
이동 경우의 수를 출력하시오

Rule
1. 수평으로 두 칸 이동한 뒤에 수직으로 한칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수직으로 한칸 이동하기

출처: 이것이 코딩테스트다_나동빈 115p
"""

first = list(input(str()))
x = ord(first[0])
y = ord(first[1])


dx1 = [2, -2]
dy1 = [1, -1]

dx2 = [1, -1]
dy2 = [2, -2]


count = 0

for i in range(len(dx1)):
    for j in range(len(dy1)):
        new_x = x + dx1[i]
        new_y = y + dy1[j]
        
        if (new_x > ord('h') or new_x < ord('a') or new_y < ord('1') or new_y > ord('8')):
            continue
        count += 1


for i in range(len(dx2)):
    for j in range(len(dy2)):
        new_x = x + dx2[i]
        new_y = y + dy2[j]
    
        if (new_x > ord('h') or new_x < ord('a') or new_y < ord('1') or new_y > ord('8')):
            continue
        count += 1

print(count)