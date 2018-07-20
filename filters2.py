# Rename this file to be "filters.py"
from PIL import Image, ImageFilter
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(path): #converts the image to something python could read
    imgObject = Image.open(path)
    return imgObject

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(imgName): #shows the image
    imgName.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imgName, path): #names and saves the image
    imgName.save(path)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def grayscale(img):
    data = img.getdata()
    grayscale_img = []
    black = (0,0,0)
    gray1 = (96,96,96)
    gray2 = (160,160,160)
    gray3 = (224,224,224)
    white = (255,255,255)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 100:
            grayscale_img.append(black)
        elif 100 <= intensity and intensity < 350:
            grayscale_img.append(gray1)
        elif 350 <= intensity and intensity < 550:
            grayscale_img.append(gray2)
        elif 550 <= intensity and intensity < 750:
            grayscale_img.append(gray3)
        elif intensity >= 750:
            grayscale_img.append(white)

    newImg = Image.new("RGB", img.size)
    newImg.putdata(grayscale_img)
    return newImg
