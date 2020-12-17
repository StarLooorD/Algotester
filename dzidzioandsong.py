song = input()

new_songs = []

for i in range(len(song)):
    new_songs.append(song[:i] + song[i+1:])

print(len(set(new_songs)))