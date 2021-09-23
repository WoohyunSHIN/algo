from itertools import permutations

data = ['A','B','C']

# 1. PERMUTATIONS
# iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산.
# ['A','B','C'] 에서 3개를 뽑아 나열하는 "모든 경우"
print("1.1. ",list(permutations(data,3)))

# ['A','B','C'] 에서 2개를 뽑아 나열하는 "모든 경우"
print("1.2. ",list(permutations(data,2)))

from itertools import combinations
# 2. COMBINATIONS
# iterable 객체에서 r개의 데이터를 뽑아 "순서를 고려하지 않고" 나열하는 모든 경우를 계산
# ['A','B','C'] 에서 2개를 뽑아 "순서에 상관 없이" 나열하는 모든 경우
print("2.1.",list(combinations(data,2)))

from itertools import product
# 3. PRODUCT >> PERMUTATIONS
# iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산, "다만 원소를 중복하여 뽑는다"
# ['A','B','C'] 에서 "중복을 포함하여" 2개를 뽑아 나열하는 모든 경우
print("3.1.",list(product(data,repeat=2)))

from itertools import combinations_with_replacement
# 4. COMBINATIONS_WITH_REPLACEMENT
# iterable 객체에서 r개의 데이터를 뽑아 "순서를 고려하지 않고" 나열하는 모든 경우를 계산, "다만 원소를 중복으로 뽑는다"
# ['A','B','C'] 에서 "중복을 포함하여" 2개를 뽑아 "순서에 상관 없이" 나열하는 모든 경우
print("4.1.",list(combinations_with_replacement(data,2)))