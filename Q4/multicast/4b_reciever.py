import socket
import struct

MULTICAST_GROUP = "224.1.1.1"
PORT = 5000

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

receiver.bind(("", PORT))

group = socket.inet_aton(MULTICAST_GROUP)
mreq = struct.pack("4sL", group, socket.INADDR_ANY)

receiver.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print("Waiting for multicast message...")

data, addr = receiver.recvfrom(1024)

print("Received from:", addr)
print("Message:", data.decode())

receiver.close()