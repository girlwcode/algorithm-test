"""
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
"""

# 조합은 서로 다른 n개 중에 r개를 선택하는 경우의 수(순서 X) 모듈 combinations import
from itertools import combinations 

# 소수인지 아닌지 판별
def isPrime(num) :
    for i in range (2,num):
        if (num % i == 0):
            return False
    return True

def solution(nums):
    answer = 0
    add = []
    test_list = list(combinations(nums, 3))
    test_list = list(set(test_list))
    
    for i in range(len(test_list)):
        add.append(sum(test_list[i]))
    

    
    for i in range (len(add)):
        if(isPrime(add[i])) :
            answer += 1
        
    return answer