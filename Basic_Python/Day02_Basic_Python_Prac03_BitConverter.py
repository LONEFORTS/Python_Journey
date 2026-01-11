# Following is the program to convert bits into megabytes, gigabytes and terabytes
bits = int(input("Enter the number of bits: "))

# Each byte consists of 8 bits
bytes_value = bits / 8

# Logic: Power of 1024 for each level
Megabytes = bytes_value / (1024**2)
Gigabytes = bytes_value / (1024**3)
Terabytes = bytes_value / (1024**4)

print("MB:", Megabytes)
print("GB:", Gigabytes)
print("TB:", Terabytes)