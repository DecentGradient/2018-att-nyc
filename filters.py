# Rename this file to be "filters.py"
# Add commands to import modules here.

from PIL import Image, ImageFilter
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
# the PIL.Image.open doesn't need the PIL part, its the more formal version
# you can use Image.open(path)
#filename, mode = 'r' is optional
def load_img(filename):
    imgObject = Image.open(filename, mode = 'r')
    return imgObject
# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(imgname):
    imgname.show()

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

    obamafied_img = []

    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]

        if intensity < 182:
            obamafied_img.append(darkBlue)

        elif 182 <= intensity and intensity < 364:
            obamafied_img.append(red)

        elif 364 <= intensity and intensity < 546:
            obamafied_img.append(lightBlue)

        else:
            obamafied_img.append(yellow)

    newImg = Image.new("RGB", img.size)
    newImg.putdata(obamafied_img)
    return newImg

def grayscale(img):
    data = img.getdata()

    grayscale_img = []

    black = (0, 0, 0)
    gray1 = (105, 105, 105)
    gray2 = (170, 170, 170)
    gray3 = (255, 255, 255)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]

        if intensity < 182:
            grayscale_img.append(black)

        elif 182 <= intensity and intensity < 364:
            grayscale_img.append(gray1)

        elif 364 <= intensity and intensity < 546:
            grayscale_img.append(gray2)

        else:
            grayscale_img.append(gray3)

    newImg = Image.new("RGB", img.size)
    newImg.putdata(grayscale_img)
    return newImg

def redscale(img):
    data = img.getdata()

    redscale_img = []

    burgundy = (102, 0, 0)
    red1 = (153, 0, 0)
    red2 = (255, 0, 0)
    red3 = (255, 204, 204)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]

        if intensity < 182:
            redscale_img.append(burgundy)

        elif 182 <= intensity and intensity < 364:
            redscale_img.append(red1)

        elif 364 <= intensity and intensity < 546:
            redscale_img.append(red2)

        else:
            redscale_img.append(red3)

    newImg = Image.new("RGB", img.size)
    newImg.putdata(redscale_img)
    return newImg
