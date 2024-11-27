# loopa igenom alla möjliga operationssekvenser tills N överskrids
n = int(input("N ? "))
m = int(input("M ? "))
nbr_steps = 0
codes = [0]
while max(codes) < n:
    nbr_steps += 1
    temp = []
    for i in codes:
        if i*m <= n:
            temp.append(i*m)
        for k in range(m):
            if i+k <= n:
                temp.append(i+k)
    codes = list(set(temp)) # ta bort dubletter, annars prestandaproblem!
print("Svar: " + str(nbr_steps))