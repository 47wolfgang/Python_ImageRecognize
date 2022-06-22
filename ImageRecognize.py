# text recognition
import cv2
import pytesseract

# read image
img = cv2.imread(r'C:\Users\jscorrea\Documents\Robots\RPA Prueba\RPAtest1\img.jpg')

# configurations
config = ('-l eng --oem 1 --psm 3')

# pytessercat
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\jscorrea\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(img, config=config)

# print text
#text = text.split('\n')
print(text)