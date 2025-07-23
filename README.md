# PDF Analysis Project

This project is a Python-based tool designed for extracting content from PDF files. It utilizes the PyMuPDF (`fitz`) library to process PDF documents and extract both text and images from each page.

## Features

- Extracts text content from each page of a PDF.
- Extracts all images from each page and saves them as PNG files.
- Stores extracted data (text and image paths) as structured JSON.

## Usage

1. Make sure you have Python installed.
2. Install the required dependencies (mainly `PyMuPDF`).  
   ```
   pip install pymupdf
   ```
3. Run the script:
   ```bash
   python extract_content.py
   ```
   By default, the script runs an example that extracts content from `sample.pdf` and saves images to an `extracted_images` directory.

## Example

```python
from extract_content import extract_pdf_content

extract_pdf_content("sample.pdf", "extracted_images")
```

## Output

- Extracted images are saved in the specified output folder.
- A JSON file (`sample_output.json`) is generated containing the text and image paths for each page.
