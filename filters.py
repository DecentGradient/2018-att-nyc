from PIL import Image
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    imgname = Image.open(filename)
    return imgname


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.

def show_img(imgname):
    imgname.show()

def obamicon(img):
    data = img.getdata()

    obamifield_img = []

    yellow = (0, 0, 0)
    green = (244, 250, 98)
    lightBlue = (0, 0, 0)
    white = (300, 227, 66)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 90:
            obamifield_img.append(yellow)
        elif 90 < intensity and intensity < 364:
            obamifield_img.append(green)
        elif 275 <= intensity and intensity < 489:
            obamifield_img.append(lightBlue)
        else:
            obamifield_img.append(white)

    newImg = Image.new("RGB", img.size)
    newImg.putdata(obamifield_img)
    return newImg

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
#def save_img(imgname, filename):
    imgname.save(filename)

#def image.getdata


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
#def obamicon():
