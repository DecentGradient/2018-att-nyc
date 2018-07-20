from filters import *

#path = input("Please type the name of your image: ")

img = load_img("luffy.png")

#show_img(img)
redscale_img = redscale(img)
show_img(redscale_img)
