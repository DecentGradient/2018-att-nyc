from PIL import Image, ImageFilter
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


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img):
    data = img.getdata()
    obamafied_img = []
    dark_Blue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)
    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            obamafied_img.append(dark_Blue)
        elif 182 <= intensity and intensity < 364:
            obamafied_img.append(red)
        elif 364 <= intensity and intensity < 546:
            obamafied_img.append(lightBlue)
        else:
            obamafied_img.append(yellow)
    newImg = Image.new("RGB", img.size)
    newImg.putdata(obamafied_img)
    return newImg
def grayscale(img):
    data = img.getdata()
    grayscale_img = []
    black = (0, 0, 0)
    darkgrey = (169, 169, 169)
    lightgrey = (211, 211, 211)
    white = (255, 255, 255)
    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            grayscale_img.append(black)
        elif 182 <= intensity and intensity < 364:
            grayscale_img.append(darkgrey)
        elif 364 <= intensity and intensity < 546:
            grayscale_img.append(lightgrey)
        else:
            grayscale_img.append(white)
    newImg = Image.new("RGB", img.size)
    newImg.putdata(grayscale_img)
    return newImg
def pinkscale(img):
    data = img.getdata()
    pinked_img = []
    deeppink = (255,20,147)
    hotpink = (255,105,180)
    lightpink = (255,182,193)
    pink = (255,192,203)
    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            pinked_img.append(deeppink)
        elif 182 <= intensity and intensity < 364:
            pinked_img.append(hotpink)
        elif 364 <= intensity and intensity < 546:
            pinked_img.append(lightpink)
        else:
            pinked_img.append(pink)
    newImg = Image.new("RGB", img.size)
    newImg.putdata(pinked_img)
    return newImg
def pls(img):
    data = img.getdata()
    pls_img = []
    dark_Blue = (255,20,147)
    darkpurple = (148,0,211)
    purple = (128,0,128)
    blue = (0, 0, 255)
    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            pls_img.append(dark_Blue)
        elif 182 <= intensity and intensity < 364:
            pls_img.append(darkpurple)
        elif 364 <= intensity and intensity < 546:
            pls_img.append(purple)
        else:
            pls_img.append(blue)
    newImg = Image.new("RGB", img.size)
    newImg.putdata(pls_img)
    return newImg
def skip(img):
    data = img.getdata()
    skip_img = []
    deeppink = (255,20,147)
    hotpink = (255,105,180)
    lightpink = (255,182,193)
    pink = (255,192,203)
    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            skip_img.append(deeppink)
        elif 182 < intensity and intensity < 364:
            skip_img.append(hotpink)
        elif 364 < intensity and intensity < 546:
            skip_img.append(lightpink)
        else:
            skip_img.append(pink)
    newImg = Image.new("RGB", img.size)
    newImg.putdata(skip_img)
    return newImg
def skipper(img):
    data = img.getdata()
    ski_img = []
    deeppink = (255,20,147)
    hotpink = (255,105,180)
    lightpink = (255,182,193)
    pink = (255,192,203)
    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 180:
            ski_img.append(deeppink)
        elif 184 < intensity and intensity < 360:
            ski_img.append(hotpink)
        elif 400 < intensity and intensity < 546:
            ski_img.append(lightpink)
        else:
            ski_img.append(pink)
    newImg = Image.new("RGB", img.size)
    newImg.putdata(ski_img)
    return newImg
