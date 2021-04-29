data = input().rstrip('\n')

def _compressor(size:int, data:str)->int:
    ret = 0
    string = ''
    cnt = 1

    start_idx = 0
    end_idx = size

    while True:
        if data[start_idx:end_idx] == data[end_idx:end_idx+size]:
            cnt += 1
            start_idx = end_idx
            end_idx = end_idx + size
        else:
            if cnt == 1:
                string += data[start_idx:end_idx]
                start_idx = end_idx
                end_idx = end_idx + size
            
            else:
                string += str(cnt) + data[start_idx:end_idx]
                start_idx = end_idx
                end_idx = end_idx + size
                cnt = 1
        
        # base case
        if end_idx >= len(data):
            if cnt == 1:
                string += data[start_idx:end_idx]
            else:
                string += (str(cnt)+data[start_idx:end_idx])
            break 

    ret = len(string)
    return ret


def solution(s:str)->int:
    answer = len(s)
    for size in range(1,(len(s)//2)+1):
        answer = min(answer,_compressor(size,s))
    return answer

print(solution(data))