# We import the necessary packages
#import the needed packages
import cv2
import os,argparse
import pytesseract
from PIL import Image

#convert to grayscale image
gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)

#checking whether thresh or blur
cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
#cv2.medianBlur(gray, 3)
	

text = pytesseract.image_to_string(Image.fromarray(gray))
print(text)

