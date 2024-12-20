import socket
import os
from tkinter import Tk, filedialog

def send_file(client_socket):
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename()
    if not file_path:
        print("No file selected.")
        return

    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    client_socket.sendall(f"FILE".ljust(10).encode())
    client_socket.sendall(f"{file_name:<100}".encode())
    client_socket.sendall(f"{file_size:<10}".encode())

    with open(file_path, "rb") as file:
        while (data := file.read(1024)):
            client_socket.sendall(data)

    print(f"File {file_name} sent successfully.")

def send_message(client_socket):
    message = input("Enter message to send (or 'exit' to quit): ")
    if message.lower() == 'exit':
        return False
    client_socket.sendall(f"MSG".ljust(10).encode()) 
    client_socket.sendall(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")
    return True

def start_connector_peer(host='localhost', port=8081):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")
    except ConnectionRefusedError:
        print("Connection failed. Is the listener peer running?")
        return

    try:
        while True:
            print("\nOptions:")
            print("1. Send a file")
            print("2. Send a message")
            print("3. Exit")
            option = input("Choose an option: ")

            if option == "1":
                send_file(client_socket)
            elif option == "2":
                if not send_message(client_socket):
                    break
            elif option == "3":
                print("Closing connection.")
                break
            else:
                print("Invalid option. Please try again.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_connector_peer()

