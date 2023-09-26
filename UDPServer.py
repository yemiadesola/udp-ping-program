from socket import *
import time
import random

serverSocket = socket(AF_INET, SOCK_DGRAM) # Create a UDP socket
serverSocket.bind(('', 12000)) #Assigning localhost address and port 12000
print("Server listening on PORT 12000") 

drop_prob = 0.4 #setting packet dropping to 40 percent

while True:
    total_packets_received = 0 #initializing total packet received
    total_packets_dropped = 0 #initializing total packet dropped

    while total_packets_received < 20:  
        message, address = serverSocket.recvfrom(1024)  #Receive client packet with the sender address 
        total_packets_received += 1  # Increment the total packets received

        # Extracting the sequence number from the packet sent by client
        try:
            received_sequence_number = int(message.decode().split()[1])
        except (ValueError, IndexError):
            received_sequence_number = -1

        print(f"Received packet {received_sequence_number} from {address[0]}:{address[1]}") # Display the sequence number of the received packet

        # Determine if the packet should be dropped based on the fixed drop probability
        if random.random() <= drop_prob:
            total_packets_dropped += 1
            print(f"Dropping packet {received_sequence_number}..........") #packet dropped with the sequence number
            continue

        message = message.decode().upper()  # Process packet that are not dropped and send response back to client
        response_message = f"Response to packet {received_sequence_number}" #Include the same sequence number in the response
        serverSocket.sendto(response_message.encode(), address)  #Send encoded message back to the client to decode
        print(f"Response sent to {address[0]}:{address[1]} with Sequence Number: {received_sequence_number}")

    print(f"Total packets dropped: {total_packets_dropped}") # print total number of packets dropped 
    print(f"Total packets processed: {total_packets_received - total_packets_dropped}") # print total number of packets with response sent
    print(f"Total packets received: {total_packets_received}") # print total number of packets received 
    