
def xor(a, b):
    result = ""
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result

def divide(data, divisor):
    n = len(divisor)
    rem = data[:n]

    for i in range(n, len(data)):
        if rem[0] == "1":
            rem = xor(divisor, rem) + data[i]
        else:
            rem = xor("0" * n, rem) + data[i]

    if rem[0] == "1":
        rem = xor(divisor, rem)
    else:
        rem = xor("0" * n, rem)

    return rem

data = input("Enter Data: ")
divisor = input("Enter Divisor: ")

print("\n----- Sender -----")
temp = data + "0" * (len(divisor) - 1)
remainder = divide(temp, divisor)
codeword = data + remainder

print("Data        :", data)
print("CRC         :", remainder)
print("Codeword    :", codeword)

print("\n----- Receiver -----")
received = input("Enter Received Codeword: ")

check = divide(received, divisor)

print("Remainder   :", check)

if set(check) == {"0"}:
    print("Result      : No Error Detected")
else:
    print("Result      : Error Detected")