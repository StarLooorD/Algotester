n = input()

counter = 0

for elem in [int(d) for d in str(n)]:
    if elem == 4 or elem == 7:
        counter += 1

print(counter)