import socket
import os
from tkinter import Tk, filedialog

SERVER_HOST = "127.0.0.1"  # IP des Servers
SERVER_PORT = 5001         # Port des Servers

def send_file(file_path):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"Verbunden mit {SERVER_HOST}:{SERVER_PORT}")
        
        # Dateiinfo senden (100 Byte für Dateiname, 10 Byte für Dateigröße)
        client_socket.send(f"{file_name:<100}".encode())  # Name auf 100 Zeichen auffüllen
        client_socket.send(f"{file_size:<10}".encode())  # Größe auf 10 Zeichen auffüllen
        
        # Datei senden
        with open(file_path, "rb") as file:
            while (data := file.read(1024)):
                client_socket.send(data)
        
        print(f"Datei {file_name} erfolgreich gesendet.")

def select_file_and_send():
    root = Tk()
    root.withdraw()  # Hauptfenster verstecken
    file_path = filedialog.askopenfilename()
    if file_path:
        send_file(file_path)

if __name__ == "__main__":
    select_file_and_send()

