import cv2
import numpy as np

# Callback function for trackbar (does nothing but required by createTrackbar)
def nothing(x):
    pass

# Create a black image
img = np.zeros((300, 512, 3), np.uint8)

# Create a window
cv2.namedWindow('image')

# Create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

while True:
    # Get the current positions of the trackbars
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')

    # Update the image color
    img[:] = [b, g, r]

    # Display the image
    cv2.imshow('image', img)

    # Break the loop when 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the ESC key
        break

# Destroy all windows
cv2.destroyAllWindows()
