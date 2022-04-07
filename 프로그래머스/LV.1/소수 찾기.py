"""
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
"""
# 에라토스테네스의 체
def solution(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    #2부터 n까지 검사
    for i in range(2,n+1):
        if a[i]:
        #리스트의 요소가 True 값인 수를 primes에 추가한다.
            primes.append(i)
            #2의 배수, 3의 배수, ... 100의 배수에 해당하는 100이하의 양의 정수를 False로 바꾼다.
            for j in range(2*i, n+1, i):
                a[j] = False
    answer = len(primes)
    return answer