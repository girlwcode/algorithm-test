"""
1. Greedy - 예제 3.4 1이 될 때까지
어떠한 수 n이 1이 될 때까지 다음의 두 과정 중 한개 선택하여 반복 후 최소 횟수 출력
1. n에서 1을 뺀다.
2. n을 k로 나눈다.
출처: 이것이 코딩테스트다_나동빈 99p
"""

n, k = map(int, input().split())
count = 0


while True:
    # k의 배수로 만들어주기
    target = (n//k) * k
    
    # k의 배수가 될 만큼 빼주기
    count += n - target
    
    # k의 배수일 때, 나누기
    n = target // k
    count +=1 
    
    # k로 나눌 수 없을 때, 반복문 탈출
    if (n < k) : break
       
# 1이 될 때까지 빼주기
count += n - 1
    
print(count)

