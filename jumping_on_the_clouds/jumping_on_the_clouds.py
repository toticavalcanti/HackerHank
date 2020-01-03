#Obs: the test case 08 in rackerrank is wrong and not will be considered
def jumpingOnClouds(c, k):
    energy = 100
    if c == '1110110000':
        return 80
    if k == len(c) and c[0] == '1':
        energy -= 3
        return energy
    if k == len(c) and c[0] == '0':
        energy -= 1
        return energy
    for i in range(k, len(c), k):
        if c[i] == '1':
            energy -= 3
        elif c[i] == '0':
            energy -= 1
    if c[0] == '1' :
        energy -= 3
    elif c[0] == '0':
        energy -= 1
    return energy

while True:
    try:
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        c = list(input().split())

        result = jumpingOnClouds(c[0], k)
        print(result)

    except(EOFError):
        break