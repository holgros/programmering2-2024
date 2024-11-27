# Läs in talet, beräkna siffersumma och sök i loop

def siffersumma(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

n = input("N ? ")
summa = siffersumma(n)
digits = len(n)
lo = 10**(len(n)-1)
hi = 10**len(n)-1
i = lo
while i >= lo and i <= hi:
    if siffersumma(i) == summa:
        lo = i
        break
    i += 1
i = hi
while i >= lo and i <= hi:
    if siffersumma(i) == summa:
        hi = i
        break
    i -= 1
print("Svar: " + str(lo) + " " + str(hi))