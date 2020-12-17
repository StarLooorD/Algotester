commands = input()
sx, sy = map(int, input().split())
r = 0
u = 0

for elem in commands:
    if elem == 'R':
        r += 1
    else:
        u += 1
        
if sx <= r and sy <= u:
    print('YES')
else:
    print('NO')
