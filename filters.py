from PIL import Image, ImageFilter
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    imgObject = Image.open(filename)
    #im = Image.open(path)
    #return im
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


    obamafield_img = []

    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue = (112, 150,158)
    yellow = (252,227,166)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            obamafield_img.append(darkBlue)
        elif 182 <= intensity and intensity < 364:
            obamafield_img.append(red)
        elif 364 <= intensity and intensity < 546:
            obamafield_img.append(lightBlue)
        else:
            obamafield_img.append(yellow)

    newImg = Image.new("RGB",img.size)
    newImg.putdata(obamafield_img)
    return newImg


def greyscale(img):
    data = img.getdata()


    greyfield_img = []

    black = (0,0,0)
    grey1 = (105,105,105)
    grey2 = (170, 170,170)
    white = (255,255,255)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            greyfield_img.append(black)
        elif 182 <= intensity and intensity < 364:
            greyfield_img.append(grey1)
        elif 364 <= intensity and intensity < 546:
            greyfield_img.append(grey2)
        else:
            greyfield_img.append(white)

    newImg = Image.new("RGB",img.size)
    newImg.putdata(greyfield_img)
    return newImg




def ownscale(img):
    data = img.getdata()


    ownfield_img = []

    black = (0,0,0)
    own1 = (155,125,175)
    own2 = (120, 170,120)
    own3 = (205,155,145)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            ownfield_img.append(black)
        elif 182 <= intensity and intensity < 364:
            ownfield_img.append(own1)
        elif 364 <= intensity and intensity < 546:
            ownfield_img.append(own2)
        else:
            ownfield_img.append(own3)

    newImg = Image.new("RGB",img.size)
    newImg.putdata(ownfield_img)
    return newImg






def ownscale(img):
    data = img.getdata()


    randomfield_img = []

    random1 = (189,189,189)
    random2 = (135,165,185)
    random3 = (180, 110,194)
    random4 = (205,155,145)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            randomfield_img.append(random1)
        elif 182 <= intensity and intensity < 364:
            randomfield_img.append(random2)
        elif 364 <= intensity and intensity < 546:
            randomfield_img.append(random3)
        else:
            randomfield_img.append(random4)

    newImg = Image.new("RGB",img.size)
    newImg.putdata(randomfield_img)
    return newImg
