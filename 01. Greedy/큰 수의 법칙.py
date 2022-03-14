"""
1. Greedy - 실전문제 큰 수의 법칙
주어진 수(N)들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음

5 8 3
2 4 5 4 6

출처: 이것이 코딩테스트다_나동빈 92p
"""
# N,M,K를 공백으로 구분하여 입력받기
n, m, k = map(int, input('입력:').split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input('입력:').split()))

# 오름차순(작은 수부터)
data.sort()

# 가장 큰 수 곱하는 횟수 == k+1개(반복 수열)로 나눈 몫 * k + 나머지
mult = (m //(k+1)) * k + (m %(k+1))

# 두번째로 큰 수 곱하는 횟수 == m-가장 큰 수 곱하는 횟수
add = m - mult

# 가장 큰 수 = n-1번째, 그 다음으로 큰 수 = n-2번째 
bigestNum = data[n-1] * mult + data[n-2] * add

print(bigestNum)
     