"""
PDF to Text Extractor

This Flask application provides a simple web interface to extract text from PDF files.

Dependencies:
    Flask: Web framework for Python.
    PyPDF2: Library for reading PDF files.

Routes:
    - '/': Renders the index.html template, which contains a form to upload a PDF file.
    - '/extract': Accepts a POST request with a PDF file, extracts text from it, and returns the extracted text.

Usage:
    1. Run the Flask application. The index page will be accessible at 'http://localhost:5000'.
    2. Upload a PDF file using the provided form.
    3. Click the 'Extract Text' button to extract text from the uploaded PDF file.
"""

from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_text():
    """
    Extract text from a PDF file uploaded via a POST request.

    Returns:
        str: Extracted text from the PDF file.
    """
    pdf_file = request.files['pdf_file']
    if pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        extracted_text = ""
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            extracted_text += page.extract_text()
        return extracted_text
    else:
        return "No PDF file provided."

# Ensures that the Flask application starts only when the script is run directly
# Allowing it to be executed standalone or imported into other scripts without automatically starting the server. 
# Common practice in Python web applications.

if __name__ == "__main__":
    app.run(debug=True)
