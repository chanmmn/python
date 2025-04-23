import pytesseract
from PIL import Image

# Path to the Tesseract executable
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        # Perform OCR on the image
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    extracted_text = ocr_image(image_path)
    print("Extracted Text:")
    print(extracted_text)