n = int(input())

days = [int(x) for x in input().split()]
good_days = []

for i in range(len(days)):
    if days[i] > 0:
        good_days.append(str(i+1))

print(' '.join(good_days))