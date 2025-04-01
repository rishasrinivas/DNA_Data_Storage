import barcode
from barcode.writer import ImageWriter

def generate_code128(dna_file, output_image="dna_barcode.png"):
    """
    Reads a DNA sequence from a text file and generates a Code128 barcode.

    Parameters:
        dna_file (str): Path to the input .txt file containing the DNA sequence.
        output_image (str): Path to save the generated barcode image.
    """
    try:
        # Read DNA sequence from the file
        with open(dna_file, "r") as file:
            dna_sequence = file.read().strip()

        if not dna_sequence:
            raise ValueError("The DNA sequence file is empty!")

        # Generate Code128 barcode
        code128 = barcode.get("code128", dna_sequence, writer=ImageWriter())
        code128.save(output_image)

        print(f"✅ Code128 Barcode saved as {output_image}")

    except FileNotFoundError:
        print("❌ Error: DNA sequence file not found!")
    except ValueError as ve:
        print(f"❌ Error: {ve}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Example Usage
if __name__ == "__main__":
    generate_code128("output_dna.txt")
