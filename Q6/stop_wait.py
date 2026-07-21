import time

frames = int(input("Enter number of frames: "))

for i in range(frames):
    print("\nSender: Sending Frame", i)

    time.sleep(1)

    print("Receiver: Frame", i, "Received")

    time.sleep(1)

    print("Receiver: ACK", i, "Sent")

    time.sleep(1)

    print("Sender: ACK", i, "Received")

print("\nAll frames transmitted successfully.")