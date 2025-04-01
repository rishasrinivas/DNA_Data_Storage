from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import gzip

# Function to decrypt and decompress the file
def decrypt_and_decompress(input_file, output_file, encryption_key):
    # Open the compressed encrypted file
    with gzip.open(input_file, 'rb') as gz_file:
        iv = gz_file.read(16)  # Read the first 16 bytes for IV (AES block size)
        encrypted_data = gz_file.read()  # The rest is the encrypted data

    # Decrypt the data using AES
    cipher = AES.new(encryption_key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Write the decrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

    print(f"File {input_file} decrypted and decompressed as {output_file}")

# Example usage:
# Load the encryption key from the file used during encryption
with open("encryption_key.bin", "rb") as key_file:
    key = key_file.read()  # Load the key from the file

# Call the decryption function with the correct key
decrypt_and_decompress('encrypted_compressed_dna.gz', 'decrypted_dna.txt', key)
