# Read the DNA sequence from a file
with open("dna.txt", "r") as file:
    dna_sequence = file.read().strip()  # Remove any trailing spaces or newlines

# Validate DNA sequence
valid_bases = {"A", "T", "G", "C"}
if not set(dna_sequence).issubset(valid_bases):
    raise ValueError("DNA sequence contains invalid characters!")

# Reverse map DNA bases to binary
binary_mapping = {"A": "00", "T": "01", "G": "10", "C": "11"}
binary_string = "".join(binary_mapping[base] for base in dna_sequence)

# Ensure binary string length is divisible by 8
binary_string = binary_string[:len(binary_string) - len(binary_string) % 8]

# Convert binary to text
output_string = ""
for i in range(0, len(binary_string), 8):
    byte = binary_string[i:i+8]
    output_string += chr(int(byte, 2))  # Convert binary to ASCII character

# Filter printable characters
output_string = "".join(c for c in output_string if c.isprintable())

# Write the decoded text to a file
with open("out_text.txt", "w") as file:
    file.write(output_string)

print("Decoded text saved to 'out_text.txt'")
