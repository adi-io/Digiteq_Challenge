import numpy as np;
import cv2;
import sys;

def is_emoji_found(window, emoji_grey):
    diff = cv2.absdiff(window, emoji_grey) #To calulate the pixel by pixel differce
    return (np.max(diff) < 150) #if you are false positive, decrease the number; if false negative, tben increase the number.

emoji_path = "emoji.jpg"
step_size = 1
x = 0
y = 0
i = 0

#Simmple error checking machnism
if (len(sys.argv) != 2):
    print("One argumnet prosim :)")
    sys.exit()

image_path = sys.argv[1]

if not (image_path.lower().endswith('.jpg')):
            print("Only .jpg files prosim :)")
            sys.exit()

image = cv2.imread(image_path)
emoji = cv2.imread(emoji_path)

if (image is None):
    print("Picture not present in the dataset")
    sys.exit()

#coverting image to greyscale makes our current analysis simpler, also it makes the .shape function to only output two values
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
emoji_grey = cv2.cvtColor(emoji, cv2.COLOR_BGR2GRAY)

emoji_height, emoji_width = emoji_grey.shape    #shape function to height and width of the image
image_height, image_width = image_grey.shape

while y <= (image_height - emoji_height):
    x = 0
    while x <= (image_width - emoji_width):
        window = image_grey[y:y + emoji_height, x:x + emoji_width]  #add the 50x50 scanning area to the window
        if (is_emoji_found(window, emoji_grey)):
            print(f"Dwag we found Emoji at: ({x}, {y})")
            i = 1
            #break #if you want to stop at the first emoji, please remove the comment from break

        x += step_size  #the area that we skip after one iteration, it is dyanamically allocated
    y += step_size

if (i == 0):
    print("No emoji for you dwag")
