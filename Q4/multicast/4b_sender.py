import socket

MULTICAST_GROUP = "224.1.1.1"
PORT = 5000

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter message: ")

sender.sendto(message.encode(), (MULTICAST_GROUP, PORT))

print("Multicast message sent.")

sender.close()