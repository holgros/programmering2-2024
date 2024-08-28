# GOOGOL - öva heltalsoperationer och typning
googol = 10**100
googol_hours = googol // 60     # Hur många hela timmar är en googol minuter?
googol_minutes = googol % 60    # Hur många minuter återstår?
time = input("Vad är klockan nu? (Ange på formatet hh:mm)")
hours, minutes = time.split(":")
hours = int(hours)              # typa från str till int
minutes = int(minutes)          #dito
minutes += googol_minutes
if minutes >= 60:               # en timme har 60 minuter
    hours += 1
    minutes -= 60
hours += googol_hours
hours %= 24                     # ett dygn har 24 timmar
time_string = str(hours) + ":" + str(minutes)
print("Om en googol minuter är klockan", time_string)