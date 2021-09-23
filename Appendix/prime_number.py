import math

def is_prime_number(x:int)->bool:
    ret = True
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i == 0:
            ret = False
            break
    return ret

print(is_prime_number(5))

def Sieve_of_Eratosthenes(x:int)->list:
    array = [True for _ in range(x+1)]
    array[0] = False
    array[1] = False

    for i in range(2, int(math.sqrt(x))+1):
        if array[i] == True:
            j = 2
            while i * j <= x:
                array[i*j] = False
                j += 1

    return array
    
only_prime_nums = Sieve_of_Eratosthenes(100)

for i in range(len(only_prime_nums)):
    if only_prime_nums[i] == True:
        print(i)
