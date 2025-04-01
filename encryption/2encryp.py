from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import gzip

# Function to encrypt and compress the file
def encrypt_and_compress(input_file, output_file, encryption_key):
    # Open the dna.txt file and read the content
    with open(input_file, 'rb') as f:
        data = f.read()

    # Generate AES encryption key
    cipher = AES.new(encryption_key, AES.MODE_CBC)

    # Encrypt the data with AES (pad it to block size)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    # Compress the encrypted data using gzip
    with gzip.open(output_file, 'wb') as gz_file:
        gz_file.write(cipher.iv)  # Write the IV for later decryption
        gz_file.write(encrypted_data)

    print(f"File {input_file} encrypted and compressed as {output_file}")

# Example usage
key = get_random_bytes(32)  # Generate a random 256-bit AES key
with open("encryption_key.bin", "wb") as key_file:
    key_file.write(key)  # Save the key to a file for later use

encrypt_and_compress('dna.txt', 'encrypted_compressed_dna.gz', key)

