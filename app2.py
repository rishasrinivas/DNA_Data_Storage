import streamlit as st
import os

# DNA Mapping
dna_to_binary_map = {"A": "00", "T": "01", "G": "10", "C": "11"}

# Function to convert DNA back to binary
def dna_to_binary(dna_sequence):
    try:
        return "".join(dna_to_binary_map[base] for base in dna_sequence)
    except KeyError as e:
        raise ValueError(f"Invalid character '{e.args[0]}' in DNA sequence. Expected only A, T, G, or C.")

# Convert DNA sequence back to original file
def dna_to_file(dna_sequence, metadata_content):
    """
    Converts a DNA sequence back into the original file.

    Parameters:
        dna_sequence (str): DNA sequence string.
        metadata_content (str): Metadata content (file extension and size).

    Returns:
        bytes: Reconstructed file content.
        str: Original file extension.
    """
    try:
        if not dna_sequence:
            raise ValueError("DNA sequence file is empty.")

        # Convert DNA back to binary string
        binary_string = dna_to_binary(dna_sequence)

        # Ensure binary string length is a multiple of 8
        if len(binary_string) % 8 != 0:
            raise ValueError("Binary string length is not a multiple of 8. Data may be corrupted.")

        # Convert binary string back to bytes
        file_bytes = bytes(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))

        # Parse metadata
        metadata_lines = metadata_content.strip().split("\n")
        if len(metadata_lines) < 2:
            raise ValueError("Metadata file is incomplete or corrupted.")
        file_ext, file_size = metadata_lines[0], metadata_lines[1]

        if not file_size.isdigit():
            raise ValueError("Invalid file size in metadata file.")
        file_size = int(file_size)  # Convert file size to integer

        return file_bytes[:file_size], file_ext  # Trim to original file size

    except Exception as e:
        return None, str(e)  # Return None for file data, error message

# Streamlit App UI
st.title("🔬 DNA-to-File Converter")

st.write("Upload the **DNA sequence file** and **metadata file** to reconstruct the original file.")

# File upload
dna_file = st.file_uploader("Upload DNA Sequence File (.txt)", type=["txt"])
metadata_file = st.file_uploader("Upload Metadata File (.txt)", type=["txt"])

if dna_file and metadata_file:
    dna_content = dna_file.getvalue().decode("utf-8").strip()
    metadata_content = metadata_file.getvalue().decode("utf-8").strip()

    if st.button("🔄 Convert DNA Back to File"):
        with st.spinner("Processing..."):
            file_data, file_ext = dna_to_file(dna_content, metadata_content)

            if file_data:  # Only if conversion is successful
                st.success("✅ File successfully reconstructed!")
                st.download_button(
                    label="📥 Download Reconstructed File",
                    data=file_data,
                    file_name=f"reconstructed_file{file_ext}",
                    mime="application/octet-stream",
                )
            else:
                st.error(f"❌ Error: {file_ext}")  # Display error message

