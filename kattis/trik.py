# https://open.kattis.com/problems/trik
moves = input("Write down Borko's cup moves:")
position = 1
for i in range(len(moves)):
    if moves[i] == "A" and position == 1:
        position = 2
    if moves[i] == "A" and position == 2:
        position = 1
    if moves[i] == "B" and position == 2:
        position = 3
    if moves[i] == "B" and position == 3:
        position = 2
    if moves[i] == "C" and position == 1:
        position = 3
    if moves[i] == "C" and position == 3:
        position = 1
print(position)