if __name__ == "__main__":
    dic = {}
    n = int(input().strip())
    for i in range(n):
        key, value = input().split(' ')
        dic[key] = value
    for i in range(n, ):
        line = input().split()
        if line == '':
            break 
        if line[0] in dic:
            print(line[0] + "=" + dic[line[0]])
        else:
            print('Not found')