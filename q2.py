for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = sum(a)
    c = 0
    for t in a:
        if not t:
            c += t
            print(c)
    if k < 100:
        print('NO')
    elif k == 10:
        print('YES')
    else:
        if k > 101:
            print('NO')
        else:
            print('YES')
