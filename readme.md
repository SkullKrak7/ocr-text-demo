# OCR Text Extraction Demo

This is a minimal project demonstrating Optical Character Recognition (OCR) using Python and Tesseract on Windows. It serves as a foundation for document parsing and content extraction systems.

## Overview

This script extracts text from scanned documents or screenshots using `pytesseract`. It is intended for use in OCR pipelines, document understanding, or downstream NLP tasks.

## Repository Structure

```
ocr-text-demo/
├── sample.png          
├── ocr.py              
├── requirements.txt    
├── README.md           
```

## Requirements

Dependencies are listed in `requirements.txt`.

## Output

The script prints the extracted text to the console and writes it to `extracted_text.txt`.

## Future Work

- Key-value field extraction
- Layout-aware parsing (e.g., LayoutLM)
- Classification using Hugging Face Transformers

## License

MIT License

This project was created to demonstrate core OCR capability and can be extended for intelligent document processing tasks.
