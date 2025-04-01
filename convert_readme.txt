convert.py = converters of file to DNA sequence.
deconvert.py = converters the DNA sequence back to original file.
both.py - works as first converter of file to DNA and back to original file from the DNA.

Explanation of both.py
DNA File Conversion System

Overview
This project allows you to **convert any file** (text, images, PDFs, etc.) into a DNA sequence and later **reconstruct the original file** from the DNA sequence. This process is based on encoding binary data as DNA bases (A, T, G, C) and decoding it back.

Features
- Supports **any file type** (text, images, PDFs, etc.).
- Converts **binary data** to **DNA sequences**.
- Stores **metadata** for proper reconstruction.
- Recovers the **original file** from the DNA sequence.

How It Works
1. The file's **binary data** is read and converted to an 8-bit binary string.
2. The binary data is mapped to **DNA bases** (`A`, `T`, `G`, `C`).
3. The DNA sequence is saved in a file.
4. A **metadata file** stores the original file's extension and size.
5. To reconstruct, the DNA sequence is converted **back to binary**, and the metadata is used to restore the file.

---

Installation
Ensure you have **Python 3** installed and the required dependencies:
```sh
pip install numpy pillow
```

Usage
1) Convert a File to DNA
```python
file_to_dna("input_file.txt", "output_dna.txt", "metadata.txt")
```
- `input_file.txt`: The file to convert.
- `output_dna.txt`: The DNA sequence output file.
- `metadata.txt`: Stores file extension and size.

2) Convert DNA Back to Original File
```python
dna_to_file("output_dna.txt", "metadata.txt", "reconstructed_file")
```
- `output_dna.txt`: The DNA sequence file.
- `metadata.txt`: The metadata file.
- `reconstructed_file`: The output filename (auto-appends correct extension).

---

Example
Convert a File to DNA:
```sh
python convert_to_dna.py text.pdf output_dna.txt metadata.txt
```

Convert DNA Back to a File:
```sh
python convert_from_dna.py output_dna.txt metadata.txt reconstructed.pdf
```

---

Supported File Types
refer end of the document.
---

Limitations
- Large files create **very long DNA sequences**, requiring high storage and processing time.
- Binary-encoded **DNA is not biologically meaningful** and is intended for data storage only.


Supported File Types
Documents & Text
.txt (Plain Text)
.pdf (PDF)
.docx (Microsoft Word)
.xlsx (Microsoft Excel)
.pptx (Microsoft PowerPoint)
.csv (Comma-Separated Values)
.rtf (Rich Text Format)
Images & Graphics
.png (Portable Network Graphics)
.jpg / .jpeg (Joint Photographic Experts Group)
.gif (Graphics Interchange Format)
.bmp (Bitmap Image)
.tiff (Tagged Image File Format)
.webp (WebP Image Format)
.psd (Adobe Photoshop)
.svg (Scalable Vector Graphics)
.eps (Encapsulated PostScript)
.raw (Raw Image Format)
Audio Files
.mp3 (MPEG Audio Layer 3)
.wav (Waveform Audio)
.aac (Advanced Audio Codec)
.flac (Free Lossless Audio Codec)
.ogg (Ogg Vorbis)
Video Files
.mp4 (MPEG-4)
.avi (Audio Video Interleave)
.mkv (Matroska Video)
.mov (Apple QuickTime Movie)
.wmv (Windows Media Video)
.flv (Flash Video)
Compressed & Archives
.zip (ZIP Archive)
.rar (RAR Archive)
.tar (Tarball)
.7z (7-Zip Archive)
.gz (Gzip Compressed File)
Executable & System Files
.exe (Windows Executable)
.bin (Binary File)
.iso (Disk Image)
.dll (Dynamic Link Library)
.so (Shared Object)
.dmg (Apple Disk Image)
.bat (Batch Script)
.sh (Shell Script)
Programming & Code Files
.py (Python)
.java (Java)
.cpp (C++)
.js (JavaScript)
.html (HTML)
.css (Cascading Style Sheets)
.json (JavaScript Object Notation)
.xml (Extensible Markup Language)
.yaml (YAML Ain’t Markup Language)
.sql (Structured Query Language)
