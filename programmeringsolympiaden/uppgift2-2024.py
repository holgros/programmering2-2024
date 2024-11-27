# Loopa igenom textsträngen, räkna poäng för vardera spelaren och avgör sedan aktuell ställning
anteckningar = input("Anteckningarna ? ")
truls = 0
henry = 0
for i in anteckningar:
    if i == "T":
        truls += 1
    else:
        henry += 1
    if (truls > 10 and truls-henry > 1) or (henry > 10 and henry-truls > 1):
        truls = 0
        henry = 0
print(str(truls) + "-" + str(henry))
