frames = int(input("Enter number of frames: "))
window = int(input("Enter window size: "))
lost = int(input("Enter frame number to lose (-1 for no loss): "))

ack = [False] * frames

i = 0

while i < frames:

    end = min(i + window, frames)

    print("\nSending Window:")

    for j in range(i, end):

        if not ack[j]:

            print("Frame", j, "sent")

            if j == lost:
                print("Frame", j, "lost")

            else:
                print("ACK", j, "received")
                ack[j] = True

    # Retransmit only the lost frame
    if lost >= i and lost < end and not ack[lost]:

        print("\nRetransmitting only Frame", lost)

        print("Frame", lost, "resent")
        print("ACK", lost, "received")

        ack[lost] = True

    i = end

print("\nAll frames transmitted successfully.")