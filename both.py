import os
import numpy as np
from PIL import Image

# DNA Mapping
binary_to_dna_map = {"00": "A", "01": "T", "10": "G", "11": "C"}
dna_to_binary_map = {v: k for k, v in binary_to_dna_map.items()}

# Function to convert binary data to DNA
def binary_to_dna(binary_string):
    return "".join(binary_to_dna_map[binary_string[i:i+2]] for i in range(0, len(binary_string), 2))

# Function to convert DNA back to binary
def dna_to_binary(dna_sequence):
    return "".join(dna_to_binary_map[base] for base in dna_sequence)

# Convert any file to a DNA sequence
def file_to_dna(input_file, output_dna_file, output_metadata_file):
    """
    Converts any file (text, image, pdf, etc.) into a DNA sequence.

    Parameters:
        input_file (str): Path to input file.
        output_dna_file (str): Path to save DNA sequence.
        output_metadata_file (str): Path to save metadata.
    """
    # Read file as binary
    with open(input_file, "rb") as f:
        file_data = f.read()

    # Convert binary data to bit string
    binary_string = "".join(format(byte, "08b") for byte in file_data)

    # Convert binary to DNA sequence
    dna_sequence = binary_to_dna(binary_string)

    # Save DNA sequence
    with open(output_dna_file, "w") as f:
        f.write(dna_sequence)

    # Save metadata (original file extension and size)
    file_ext = os.path.splitext(input_file)[1]
    metadata = f"{file_ext}\n{len(file_data)}"  # Store file extension and size
    with open(output_metadata_file, "w") as f:
        f.write(metadata)

    print(f"File '{input_file}' converted to DNA and saved as '{output_dna_file}'")
    print(f"Metadata saved as '{output_metadata_file}'")

# Convert DNA sequence back to original file
def dna_to_file(dna_file, metadata_file, output_file):
    """
    Converts a DNA sequence back into the original file.

    Parameters:
        dna_file (str): Path to the DNA sequence file.
        metadata_file (str): Path to the metadata file.
        output_file (str): Path to save the reconstructed file.
    """
    # Read DNA sequence
    with open(dna_file, "r") as f:
        dna_sequence = f.read().strip()

    # Convert DNA back to binary string
    binary_string = dna_to_binary(dna_sequence)

    # Convert binary string back to bytes
    file_bytes = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))

    # Read metadata (get file extension and original size)
    with open(metadata_file, "r") as f:
        file_ext, file_size = f.read().split("\n")
        file_size = int(file_size)  # Convert file size to integer

    # Ensure correct file extension
    output_file = output_file if output_file.endswith(file_ext) else output_file + file_ext

    # Save reconstructed file
    with open(output_file, "wb") as f:
        f.write(file_bytes[:file_size])  # Trim to original file size

    print(f"DNA sequence successfully converted back to '{output_file}'")

# Example Usage:
# Convert any file to DNA
file_to_dna("text.txt", "output_dna.txt", "metadata.txt")

# Convert DNA back to the original file
dna_to_file("output_dna.txt", "metadata.txt", "reconstructed_file")

