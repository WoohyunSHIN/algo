from collections import deque
numbers = [1,1,1,1,1]
target = 3

def solution(numbers:list, target:int)->int:
    answer = 0
    
    answer_tree = [0]
    queue = deque(numbers)

    while queue:
        print(f"queue : {queue} , answer_tree : {answer_tree}")
        num = queue.pop()
        node_list = []
        for idx in range(len(answer_tree)):
            node_list.append(answer_tree[idx] + num)
            node_list.append(answer_tree[idx] - num)
        answer_tree = node_list        
        #print(answer_tree)
        print('----DONE----')
    answer = answer_tree.count(target)


    return answer

print(solution(numbers,target))