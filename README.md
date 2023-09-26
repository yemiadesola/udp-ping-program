# udp-ping-program
The UDP Ping Program is a Python-based application that simulates network communication using User Datagram Protocol (UDP).

# UDP Ping Program
This is a simple UDP Ping program implemented in Python. It consists of both a client (`UDPClient.py`) and a server (`UDPServer.py`) component.

## Description
The UDP Ping program simulates sending ping messages from a client to a server. The server randomly drops a percentage of received packets to simulate real-world network conditions. The client measures the round-trip time for each ping message.

## Usage

### Server
The server program (`UDPServer.py`) listens for incoming UDP packets on port 12000. It randomly drops 40% of the received packets and responds to the rest. You can run the server using the following command:

```bash
python UDPServer.py
python UDPClient.py

