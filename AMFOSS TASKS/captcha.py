#!python3
from PIL import Image
from pytesseract import image_to_string

pytesseract = Image.open('captcha.jpg')

text = image_to_string(image, config='--psm6', output_type=Output.STRING)

print(text)
