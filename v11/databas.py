"""
Innan du kör koden, skapa en tabell med följande kommando:
CREATE TABLE Elever (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Autoinkrementerande primärnyckel
    fornamn VARCHAR(50) NOT NULL,       -- Förnamn, max 50 tecken
    efternamn VARCHAR(50) NOT NULL,    -- Efternamn, max 50 tecken
    klass VARCHAR(10) NOT NULL         -- Klass, max 10 tecken
);
"""

import mysql.connector  # installera med "pip install mysql-connector-python" i kommandotolken
mydb = mysql.connector.connect(
  host="localhost",
  user="root",  # standardanvändarnamn för XAMPP
  password="",  # dito lösenord (en tom sträng)
  database="Prog2"  # byt namn om din databas heter något annat
)
mycursor = mydb.cursor()
print("Uppkopplad till databasen!")

# Skriva till databasen
sql = "INSERT INTO Elever (fornamn, efternamn, klass) VALUES (%s, %s, %s)"
val = ("Terry", "Jones", "TE19C")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Läsa från databasen
mycursor.execute("SELECT * FROM Elever")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

