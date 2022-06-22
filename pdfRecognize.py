"""
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os

archivoPDF = 'EstrategiaV1.pdf'

# Store all the pages of the PDF in a variable
pagina = convert_from_path(archivoPDF, 1)
  
# Counter to store images of each page of PDF to image
image_counter = 1

# Iterate through all the pages stored above
for page in pagina:
  
    # For each page, filename will be:
    # PDF page 1 -> page_1.jpg
    # PDF page 2 -> page_2.jpg

    filename = "page_"+str(image_counter)+".jpg"
      
    # Save the image of the page in system
    page.save(filename, 'JPEG')
  
    # Increment the counter to update filename
    image_counter = image_counter + 1

'''
Part #2 - Recognizing text from the images using OCR
'''

# Variable to get count of total number of pages
filelimit = image_counter-1
  
# Creating a text file to write the output
outfile = "out_text.txt"
  
# Open the file in append mode so that 
# All contents of all images are added to the same file
f = open(outfile, "a")
  
# Iterate from 1 to total number of pages
for i in range(1, filelimit + 1):
  
    # Set filename to recognize text from
    # Again, these files will be:
    # page_1.jpg
    # page_2.jpg
    # ....
    # page_n.jpg
    filename = "page_"+str(i)+".jpg"

    # Recognize the text as string in image using pytesserct
    text = str(((pytesseract.image_to_string(Image.open(filename)))))

    # The recognized text is stored in variable text
    # Any string processing may be applied on text
    # Here, basic formatting has been done:
    # In many PDFs, at line ending, if a word can't
    # be written fully, a 'hyphen' is added.
    # The rest of the word is written in the next line
    # Eg: This is a sample text this word here GeeksF-
    # orGeeks is half on first line, remaining on next.
    # To remove this, we replace every '-\n' to ''.
    text = text.replace('-\n', '')    

    # Finally, write the processed text to the file.
    f.write(text)
  
# Close the file after writing all the text.
f.close()
"""

import os
import requests
import pdfplumber

#Lee el archivo pdf a trabajar
with pdfplumber.open(r'C:\Users\jscorrea\Documents\Robots\RPA Prueba\RPAtest1\hijo dary.pdf') as pdf:
    #selecciona la pagina
    page = pdf.pages[0]
    #extrae la información en forma de texto
    text = page.extract_text(x_tolerance=2)
    #divide el texto por lineas(opcional)
    lines = text.split('\n')
    print(text)
    #Busca una palabra clave en todas las lineas del texto
    for line in lines:          
            if lines.__contains__('Develop'):   
                #procesando=False
                print('SI HAY RAMA DEVELOP')
                #break
            
    os.system('echo off | clip')


