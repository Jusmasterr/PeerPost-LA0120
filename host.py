import socket

def start_listener_peer(host='10.1.21.77', port=80):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    # Start listening for incoming connections
    server_socket.listen(1)
    print(f"Listening on {host}:{port}")

    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Receive data from the client
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received from client: {data.decode()}")
            # Echo the data back to the client
            conn.sendall(data)
    except ConnectionResetError:
        print("Connection closed by client.")
    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    start_listener_peer()
