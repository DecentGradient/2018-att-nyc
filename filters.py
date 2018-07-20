from PIL import Image
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    imgObject= Image.open(filename)
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
    obamified_img = []
    black = (0,0,70)
    grey = (105,105,105)
    grey2 = (170,170,170)
    white = (255,255,255)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            obamified_img.append(black)
        elif 182 <= intensity and intensity < 364:
            obamified_img.append(grey)
        elif 364 <= intensity and intensity < 546:
            obamified_img.append(grey2)
        else:
            obamified_img.append(white)

    newImg = Image.new("RGB", img.size)
    newImg.putdata(obamified_img)
    return newImg
