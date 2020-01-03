def solution(n):
    num_str = str(n)
    count = 0
    for digit in num_str:
        if int(digit) == 0:
            continue
        elif int(num_str) % int(digit) == 0:
            count = count + 1
    return count