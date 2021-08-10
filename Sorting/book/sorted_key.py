"""
sorted() 나 sort()를 이요할 때에는 key 매개변수를 입력받을 수 있다.
"""

array = [('바나나',2),('사과',5),('당근',3)]

def setting(data:tuple)->int:
    return data[1]

result = sorted(array, key=setting)
print(result)