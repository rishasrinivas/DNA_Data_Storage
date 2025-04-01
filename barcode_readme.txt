The DNA sequemce shoul be small

This script generates a Code128 barcode from a DNA sequence stored in a text file. It reads the sequence from the file and converts it into a barcode image.

Requirements

Ensure you have the following Python packages installed:

pip install python-barcode pillow

Usage

Create a text file (e.g., output_dna.txt) containing a DNA sequence.

Run the script to generate the barcode:

python script.py

By default, the output barcode image will be saved as dna_barcode.png.

Parameters

dna_file (str): Path to the input .txt file containing the DNA sequence.

output_image (str, optional): Path to save the generated barcode image. Default is dna_barcode.png.

Error Handling

If the input file is missing, the script will display an error message.

If the input file is empty, the script will raise a ValueError.

Any unexpected errors will be caught and displayed.

Example

Input (output_dna.txt):

ATGCGTACGTAGCTAG

Output: dna_barcode.png (Barcode Image)
