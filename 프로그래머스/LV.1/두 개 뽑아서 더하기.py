"""
정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 
solution 함수를 완성해주세요.

제한사항
- numbers의 길이는 2 이상 100 이하입니다.
- numbers의 모든 수는 0 이상 100 이하입니다.
"""

def solution(numbers):
    answer = []
    numbers.sort()
    
    while len(numbers) > 0:
        num = numbers[-1]
        numbers.pop()
        for i in range(len(numbers)):
            add = num + numbers[i]
            if (add not in answer):
                answer.append(add)
                
    answer.sort()
    return answer

# or 그냥 배열에 담고 나중에 set으로 중복 제거하고 sort해줌
def solution(numbers):
    answer = []
    numbers.sort()
    
    while len(numbers) > 0:
        num = numbers[-1]
        numbers.pop()
        for i in range(len(numbers)):
            add = num + numbers[i]
            answer.append(add)
           
    answer = list(set(answer))
    answer.sort()
    return answer