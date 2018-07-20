#Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image , ImageFilter
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
def save_img(imgname , filename):
    imgname.save(filename)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img):
    data = img.getdata()

    obamaifield_img = []

    pink = (100, 175, 57)
    turquoise = (79, 9, 78)
    blue = (0, 0 , 78)
    green = (15, 0 , 0)

    for pixel in data:
        #pixel = (45, 145, 23) --> intesity = 45 + 145 + 23 = 213
        intesity = pixel[0] + pixel[1] + pixel[2]
        if intesity < 182:
            obamaifield_img.append(pink)
        elif 182 <= intesity and intesity < 364:
            obamaifield_img.append(turquoise)
        elif 364 <= intesity and intesity < 546:
             obamaifield_img.append(blue)
        else:
             obamaifield_img.append(green)

    newImg = Image.new("RGB" , img.size)
    newImg.putdata(obamaifield_img)
    return newImg
