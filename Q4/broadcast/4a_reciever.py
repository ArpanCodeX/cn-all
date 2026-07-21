import socket

PORT = 5000

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

receiver.bind(("", PORT))

print("Waiting for broadcast message...")

data, addr = receiver.recvfrom(1024)

print("Received from", addr)
print("Message:", data.decode())

receiver.close()