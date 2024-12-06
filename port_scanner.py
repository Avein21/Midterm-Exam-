# Import all require module
import socket
from datetime import datetime 

# Enter Host address to scan for ports
host_address = input("Enter the target host address to scan: ")

# translate a host name to ipv4 address format
ip_addr = socket.gethostbyname(host_address)

# Add while loop to make sure starting loop is lower than the ending port
while True:
    # Adding error handling try block 
    try:
        initial_port = int(input("Enter the starting port number (1-65535): "))
        final_port = int(input("Enter the ending port number (1-65535): "))
        
        # Ensure the port numbers are within the valid range
        if not (1 <= initial_port <= 65535 and 1 <= final_port <= 65535):
            print("Port numbers must be between 1 and 65535.")
            continue
    
        # Using if statement to ensure that the starting port is lower than the ending port
        if initial_port > final_port:
            print("The starting port must be smaller than the ending port.")
            continue
        break
    except ValueError:
        print("Please enter valid port numbers. ")
    
# These three lines are just added for messages that it is scanning the host
print("-" * 80)
print(f"          Please wait, Scanning The Host ---------> {host_address}")
print("-" * 80)

# starting time to be recorded
start_time = datetime.now()

# Start of the code for port scanning
# Use for statement to loop through the range of ports
for port in range(initial_port, final_port + 1):
    # Create a new socket connection for each port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((host_address, port))
    # Check if the port is open (result == 0 means the connection was successful)
    if result == 0:
        # If a socket is listening it will print out the port number
        print(f"Port number {port} is OPEN")
    else:
        print(f"Port number {port} is CLOSED")

    # Close the socket connection
    sock.close()

# Calculate and print the total scan time
end_time = datetime.now()
total_time = end_time - start_time
print(f"Total Scanning Time:  {total_time}")

# Timestamp 
current_timestamp = datetime.now()
print(current_timestamp)