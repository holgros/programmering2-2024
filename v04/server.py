from socket import *
def start_server():
    s = socket()            # Skapa ett socket-objekt
    host = "localhost"      # som körs på den egna datorn
    port = 12345            # på port 12345.
    s.bind((host, port))    # Konfigurera socket-objektet.
    s.listen()              # Vänta på att klient ansluter.
    return s
s = start_server()
print("Servern är igång på port 12345! Väntar på att en klient ska ansluta...")
conn, addr = s.accept()     # När en klient ansluter
print("En klient anslöt från adressen", addr)
conn.close()