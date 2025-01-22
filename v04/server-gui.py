'''
En enkel chattklient med grafiskt gränssnitt.
Starta servern först, sedan klienten och ange IP-adressen.
Avsluta genom att stänga fönstret.
Begränsningar: Servern kan bara låta en enda klient ansluta. När klienten kopplats ifrån så kan den inte ansluta igen.
'''
import tkinter as tk
from socket import *
from threading import Thread

def start_server(ip):
    s = socket()
    host = ip
    port = 12345
    s.bind((host, port))
    s.listen()
    return s

def start_server_gui(ip):
    def send_message():
        msg = input_field.get()
        if msg and conn:
            b = msg.encode("utf-16")
            conn.send(b)
            chat_box.insert(tk.END, f"Du: {msg}\n")
            input_field.delete(0, tk.END)

    def handle_client():
        global conn
        conn, addr = s.accept()
        chat_box.insert(tk.END, f"Klient ansluten: {addr}\n")
        while True:
            try:
                b = conn.recv(1024)
                msg = b.decode("utf-16")
                chat_box.insert(tk.END, f"Klienten: {msg}\n")
            except:
                chat_box.insert(tk.END, "Klient frånkopplad\n")
                break

    s = start_server(ip)

    root = tk.Tk()
    root.title("Server")

    chat_box = tk.Text(root, state="normal", height=15, width=50)
    chat_box.pack(pady=10)

    input_field = tk.Entry(root, width=40)
    input_field.pack(side="left", padx=5)

    send_button = tk.Button(root, text="Skicka", command=send_message)
    send_button.pack(side="right", padx=5)

    Thread(target=handle_client, daemon=True).start()

    root.mainloop()

my_ip = input("Ange din IP-adress (antingen 'localhost' eller en adress på det lokala nätverket t.ex. '10.32.42.137'):")
start_server_gui(my_ip)
