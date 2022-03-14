"""
1. Greedy - 예제 3.1 거스름돈
손님에게 거슬러줘야 할 돈이 N원일 때, 거슬러줘야 할 동전의 최소 개수를 구하라.
출처: 이것이 코딩테스트다_나동빈 90p
"""
        
n = 1260
count = 0
    
coin_types = [500, 100, 50, 10]

# 큰 단위의 화폐부터 차례대로 확인

for coin in coin_types:
    count += n // coin
    n %= coin
    
print(count)