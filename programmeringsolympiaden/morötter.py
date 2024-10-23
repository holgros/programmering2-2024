# https://progolymp.se/2023/skolkval/kval23.pdf

# input och startvärden
tor = int(input("Tors tid ? "))
tor_remaining = tor
tor_carrots = 1 # Tor tar omedelbart en morot
mor = int(input("Mors tid ? "))
mor_remaining = mor
mor_carrots = 1 # Mor tar omedelbart en morot

# loopa igenom så länge det finns morötter
carrots = 38    # båda tar omedelbart en morot var (40-2=38)
while carrots > 1:
    tor_remaining -= 1
    mor_remaining -= 1
    if tor_remaining == 0:
        tor_carrots += 1
        tor_remaining = tor
        carrots -= 1
    if mor_remaining == 0:
        mor_carrots += 1
        mor_remaining = mor
        carrots -= 1

# vem tar sista moroten?
if carrots == 1:
    if tor_remaining < mor_remaining:
        tor_carrots += 1
    if mor_remaining < tor_remaining:
        mor_carrots += 1

# skriv ut
print("Svar: Tor", tor_carrots, ", Mor ", mor_carrots)