from PIL import Image, ImageFilter
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    imgObject = Image.open(filename)
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

def bright(img):
    data = img.getdata()

    bright = []

    blue = (153, 255, 255)
    pink = (255, 153, 204)
    yellow = (255, 255, 102)
    white = (255, 255, 255)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 200:
            bright.append(blue)
        elif 200 <= intensity and intensity < 300:
            bright.append(pink)
        elif 300 <= intensity and intensity < 400:
            bright.append(yellow)
        else:
            bright.append(white)

    newImg = Image.new("RGB", img.size)
    newImg.putdata(bright)
    return newImg
