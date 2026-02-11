import pytesseract
from PIL import Image
import os
import sys
import platform

# Auto-detect Tesseract path based on OS
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Linux/Mac: tesseract should be in PATH

def main():
    image_path = sys.argv[1] if len(sys.argv) > 1 else "sample.png"
    
    if not os.path.exists(image_path):
        print(f"Error: Image not found at: {image_path}")
        print(f"Usage: python ocr.py [image_path]")
        sys.exit(1)
    
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        
        print("Extracted text:\n" + "-" * 20)
        print(text)
        
        output_file = "extracted_text.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"\nText saved to '{output_file}'")
        
    except pytesseract.TesseractNotFoundError:
        print("Error: Tesseract not found. Please install it:")
        print("  Ubuntu/Debian: sudo apt-get install tesseract-ocr")
        print("  macOS: brew install tesseract")
        print("  Windows: https://github.com/UB-Mannheim/tesseract/wiki")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()