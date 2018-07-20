from PIL import Image, ImageFilter
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    img0bject = Image.open(filename)
    return img0bject
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

    darkBlue = (0, 51, 76)
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

    greyscale_img = []

    black = (0, 0, 0)
    grey1 = (105, 105, 105)
    grey2 = (170, 170, 170)
    white = (255, 255, 255)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            greyscale_img.append(black)
        elif 182 <= intensity and intensity < 364:
            greyscale_img.append(grey1)
        elif 364 <= intensity and intensity < 546:
            greyscale_img.append(grey2)
        else:
            greyscale_img.append(white)

    newImg = Image.new("RGB", img.size)
    newImg.putdata(obamified_img)
    return newImg
