import cv2
import pytesseract
import os
from difflib import SequenceMatcher

# If needed, set the path to your local tesseract installation
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Folder path containing images
folder_path ="C:\\Users\\rinda\\OneDrive\\OCR\\nhcd\\nhcd\\consonants\\1"  # e.g., './images'

# Optional: store results
results = {}

# Custom Tesseract config for Hindi (Devanagari)
custom_config = r'--oem 3 --psm 6 -l hin'

# Loop over all files
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(folder_path, filename)

        # Load and preprocess
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # OCR
        text = pytesseract.image_to_string(thresh, config=custom_config)

        # Save result
        results[filename] = text.strip()

# Print or save results
for file, text in results.items():
    print(f"\n📄 File: {file}\n📝 Extracted Text:\n{text}\n{'-'*40}")
with open("ocr_output.txt", "w", encoding='utf-8') as f:
    for file, text in results.items():
        f.write(f"File: {file}\n{text}\n{'-'*40}\n")
for file, extracted in results.items():
    # Assuming ground truth text file has same name as image but .txt extension
    txt_file = os.path.join('ground_truth_folder', file.replace('.jpg', '.txt'))

    if os.path.exists(txt_file):
        with open(txt_file, 'r', encoding='utf-8') as f:
            actual = f.read().strip()

        similarity = SequenceMatcher(None, actual, extracted).ratio()
        print(f"{file} ➤ Accuracy: {similarity * 100:.2f}%")
import cv2
import pytesseract
import os
import pandas as pd
from difflib import SequenceMatcher
import matplotlib.pyplot as plt

# Set Tesseract path if needed (for Windows users)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Folder containing images
image_folder = "C:\\Users\\rinda\\OneDrive\\OCR\\nhcd\\nhcd\\consonants\\1"  # e.g., './devanagari_images'
ground_truth_folder = "C:\\Users\\rinda\\OneDrive\\OCR\\nhcd\\nhcd\\consonants\\1"  # Only if available

# OCR settings
custom_config = r'--oem 3 --psm 6 -l hin'

# Results list
results = []

# Loop through images
for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(image_folder, filename)

        # Read & preprocess image
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # OCR
        extracted_text = pytesseract.image_to_string(thresh, config=custom_config).strip()

        # Try to load ground truth
        ground_truth_text = ''
        accuracy = ''
        if os.path.exists(ground_truth_folder):
            txt_file = os.path.join(ground_truth_folder, filename.replace('.jpg', '.txt'))
            if os.path.isfile(txt_file):
                with open(txt_file, 'r', encoding='utf-8') as f:
                    ground_truth_text = f.read().strip()
                similarity = SequenceMatcher(None, ground_truth_text, extracted_text).ratio()
                accuracy = f"{similarity * 100:.2f}%"

        # Add to results
        results.append({
            'Filename': filename,
            'Extracted Text': extracted_text,
            'Ground Truth': ground_truth_text,
            'Accuracy': accuracy
        })

        # Optional: Visualize
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        
        plt.title(f"OCR Output: {extracted_text}")
        plt.axis('off')
        plt.show()

# Save results to CSV
df = pd.DataFrame(results)
df.to_csv('ocr_results.csv', index=False, encoding='utf-8-sig')
print("✅ OCR analysis saved to ocr_results.csv")
