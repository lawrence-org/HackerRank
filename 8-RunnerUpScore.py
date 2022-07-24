if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    a = list(set(arr))
    b = sorted(a)
    print(b[-2])

    #assets/8-RunnerUpScore/2022-07-24-13-43-39.png