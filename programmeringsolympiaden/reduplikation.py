# https://progolymp.se/2024/skolkval/uppgifter24.pdf
ordet = input("Ordet ? ")
antal = int(input("Antal upprepningar ? "))
for i in range(antal):
    print(ordet, end="")
print()

# alternativ lösning på en enda rad
print(input("Ordet ? ")*int(input("Antal upprepningar ? ")))
