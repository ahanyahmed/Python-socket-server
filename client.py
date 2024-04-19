import socket

# Define the server address and port
SERVER_HOST = "localhost" 
SERVER_PORT = 8080    

def send_message(message):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Connect to the server
            s.connect((SERVER_HOST, SERVER_PORT))
            
            # Send the message to the server
            s.sendall(message.encode())

            # Receive the server's response
            response = s.recv(1024).decode()
            print("Server response:", response)

        except ConnectionRefusedError:
            print("Connection to the server failed.")

if __name__ == "__main__":
    messages = [
        "Wpython Socket Server",
        "LpythonSocketServer",
        "UPYTHONSOCKETSERVER",
        "R1234567890",
        "TpythonSocketServer123",
        "pythonSocketServer123"
    ]

    for msg in messages:
        print("Sending message:", msg)
        send_message(msg)
