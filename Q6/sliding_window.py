window_size = int(input("Enter Window Size: "))
total_frames = int(input("Enter Total Frames: "))

sender = 0

while sender < total_frames:
    print("\nSender Window:")

    for i in range(sender, min(sender + window_size, total_frames)):
        print("Frame", i, "sent")

    print("\nReceiver:")

    for i in range(sender, min(sender + window_size, total_frames)):
        print("ACK", i, "received")

    sender += window_size

print("\nAll frames transmitted successfully.")