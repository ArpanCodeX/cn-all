import time

frames = int(input("Enter number of frames: "))
lost = int(input("Enter frame number to lose (-1 for no loss): "))

for i in range(frames):

    print("\nSender: Sending Frame", i)
    time.sleep(1)

    if i == lost:
        print("Frame", i, "Lost")
        time.sleep(1)

        print("Sender: Timeout")
        time.sleep(1)

        print("Sender: Resending Frame", i)
        time.sleep(1)

    print("Receiver: Frame", i, "Received")
    time.sleep(1)

    print("Receiver: ACK", i, "Sent")
    time.sleep(1)

    print("Sender: ACK", i, "Received")
    time.sleep(1)

print("\nAll frames transmitted successfully.")