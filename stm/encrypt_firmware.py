import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# --- CONFIGURATION ---
# AES-128 requires a 16-byte key
KEY = b'MySecretKey12345'  # 16 bytes exactly
IV = b'InitializationVt'   # 16 bytes exactly (Fixed IV for simplicity in this demo)

def encrypt_file(input_filename, output_filename):
    # 1. Read the "Firmware" (Plaintext)
    if not os.path.exists(input_filename):
        print(f"Error: {input_filename} not found.")
        return

    with open(input_filename, 'rb') as f:
        plaintext = f.read()

    print(f"Original Size: {len(plaintext)} bytes")

    # 2. Encrypt using AES-128 in CBC mode
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    # 3. Save the Encrypted Image
    with open(output_filename, 'wb') as f:
        f.write(ciphertext)

    print(f"Encrypted Size: {len(ciphertext)} bytes")
    print(f"Success! Encrypted firmware saved to: {output_filename}")

# Create a dummy firmware file for testing
with open("firmware_v1.bin", "w") as f:
    f.write("This is a simulation of new STM32 firmware code.")

# Run encryption
encrypt_file("firmware_v1.bin", "firmware_encrypted.bin")