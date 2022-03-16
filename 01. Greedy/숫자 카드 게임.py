"""
1. Greedy - 예제 3.3 숫자 카드 게임
여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
출처: 이것이 코딩테스트다_나동빈 96p
"""

n,m = map(int, input("입력: ").split())
max_num = 0

for i in range(n):
    number = list(map(int, input("입력: ").split()))
    min_num = min(number)
    max_num = max(max_num, min_num)
    
print(max_num)
    