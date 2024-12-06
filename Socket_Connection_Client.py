# Import all require module
import socket
from datetime import datetime 

# Constant
# Local Host
HOST = '127.0.0.1' 
# Port number to bind
PORT = 65432

# Create a server connection socket
client_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Adding error handling try block
try:
    # Connect to the server
    client_conn.connect((HOST, PORT))
    print(f"Connected to server at {HOST}: {PORT}")

    # Send a message to the server
    message = "Hello, server! This is the client"
    client_conn.sendall(message.encode())
    print(f"Sent message: {message}")

    # Receive the response from the server
    data = client_conn.recv(1024)
    print(f"Received from server: {data.decode()}")

except Exception as e:
    print(f"Error communicating with the server: {e}")

finally:
    # close the client socket connection
    client_conn.close()
    print("Connection closed")

    # Timestamp 
current_timestamp = datetime.now()
print(current_timestamp)
