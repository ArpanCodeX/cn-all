import socket

PORT = 5000

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sender.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

message = input("Enter message: ")

sender.sendto(message.encode(), ("255.255.255.255", PORT))

print("Broadcast message sent.")

sender.close()