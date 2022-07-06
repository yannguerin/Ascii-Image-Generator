import cv2
import math

# Some Ascii Character lists
ascii_long = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,^'. "
ascii_short = "  .:-=+*#%@"
ascii_short_rev = "@%#*+=-:.    "

# Reads the image and first converts it to grayscale
img = cv2.imread('high_contrast.jpeg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('high_contrast.jpeg', cv2.IMREAD_GRAYSCALE)

# Getting the shape of the image
x, y, d = img.shape

# The pixel size variable determines how detailed the image in ASCII will be, 1 means each pixel is converted to ascii, 
# while 5 would mean each 5x5 pixel area would be converted
pixel_size = 1

# Uncomment the line below to have a view of the original show up
#cv2.imshow('Original', img)
char_rows = []

# Loops through every second pixel (* pixel size if not one) in X direction. Every second is used since most fonts show characters as taller than wide by about 2
for x_val in range(0, x, pixel_size*2):
    char_cols = []
    # Loop through every pixel in Y direction by pixel size increments
    for y_val in range(0, y, pixel_size):
        px_color = img[x_val, y_val]
        gray_px = img_gray[x_val, y_val]
        # Find the single ASCII char that best represents the gray color of the pixel
        single_char = ascii_short_rev[math.floor((gray_px//len(ascii_short_rev))/2.5) - 1]
        char_cols.append(single_char)
        localmax_x = x_val + pixel_size*2
        localmax_y = y_val + pixel_size
        img[x_val:localmax_x, y_val:localmax_y] = px_color
    char_rows.append(''.join(char_cols))

# Saves ASCII characters to a text file
formatted_for_save = '\n'.join(char_rows)
text_file = open('ascii_img.txt', 'w+')
text_file.write(formatted_for_save)
text_file.close()

# Shows the pixelated view of the image, to the level of pixelation determined by pixel_size
cv2.imshow('Pixelated', img)
# Press any key to terminate the program
cv2.waitKey(0)
cv2.destroyAllWindows()
