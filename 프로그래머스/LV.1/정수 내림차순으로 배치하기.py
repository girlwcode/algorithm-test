"""
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
"""
def solution(n):
    answer = 0
    # 이런식으로 다시 선언해서 int 형으로 변환해주기... 웃기네 참
    n = int(n)
    ls = list(str(n))
    ls.sort(reverse=True)
    # python3 부터 int/long 구분 없이 int로 통합
    answer = int("".join(ls))
        
    return answer