import socket

def start_connector_peer(host='localhost', port=5000):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the listener peer
    try:
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")
    except ConnectionRefusedError:
        print("Connection failed. Is the listener peer running?")
        return

    # Send and receive messages
    try:
        while True:
            # Get user input to send
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                print("Closing connection.")
                break
            
            # Send the message
            client_socket.sendall(message.encode())
            # Receive the echoed response
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_connector_peer()
