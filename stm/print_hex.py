# print_hex.py
filename = "firmware_encrypted.bin"

try:
    with open(filename, "rb") as f:
        data = f.read()
        
    print("COPY THIS ARRAY INTO YOUR C CODE:\n")
    print("{", end="")
    for i, byte in enumerate(data):
        print(f"0x{byte:02x}", end="")
        if i < len(data) - 1:
            print(", ", end="")
    print("};")
    print(f"\n\nTotal size: {len(data)}")

except FileNotFoundError:
    print(f"Error: Could not find {filename}")