from PIL import Image, ImageFilter
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    im = Image.open(filename)
    return im


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
#def obamicon():
def obamicon(img):
    data = img.getdata()

    obamified_img = []

    darkblue = (0, 51, 76)
    red = (217, 26, 33)
    lightblue = (112, 150, 158)
    yellow = (252, 227, 166)

    for pixel in data:
        #pixel11 = (45, 145, 23) --> intensity = 45 + 145 + 23 + 213
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            obamified_img.append(darkblue)
        elif 182 <= intensity and intensity < 364:
            obamified_img.append(red)
        elif 364 <= intensity and intensity < 546:
            obamified_img.append(lightblue)
        else:
            obamified_img.append(yellow)

    newImg = Image.new("RGB", img.size)
    newImg.putdata(obamified_img)
    return newImg

    def Pinkscale(img):
        data = img.getdata()

        pink_img = []

        pink = (0, 51, 76)
        red = (217, 26, 33)
        grey = (112, 150, 158)
        yellow = (252, 227, 166)

        for pixel in data:
            #pixel11 = (45, 145, 23) --> intensity = 45 + 145 + 23 + 213
            intensity = pixel[0] + pixel[1] + pixel[2]
            if intensity < 182:
                pink_img.append(pink)
            elif 182 <= intensity and intensity < 364:
                pink_img.append(red)
            elif 364 <= intensity and intensity < 546:
                pink_img.append(grey)
            else:
                pink_img.append(yellow)

        newImg = Image.new("RGB", img.size)
        newImg.putdata(pink_img)
        return newImg
