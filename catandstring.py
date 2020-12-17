s = input()
s.split()
counter = 0

for i in range(len(s) - 1):
    if s[i + 1] == s[i]:
        counter += 1

print(counter)