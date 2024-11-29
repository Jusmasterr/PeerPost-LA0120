import socket
import socket

HOST = "0.0.0.0"  # Server akzeptiert Verbindungen von allen IPs
PORT = 5001       # Port für die Dateiübertragung

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server läuft auf {HOST}:{PORT} und wartet auf Verbindungen...")
        
        conn, addr = server_socket.accept()
        print(f"Verbindung hergestellt mit {addr}")
        
        # Dateiname und Dateigröße empfangen
        file_name = conn.recv(100).decode().strip()  # Erst 100 Bytes für den Dateinamen
        file_size = int(conn.recv(10).decode().strip())  # Dann 10 Bytes für die Dateigröße
        print(f"Empfange Datei: {file_name} ({file_size} Bytes)")
        
        # Datei empfangen
        with open(file_name, "wb") as file:
            received_data = 0
            while received_data < file_size:
                data = conn.recv(1024)
                file.write(data)
                received_data += len(data)
        
        print(f"Datei {file_name} erfolgreich empfangen.")
        conn.close()

if __name__ == "__main__":
    start_server()
