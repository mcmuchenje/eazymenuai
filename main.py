from PIL import Image
import pytesseract

# Load the PNG image
image_path = "test2.png"
image = Image.open(image_path)

# Perform OCR
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)