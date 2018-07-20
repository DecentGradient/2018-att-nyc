# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
from PIL import Image

def load_img(filename):
    imgObject = Image.open(filename)
    return imgObject

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(img):
    img.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.

def save_img(img, filename):
  img.save(filename)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img):
    data = img.getdata()

    obamified_img = []

    darkBlue = (0,51,76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            obamified_img.append(darkBlue)
        elif 182 <= intensity and intensity < 364:
            obamified_img.append(red)
        elif 364 <= intensity and intensity < 546:
            obamified_img.append(lightBlue)
        else:
            obamified_img.append(yellow)

    newImg = Image.new ("RGB", img.size)
    newImg.putdata(obamified_img)
    return newImg
