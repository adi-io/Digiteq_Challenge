import cv2

img = cv2.imread("emoji_0.jpg") # We can add any image that has emoji

width, height = 50, 50 #This needs to match the emoji size
x, y = 437, 284 #Here i manually add the location of the emoji for cropping

crop_img = img[y:y + height, x:x + width] #To crop

cv2.imwrite("emoji.jpg", crop_img) #To save

