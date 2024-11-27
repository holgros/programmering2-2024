# Inte särskilt svår, behövs inte ens någon loop
vinkel1 = int(input("Vinkel 1 ? "))
vinkel2 = int(input("Vinkel 2 ? "))
vinkel3 = int(input("Vinkel 3 ? "))
if vinkel1 > 90 or vinkel2 > 90 or vinkel3 > 90:
    print("Svar: Trubbig Triangel")
elif vinkel1 == 90 or vinkel2 == 90 or vinkel3 == 90:
    print("Svar: Rätvinklig Triangel")
else:
    print("Svar: Spetsig Triangel")
