# PDF to Audiobook Converter

## Description:
This Python script converts a PDF file into an audiobook by reading out the text using a text-to-speech engine. It utilizes the `PyPDF2` library to extract text from the PDF file and the `pyttsx3` library for text-to-speech conversion.

## Requirements:
- Python 3.x
- PyPDF2 library (`pip install PyPDF2`)
- pyttsx3 library (`pip install pyttsx3`)

## Usage:
1. Ensure that you have Python installed on your system along with the required libraries.
2. Place the PDF file you want to convert into the same directory as this script.
3. Update the filename in the script to match the name of your PDF file.
4. Run the script using Python.

# Description of the code

1. **Importing Libraries**: The code begins by importing two Python libraries:
   - `pyttsx3`: This library is used for text-to-speech conversion.
   - `PyPDF2`: This library is used for reading PDF files.

2. **Opening the PDF File**: The code opens a PDF file named "object_oriented_python_tutorial.pdf" in binary read mode (`'rb'`). 

3. **Initializing PDF Reader**: It initializes a `PdfFileReader` object from `PyPDF2` to read the PDF file.

4. **Getting Number of Pages**: It retrieves the total number of pages in the PDF file using the `numPages` attribute of the `pdfReader` object and prints the result.

5. **Initializing Text-to-Speech Engine**: It initializes the text-to-speech engine using `pyttsx3.init()`.

6. **Speaking Introductory Message**: It uses the text-to-speech engine to speak an introductory message.

7. **Extracting and Speaking Text from a Specific Page**: 
   - It extracts the text from page , using the `getPage()` method of the `pdfReader` object.
   - Then, it extracts the text from the page using the `extractText()` method.
   - Finally, it uses the text-to-speech engine to speak out the extracted text.

8. **Running Text-to-Speech Engine**: It runs the text-to-speech engine using `runAndWait()` method to ensure that the text is spoken synchronously.


# Acknowledgments
This simple code helps to read a specific page from a PDF file and convert its content into speech using well-known Python libraries. The PyPDF2 library is utilized for PDF processing, enabling accurate text extraction for speech conversion.

# Author
Sumona Banerjee

# License
This project is licensed under the MIT License.
