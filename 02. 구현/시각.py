"""
2. 구현 - 예제 4.2 시각
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 
모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하시오

출처: 이것이 코딩테스트다_나동빈 113p
"""

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if str(3) in str(i)+str(j)+str(k):
                count += 1

print(count)