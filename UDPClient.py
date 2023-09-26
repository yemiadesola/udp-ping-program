import socket
import time

server_address = ('localhost', 12000) # Server address (replace with the actual server's IP address and port)
client_socket = socket.socket(socket.AF_INET, socket. SOCK_DGRAM) # Create a UDP socket
client_socket.settimeout(1.0) # Set a timeout for the socket (1 second)

num_pings = 20 # Number of ping messages to send

for sequence_number in range(1, num_pings + 1):
    send_time = time.time() # Get the current time
    message = f'Ping {sequence_number} {send_time}' # Construct the message to send

    try:
        client_socket.sendto(message.encode(), server_address)  # Send the message to the server
        response, _ = client_socket.recvfrom(1024) # Receive the response from the server

        receive_time = time.time()  # Calculate the round-trip time
        round_trip_time = receive_time - send_time

        # Print the response message and round-trip time
        print(f'SERVER_RESPONSE_MESSAGE: {response.decode()} Round-trip time: {round_trip_time:.6f} seconds')

    except socket.timeout:  #Print "Request timed out" when no packet is received from the server.
        print(f'Ping {sequence_number} Request timed out')

client_socket.close() # Close the socket

