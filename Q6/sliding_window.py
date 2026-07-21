window_size = int(input("Enter Window Size: "))
total_frames = int(input("Enter Total Frames: "))
lost = int(input("Enter Frame Number to Lose (-1 for no loss): "))

sender = 0

while sender < total_frames:

    print("\nSender Window:")

    end = min(sender + window_size, total_frames)

    for i in range(sender, end):
        print("Frame", i, "sent")

    print("\nReceiver:")

    for i in range(sender, end):

        if i == lost:
            print("Frame", i, "Lost")
            print("No ACK", i)
        else:
            print("ACK", i, "received")

    if lost >= sender and lost < end:
        print("\nSender: Timeout")
        print("Retransmitting Frame", lost)
        print("ACK", lost, "received")

    sender += window_size

print("\nAll frames transmitted successfully.")