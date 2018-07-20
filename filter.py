from PIL import Image, ImageFilter
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(path):
    im = Image.open(path)
    return im

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(im):
    im.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imgname, filename):
    imgname.save(filename)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img):
    data = img.getdata()

    obamified_img = []

    white = (255, 255, 255)
    black = (0, 0, 0)
    darkgrey = (125, 125, 125)
    lightgrey = (170, 170, 170)

    for pixel in data:
        #pixel1 = (45, 145, 23)
        intensity = pixel[0] + pixel [1] + pixel [2]
        if intensity < 182:
            obamified_img.append(white)
        elif 182 <= intensity and intensity < 364:
            obamified_img.append(lightgrey)
        elif 364 <= intensity and intensity < 564:
            obamified_img.append(black)
        else:
            obamified_img.append(darkgrey)
    newImg = Image.new("RGB", img.size)
    newImg.putdata(obamified_img)
    return newImg
