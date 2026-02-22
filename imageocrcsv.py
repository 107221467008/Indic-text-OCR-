import os
import csv

folder_path = "C:\\Users\\rinda\\OneDrive\\OCR\\nhcd\\nhcd\\consonants\\1"
csv_file = "images.csv"

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["filename", "label"])  # header

    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # adjust formats if needed
            label = "unknown"  # You can modify this logic to extract real labels
            writer.writerow([os.path.join(folder_path, filename), label])