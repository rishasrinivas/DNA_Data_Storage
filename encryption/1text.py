# Read input text from a file
with open("text.txt", "r") as file:
    input_string = file.read().strip()  # Read and clean the input text

# Convert the text to binary
binary_string = "".join(format(ord(char), '08b') for char in input_string)

# Map binary pairs to DNA bases
dna_mapping = {"00": "A", "01": "T", "10": "G", "11": "C"}
dna_sequence = "".join(dna_mapping[binary_string[i:i+2]] for i in range(0, len(binary_string), 2))

# Write DNA sequence to a file
with open("dna.txt", "w") as file:
    file.write(dna_sequence)

print("DNA sequence saved to 'dna.txt'")

