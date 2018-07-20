from PIL import Image
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


def show_img(img):
    #in gerogias it is white
    img.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imgname,filename):
    imgname.save(filename)

def obamicon(img):
    data = img.getdata()

    obamified_img=[]

    darkBlue=(0,51,76)
    red= (217,26,33)
    lightBlue=(112,150,158)
    yellow= (255,255,0)
#LOOPS
    for pixel in data:
        #pixel=(45,145,23) --> intensity=45+145+23=213
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            obamified_img.append(darkBlue)
        elif 182 <=intensity and intensity < 364:
            obamified_img.append(red)
        elif 364 <= intensity and intensity < 546:
            obamified_img.append(lightBlue)
        elif intensity >= 546:
            obamified_img.append(yellow)

    newImg = Image.new ("RGB", img.size)
    newImg.putdata(obamified_img)
    return newImg

def beautiful(img):
    data = img.getdata()

    rainbow_img =[]

    lightBlue=(92,235,255)
    pink= (255,57,215)
    yellow=(255,255,0)
    purple= (161,40,232)

#LOOPS
    for pixel in data:
        #pixel=(45,145,23) --> intensity=45+145+23=213
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            rainbow_img.append(lightBlue)
        elif 182 <=intensity and intensity < 364:
            rainbow_img.append(purple)
        elif 364 <= intensity and intensity < 546:
            rainbow_img.append(yellow)
        elif intensity >= 546:
            rainbow_img.append(pink)

    newImg = Image.new ("RGB", img.size)
    newImg.putdata(rainbow_img)
    return newImg
