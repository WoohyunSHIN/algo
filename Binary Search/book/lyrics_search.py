from sys import stdin
from bisect import bisect_left, bisect_right
from collections import defaultdict

words = list(map(str,stdin.readline().split()))
queries = list(map(str,stdin.readline().split()))
words_length_dict = {}

def count_by_range(a:list, left_value:str, right_value:str)->int:
    a = sorted(a)

    left = bisect_left(a,left_value)
    right = bisect_right(a,right_value)

    return right-left

def solution(words:list, queries:list)->list:
    answer = []

    words_length_dict = defaultdict(list)
    reversed_words_length_dict = defaultdict(list)

    for word in words:
        words_length_dict[len(word)].append(word)
        reversed_words_length_dict[len(word)].append(word[::-1])

    for query in queries:
        if query[0] != '?':
            ans = count_by_range(words_length_dict[len(query)],query.replace('?','a'),query.replace('?','z'))
            answer.append(ans)
        else:
            ans = count_by_range(reversed_words_length_dict[len(query)],query[::-1].replace('?','a'),query[::-1].replace('?','z'))
            answer.append(ans)
        
    return answer

print(solution(words,queries))

"""
frodo front frost frozen frame kakao
fro?? ????o fr??? fro??? pro?
ans = [3, 2, 4, 1, 0]
"""