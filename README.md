# DNA_Data_Storage

app.py =converts file --> DNA (any type of input)
app2.py =converts DNA and metadata --> file (to the original input)


Explaination of app.py

The DNA File Converter is a Streamlit web application that allows users to convert any file into a DNA sequence. This process transforms binary data into a DNA-encoded format using a mapping scheme. Additionally, metadata including file extension and size is generated for reference.

Features
Convert any file into a DNA sequence representation.
Download the DNA sequence as a text file.
Download metadata containing file extension and size.
Simple and intuitive web-based interface built with Streamlit.

How It Works
The uploaded file is read in binary format.
The binary data is converted into DNA sequences using the following mapping:
00 → A
01 → T
10 → G
11 → C

The converted DNA sequence is displayed on the interface.
Users can download the DNA sequence and metadata as text files.

Installation
To run the DNA File Converter, follow these steps:
Prerequisites
Ensure you have Python installed (version 3.7 or later recommended). You can check your Python version using:
python --version
Install Dependencies
Clone the repository and install the required dependencies:
git clone 
pip install -r requirements.txt

Run the Application
To start the Streamlit web app, execute the following command:
streamlit run app.py

Usage
Run the application using Streamlit.
Upload a file of any type.
View and copy the DNA sequence output.
Download the DNA sequence and metadata.




Explanation of app2.py

Features
Convert any file into a DNA sequence representation.
Convert a DNA sequence back into its original file.
Download the DNA sequence and metadata as text files.
Simple and intuitive web-based interface built with Streamlit.

How It Works
Encoding Process:
The uploaded file is read in binary format.
The binary data is converted into DNA sequences using the following mapping:
00 → A
01 → T
10 → G
11 → C

The converted DNA sequence is displayed on the interface.
Users can download the DNA sequence and metadata as text files.
Decoding Process:
Users upload the DNA sequence file and the corresponding metadata file.
The DNA sequence is converted back into a binary string using the reverse mapping:
A → 00
T → 01
G → 10
C → 11

The binary string is converted back into the original file format.
The reconstructed file is made available for download.
Installation
To run the DNA File Converter, follow these steps:
Prerequisites
Ensure you have Python installed (version 3.7 or later recommended). You can check your Python version using:
python --version
Install Dependencies
Clone the repository and install the required dependencies:
git clone https://github.com/your-repo/dna-file-converter.git
cd dna-file-converter
pip install -r requirements.txt

Run the Application
To start the Streamlit web app, execute the following command:
streamlit run app2.py

Usage

Run the application using Streamlit.
Upload a file of any type and convert it to a DNA sequence.
Download the DNA sequence and metadata.
To reconstruct the file, upload the DNA sequence file and the metadata file.
Download the reconstructed file.
