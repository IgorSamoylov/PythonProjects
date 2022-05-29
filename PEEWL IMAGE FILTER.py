from PIL import Image, ImageFilter

import matplotlib.pyplot as plt
import random as r

#path = "C:/Users/A12/Downloads/PICTURES/01.jpg"
path = "F:/Archiv/PHOTO/Фото 6/122CANON/IMG_2889.jpg"

Filters = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.DETAIL,
           ImageFilter.EDGE_ENHANCE, ImageFilter.EDGE_ENHANCE_MORE,
           ImageFilter.EMBOSS, ImageFilter.FIND_EDGES, ImageFilter.SHARPEN,
           ImageFilter.SMOOTH, ImageFilter.SMOOTH_MORE]

FiltersAdv = [ImageFilter.Color3DLUT(
    size=25, table=[(r.random(), r.random(), r.random()) for x in range(15625)])]

with Image.open(path) as im:
    for filtr in FiltersAdv:
        # Blur the input image using the filter ImageFilter.BLUR
        im_blurred = im.filter(filter=filtr) #.rotate(-90)

        fig = plt.figure(str(filtr)) # Creating canvas
        plt.imshow(im_blurred) # Show image that will be sent to canvas
        plt.show() # Show canvas with image

        #im_blurred.show()
        im_blurred.save(str(r.random()) + ".jpg", "jpeg")

