# Sikta konsekvent på ett monster med maximalt antal liv
nsa = input("N, S, A ? ").split(" ")
for i in range(len(nsa)):
    nsa[i] = int(nsa[i])
lives = input("Monstrens liv ? ").split(" ")
for i in range(len(lives)):
    lives[i] = int(lives[i])
shots = 0
max_lives = max(lives)
while max_lives > 0:
    shots += 1
    aim = 0
    for i in range(len(lives)):
        if lives[i] == max_lives:
            aim = i
            lives[i] -= (nsa[1] + nsa[2])
            break
    for i in range(len(lives)):
        if i != aim:
            lives[i] -= nsa[2]
    lives = [x for x in lives if not x < 1] # rensa bort döda monster från listan
    if len(lives) == 0:
        max_lives = 0
    else:
        max_lives = max(lives)
print("Svar: " + str(shots))