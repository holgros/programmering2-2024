# https://progolymp.se/2023/skolkval/kval23.pdf

# input och startvärden
krypto = input("Kryptosträng ? ")
sequences = [[krypto[0]]]

# loopa
for ch in krypto[1:]:
    if ch == "0":
        for seq in sequences:   # noll kan inte vara första siffran
            seq[-1] += "0"
        continue
    temp = []
    for seq in sequences:
        if seq[-1] == "1" or seq[-1] == "2":    # kan tolkas som antingen tiotalssiffra eller entalssiffra
            my_copy = seq.copy()
            my_copy.append(ch)
            temp.append(my_copy)
            seq[-1] += ch
        else:   # siffra högre än 2
            seq.append(ch)
    sequences = sequences + temp    # tiotalstolkningar plus entalstolkningar

print(len(sequences))

'''
print("Strängarna är: ")
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
for seq in sequences:
    for ch in seq:
        print(key[int(ch)-1], end="")
    print()
'''