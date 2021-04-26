"""
단순히 input 을 사용하여 값을 전달 받아도 되지만 동작 속도가 느려서 시간 초과로 오답 판정을
받을 수 있기 때문에 파이썬의 경우 sys 라이브러리에 정의 되어있는 함수를 아래와 같이 사용한다.

import sys
data = sys.stdi.readline().rstrip() # .rstrip() = enter 제거용
print(data)
"""