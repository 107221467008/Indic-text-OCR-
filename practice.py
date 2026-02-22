'''import cv2
import pytesseract
import easyocr
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
# Load your image
image_path = "C:\\Users\\rinda\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-06-04 201456.png"  # Replace with your image file
image = cv2.imread(image_path)

# Convert BGR to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Show image
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')
plt.show()
# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Remove noise (optional)
denoised = cv2.medianBlur(thresh, 3)

# Show preprocessed image
plt.imshow(denoised, cmap='gray')
plt.title('Preprocessed Image')
plt.axis('off')
plt.show()
# Set the path to tesseract.exe if you're using Windows
# Example: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set language (e.g., 'hin' for Hindi, 'tam' for Tamil, 'tel' for Telugu)
custom_config = r'--oem 3 --psm 6 -l hin'  # Change "hin" to other language codes if needed

text_tesseract = pytesseract.image_to_string(denoised, config=custom_config)
print("📌 Tesseract OCR Output:\n")
print(text_tesseract)
# Initialize EasyOCR Reader (supports many Indic languages)
reader = easyocr.Reader(['en', 'hi'])  # Add other language codes like 'ta', 'te', etc.

text_easyocr = reader.readtext(image_path, detail=0)
print("📌 EasyOCR Output:\n")
print("\n".join(text_easyocr))
print("Tesseract Output:\n", text_tesseract[:500])
print("\nEasyOCR Output:\n", "\n".join(text_easyocr[:5]))'''

from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
ds = load_dataset("rs545837/sanskrit-ocr-images")
