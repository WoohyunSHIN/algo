from itertools import permutations,combinations

L, C = map(int,input().split())
pw = list(map(str,input().split()))
VOWELS = ('a','e','i','o','u')

def main(L:int, C:int, pw:list)->None:

    results = []
    global VOWELS    

    for case in list(combinations(pw,L)):
        for idx in range(L):
            if case[idx] in VOWELS:
                results.append(str.join('',case))
                break

    for result in results:
        print(result) 

main(L,C,sorted(pw))

"""
4 6
a t c i s w
"""