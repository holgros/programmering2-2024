'''
En enkel chattklient med grafiskt gränssnitt.
Starta servern först, sedan klienten och ange IP-adressen.
Avsluta genom att stänga fönstret.
Begränsningar: Servern kan bara låta en enda klient ansluta. När klienten kopplats ifrån så kan den inte ansluta igen.
'''
import tkinter as tk
from socket import *
from threading import Thread

def connect_to_server():
    s = socket()
    host = input("Ange serverns IP-adress:")
    port = 12345
    s.connect((host, port))
    return s

def start_client_gui():
    def send_message():
        msg = input_field.get()
        if msg:
            b = msg.encode("utf-16")
            s.send(b)
            chat_box.insert(tk.END, f"Du: {msg}\n")
            input_field.delete(0, tk.END)

    def receive_message():
        while True:
            try:
                b = s.recv(1024)
                msg = b.decode("utf-16")
                chat_box.insert(tk.END, f"Servern: {msg}\n")
            except:
                break

    s = connect_to_server()

    root = tk.Tk()
    root.title("Klient")

    chat_box = tk.Text(root, state="normal", height=15, width=50)
    chat_box.pack(pady=10)

    input_field = tk.Entry(root, width=40)
    input_field.pack(side="left", padx=5)

    send_button = tk.Button(root, text="Skicka", command=send_message)
    send_button.pack(side="right", padx=5)

    Thread(target=receive_message, daemon=True).start()

    root.mainloop()

start_client_gui()