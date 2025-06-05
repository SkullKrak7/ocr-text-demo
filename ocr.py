import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = "sample.png"

if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found at: {image_path}")

image = Image.open(image_path)
text = pytesseract.image_to_string(image)

print("Extracted text:\n" + "-" * 20)
print(text)

with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(text)
    print("\nText saved to 'extracted_text.txt'")