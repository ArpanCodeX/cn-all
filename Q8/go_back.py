# Go-Back-N ARQ Simulation

frames = int(input("Enter number of frames: "))
window = int(input("Enter window size: "))
lost = int(input("Enter frame number to lose (-1 for no loss): "))

i = 0

while i < frames:
    print("\nSending Window:")

    end = min(i + window, frames)

    # Send frames
    for j in range(i, end):
        print("Frame", j, "sent")

    # Check loss
    if lost >= i and lost < end:
        print("\nFrame", lost, "lost!")
        print("Receiver sends ACK for frame", lost - 1)

        print("\nRetransmitting from frame", lost)

        for j in range(lost, end):
            print("Frame", j, "resent")
            print("ACK", j, "received")

        i = end

    else:
        for j in range(i, end):
            print("ACK", j, "received")

        i = end

print("\nAll frames transmitted successfully.")