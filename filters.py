
from PIL import Image

def load_img(filename):
    imgObject = Image.open(filename)
    return imgObject

def show_img(imgObject):
    imgObject.show()

def save_img(imgObject, filename):
    imgObject.save(filename)

def bluescale(imgObject):
    data = imgObject.getdata()

    sarah_img = []

    black = (0, 0, 0)
    darkblue = (0, 38, 51)
    blue = (0, 115, 153)
    lightblue = (0, 191, 255)
    slightblue = (102, 217, 255)
    slightishblue = (203, 242, 255)
    whiteblue = (204, 242, 255)
    white = (255, 255, 255)

    for pixel in data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity >= 0 and intensity < 182:
            sarah_img.append(black)
        elif intensity >= 182 and intensity < 276:
            sarah_img.append(darkblue)
        elif intensity >= 276 and intensity < 364:
            sarah_img.append(blue)
        elif intensity >= 364 and intensity < 489:
            sarah_img.append(lightblue)
        elif intensity >= 489 and intensity < 574:
            sarah_img.append(slightishblue)
        elif intensity >= 574 and intensity < 663:
            sarah_img.append(whiteblue)
        else:
            sarah_img.append(white)

    newImg = Image.new("RGB", imgObject.size)
    newImg.putdata(sarah_img)
    return newImg
