import os

# DNA Mapping
dna_to_binary_map = {"A": "00", "T": "01", "G": "10", "C": "11"}

# Function to convert DNA back to binary
def dna_to_binary(dna_sequence):
    return "".join(dna_to_binary_map[base] for base in dna_sequence)

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

# Example Usage
if __name__ == "__main__":
    dna_to_file("output_dna.txt", "metadata.txt", "reconstructed_file")

