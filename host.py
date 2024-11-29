import socket
import os

def start_listener_peer(host='10.1.21.77', port=80):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        
        try:
            while True:
                header = conn.recv(10).decode().strip()
                if not header:
                    break

                if header == "FILE":   
                    file_name = conn.recv(100).decode().strip()
                    file_size = int(conn.recv(10).decode().strip())
                    print(f"Receiving file: {file_name} ({file_size} bytes)")

                    # Datei speichern
                    with open(file_name, "wb") as file:
                        received_data = 0
                        while received_data < file_size:
                            data = conn.recv(1024)
                            if not data:
                                break
                            file.write(data)
                            received_data += len(data)

                    print(f"File {file_name} received successfully.")

                elif header == "MSG":  
                    data = conn.recv(1024).decode()
                    if not data:
                        break
                    print(f"Received message from client: {data}")
                    conn.sendall(data.encode())  
        except ConnectionResetError:
            print("Connection closed by client.")
        finally:
            conn.close()

if __name__ == "__main__":
    start_listener_peer()

