# Klient till den trådade servern
from socket import *
def connect_to_server():    # samma som i tidigare exempel
    s = socket()
    host = input("Ange serverns IP-adress:")
    port = 12345    # Samma som serverns port
    s.connect((host, port))
    return s
conn = connect_to_server()
b = conn.recv(1024)
msg = b.decode('utf-16')
print(msg)
# Skicka meddelande en gång till servern
msg = input("Skriv något till servern:")
b = msg.encode("utf-16")
conn.send(b)
    
while True:
    # ta emot meddelanden från andra klienter i en evig loop
    b = conn.recv(1024)
    msg = b.decode("utf-16")
    print(msg)
