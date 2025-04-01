import os

# DNA Mapping
binary_to_dna_map = {"00": "A", "01": "T", "10": "G", "11": "C"}

# Function to convert binary data to DNA
def binary_to_dna(binary_string):
    return "".join(binary_to_dna_map[binary_string[i:i+2]] for i in range(0, len(binary_string), 2))

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

# Example Usage
if __name__ == "__main__":
    file_to_dna("1.pdf", "output_dna.txt", "metadata.txt")

