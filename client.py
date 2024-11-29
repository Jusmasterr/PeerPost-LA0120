import socket
import os
from tkinter import Tk, filedialog

# Server-Konfiguration
SERVER_HOST = "127.0.0.1"  # IP des Servers
SERVER_PORT = 5001         # Port des Servers

def send_file(file_path):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"Verbunden mit {SERVER_HOST}:{SERVER_PORT}")
        
        # Dateiinfo senden
        client_socket.send(file_name.encode())
        client_socket.send(str(file_size).encode())
        
        # Datei senden
        with open(file_path, "rb") as file:
            while (data := file.read(1024)):
                client_socket.send(data)
        
        print(f"Datei {file_name} erfolgreich gesendet.")

def select_file_and_send():
    # Datei-Auswahl GUI
    root = Tk()
    root.withdraw()  # Hauptfenster verstecken
    file_path = filedialog.askopenfilename()
    if file_path:
        send_file(file_path)

if __name__ == "__main__":
    select_file_and_send()
