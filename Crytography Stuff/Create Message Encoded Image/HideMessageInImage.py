#!/usr/bin/env python
__author__ = 'marcsantiago'

from PIL import Image
from easygui import buttonbox, enterbox, msgbox, fileopenbox


answer = buttonbox("What would you like to do, encrypt a message or decrypt the image?", choices=["Encrypt", "Decrypt"])

if answer == "Encrypt":
    plaintext = enterbox("Enter a message you would like to hide in an image.")
    im = Image.fromstring('L', (1, len(plaintext)), plaintext)
    filename = enterbox("Give your image a name.")
    if ".png" in filename:
        filename = filename.replace(".png", "")
    im.save(filename + ".png", format("PNG"))
elif answer == "Decrypt":
    image_file = fileopenbox("Please pick an image file that you would like to decrypt.", filetypes=["*.png"])
    my_image = Image.open(image_file)
    pix = my_image.getdata()
    temp = []
    for i in list(pix):
        temp.append(i)
    msgbox("".join([chr(i) for i in temp]))
