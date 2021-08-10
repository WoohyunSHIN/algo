A = input()
B = input()

def main(A:str, B:str)->int: 
    ret = 0
    
    # Insert, Remove
    ret += abs(len(A) - len(B))
    
    # Replace
    replace_diff = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            replace_diff += 1
    print(replace_diff)
    ret = replace_diff - ret
    return ret

print(main(A,B))