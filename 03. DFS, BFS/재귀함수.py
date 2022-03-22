# def recursive_function():
#     print("재귀 함수를 호출합니다.")
#     recursive_function()

# # "재귀 함수를 호출합니다." 메세지 무한 출력
# recursive_function()

## 재귀함수 종료 예제
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i,"번째 재귀 함수에서", i+1, "번째 재귀함수를 호출합니다")
    recursive_function(i+1)
    print(i,"번째 재귀함수를 종료합니다")

recursive_function(1)

# 반복적으로 구현한 n!
def factorial_interative(n):
    result =1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_reculsive(n):
    if n <= 1:
        return 1
    # n! = n * (n-1)!
    return n * factorial_reculsive(n-1)

print("반복적으로 구현:",factorial_interative(5))
print("재귀적으로 구현:",factorial_reculsive(5))
