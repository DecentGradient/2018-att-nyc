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


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imgname, filename):
    imgname.save(filename)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
#def show_img():


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
#def save_img():


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img):
    data = img.getdata()

    obamified_img = []

    darkBlue = (0, 0, 255)
    red = (255, 0, 0)
    lightBlue =(0, 255, 0)
    yellow = (204, 51, 255)

    for pixel in data:
        #pixel1 = (45, 145, 23)
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            obamified_img.append(darkBlue)
        elif 182 < intensity and intensity < 364:
            obamified_img.append(red)
        elif 364 <= intensity and intensity <546:
            obamified_img.append(lightBlue)
        else:
            obamified_img.append(yellow)


    newImg = Image.new("RGB", img.size)
    newImg.putdata(obamified_img)
    return newImg
