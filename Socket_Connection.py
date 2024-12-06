# Import all require module
import socket
from datetime import datetime 

# Constant
# Local Host
HOST = '127.0.0.1' 
# Port number to bind
PORT = 65432
    
# Create a server connection socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Adding error handling try block
try:
    # Bind the socket to the address and port number
    socket_server.bind((HOST, PORT))

    # Enable server to listen or accept connections
    socket_server.listen()
    print(f"The server is listening on {HOST}:{PORT}...")
    
    while True:
         # Accept the connection
        client_conn, client_address = socket_server.accept()
        print(f"Connection established with {client_address}")

        # Add another error handling try block to check if data has been received
        try:
            # Receive data from the client
            data = client_conn.recv(1024)
            if data:
                print(f"Received message from client: {data.decode()}")
                # Send a response back to the client
                client_conn.sendall(b"Hello, client! Your Message has been received.")
        except Exception as e:
            print(f"Error receiving data: {e}")
        finally:
            # Close the client connection
            client_conn.close()
            print(f"Connection with {client_address} closed")

except Exception as e:
    print(f"Error starting the server: {e}")

finally:
    # Ensure the server connection is closed when done
    socket_server.close()

    # Timestamp 
current_timestamp = datetime.now()
print(current_timestamp)