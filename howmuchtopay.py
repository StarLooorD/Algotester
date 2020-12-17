a, b = map(int, input().split())

if a - b != 1 and b - a != 1:
    if a > b:
        print(b+1)
    else:
        print(a+1)
else:
    print(-1)
