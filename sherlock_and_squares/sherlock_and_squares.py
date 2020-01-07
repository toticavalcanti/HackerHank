import math 

def squares(a, b):
    count = math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1))
    return count

q = int(input())

for q_itr in range(q):
    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    result = squares(a, b)

    print(result)
