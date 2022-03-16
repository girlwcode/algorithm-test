"""
2. 구현 - 예제 4.1 상하좌우
N*N 크기의 정사각형 공간 위에서 (1,1)에서 시작하여 최종 도착할 좌표 구하기
L, R, U, D
(단, 공간을 벗어나는 움직임은 무시한다.)
출처: 이것이 코딩테스트다_나동빈 110p
"""


from re import X


n = int(input())
rule = list(map(str, input().split()))

# 첫 좌표 선언
x = 1
y = 1
new_pos_x = 1
new_pos_y = 1

for r in rule:
    if (r == 'L'):
        new_pos_y = y - 1
    elif (r == "R"):
        new_pos_y = y + 1
    elif (r == "U"):
        new_pos_x = x - 1
    elif (r == "D"):
        new_pos_x = x + 1
    
    if (new_pos_x < 1 or new_pos_x > n or new_pos_y < 1 or new_pos_y > n): 
        continue
    else:
        x = new_pos_x
        y = new_pos_y

print(x, y)   

"""
모범코드
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for r in rules:
    for i in range(len(move_types)):
        if (r == move_types[i]):
            new_pos_x = x + dx[i]
            new_pos_y = y + dy[i]
        
        if (new_pos_x < 1 or new_pos_x > n or new_pos_y < 1 or new_pos_y > n): 
        continue
        
        x, y = new_pos_x, new_pos_y
        
print(x, y)
"""