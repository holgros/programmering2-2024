# FLÖDESHANTERING
x = 10
s = "Hej"
if x < 10 or s == "Nej":
    print("Foo")
elif s == "Hej":
    print("Bar")            # Hit går programflödet
else:
    print("Baz")

# FOR-LOOP GENOM OLIKA DATASTRUKTURER (list, set, dictionary)
arr = ["Foo", "Bar", "Baz"]
for i in range(3):
    print(arr[i])
set = {"One", "Two", "Three"}
for i in set:
    print(i)
dic = {"Sverige": "Stockholm", "Norge": "Oslo", "Finland": "Helsingfors"}
for i in dic:
    print("Huvudstaden i", i, "heter", dic[i])

# DEMONSTRATION BREAK OCH CONTINUE
x = 0
while x < 10:
    x += 1
    if x == 2:
        continue
    if x == 5:
        break
    print(x)	# ger utskrift 1 3 4

# DEMONSTRATION UNDANTAGSHANTERING MED TRY-CATCH-ELSE-FINALLY
proceed = True
while proceed:
    try:
        x = input("Ange ett heltal eller acceptera konsekvenserna av felaktig input: ")
        x = int(x)
        proceed = False
    except:
        print("Du måste ange ett heltal!")
    else:
        print("Input OK!")
    finally:
        print("Detta meddelande skrivs ut vad som än händer.")
