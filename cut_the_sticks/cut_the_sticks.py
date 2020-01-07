def cutTheSticks(arr):
    output = []
    while(arr):
        smaller = min(arr)
        output.append(len(arr))        
        for i in range(len(arr)):
            arr[i] = arr[i] - smaller
        arr = list(filter(lambda a: a != 0, arr))
    return output

while True:
    try:
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = cutTheSticks(arr)
        print('\n'.join(map(str, result)))

    except(EOFError):
        break
