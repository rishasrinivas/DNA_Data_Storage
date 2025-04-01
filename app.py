import os
import streamlit as st

# DNA Mapping
binary_to_dna_map = {"00": "A", "01": "T", "10": "G", "11": "C"}

# Function to convert binary data to DNA
def binary_to_dna(binary_string):
    return "".join(binary_to_dna_map[binary_string[i:i+2]] for i in range(0, len(binary_string), 2))

# Convert any file to a DNA sequence
def file_to_dna(file_bytes, file_name):
    """
    Converts uploaded file bytes into a DNA sequence.

    Parameters:
        file_bytes (bytes): The binary content of the uploaded file.
        file_name (str): The name of the file.

    Returns:
        dna_sequence (str): The generated DNA sequence.
        metadata (str): Metadata containing file extension and size.
    """
    binary_string = "".join(format(byte, "08b") for byte in file_bytes)
    dna_sequence = binary_to_dna(binary_string)
    
    # Metadata
    file_ext = os.path.splitext(file_name)[1]
    metadata = f"{file_ext}\n{len(file_bytes)}"  # Store file extension and size

    return dna_sequence, metadata

# Streamlit UI
st.title("🧬 DNA File Converter")
st.write("Upload any file to convert it into a DNA sequence!")

uploaded_file = st.file_uploader("Choose a file", type=None)  # Accepts any file type

if uploaded_file:
    file_bytes = uploaded_file.read()
    
    # Convert file to DNA
    dna_sequence, metadata = file_to_dna(file_bytes, uploaded_file.name)

    # Display DNA sequence
    st.subheader("DNA Sequence Output")
    st.text_area("DNA Sequence:", dna_sequence[:5000] + "..." if len(dna_sequence) > 5000 else dna_sequence, height=200)
    
    # Provide download buttons
    st.download_button("Download DNA Sequence", dna_sequence, "dna_sequence.txt")
    st.download_button("Download Metadata", metadata, "metadata.txt")

    st.success("✅ Conversion Successful!")

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit")

