from PIL import Image, ImageFilter
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
        #pixel = (45, 145, 23)
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            obamified_img.append(darkBlue)
        elif 182 <= intensity and intensity < 364:
            obamified_img.append(red)
        elif 364 <= intensity < 546:
            obamified_img.append(lightBlue)
        #or use elif intensity >= 546
        #obamified_img.append(yellow)
        else:
            obamified_img.append(yellow)

    newImg = Image.new("RGB", img.size)
    newImg.putdata(obamified_img)
    return newImg



    #def colorful(img):
        #data = img.getdata()

        #colors_img = []

        #lightBlue = (204, 252, 235)
        #blue = (158, 216, 196)
        #green = (51, 247, 136)
        #darkGreen = (22, 173, 87)

        #for pixel in data:
            #pixel = (45, 145, 23)
            #intensity = pixel[0] + pixel[1] + pixel[2]
            #if intensity < 182:
                #colors_img.append(lightBlue)
            #elif 182 <= intensity and intensity < 364:
                #colors_img.append(blue)
            #elif 364 <= intensity < 546:
                #colors_img.append(green)
            #or use elif intensity >= 546
            #colors_img.append(yellow)
            #else:
                #colors_img.append(darkGreen)

        #newImg = Image.new("RGB", img.size)
        #newImg.putdata(colors_img)
        #return newImg
