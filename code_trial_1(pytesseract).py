import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
file = open("recognized.txt", "w+")
file.write("")
file.close()
img=cv2.imread('3.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #pytesseract accepts rgb values and open cv is in bgr
text=pytesseract.image_to_string(img)
print(text[:-1])
cv2.imshow('Result',img)
cv2.waitKey(0)
file = open("recognized.txt", "a")
file.write(text)
file.write("\n")
file.close