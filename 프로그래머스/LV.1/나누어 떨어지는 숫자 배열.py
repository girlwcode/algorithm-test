def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if(arr[i] % divisor == 0):
            answer.append(arr[i])
    # not [list] 는 문자열이 빈것이면 true 반환       
    if(not answer): answer.append(-1)
    answer.sort()
    return answer