# dela upp F i två delar, loopa igenom vardera och sök efter tecken i H
f = input("F ? ")
h = input("H ? ")
f_split = f.split(".")
j = -1
fail = False
# dubbelloop som söker i strängen H efter varje tecken i strängen F
for i in f_split[0]:
    found = False
    while j < len(h)-1:
        j += 1
        if i == h[j]:
            found = True
            break
    if not found:
        fail = True
        break
if not fail:
    # söka igenom textsträngen efter första punkten i återstoden av H
    h = h[j+1::]
    h = h[h.index(".")+1::]
    # samma loop som ovan, kanske går att effektivisera med en funktion...
    j = -1
    for i in f_split[1]:
        found = False
        while j < len(h)-1:
            j += 1
            if i == h[j]:
                found = True
                break
        if not found:
            fail = True
            break
if fail:
    print("Svar: Nej")
else:
    print("Svar: Ja")