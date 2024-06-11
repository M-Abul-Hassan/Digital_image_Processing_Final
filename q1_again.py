import cv2
import numpy as np

# Callback function for trackbar
def update_image(x):
    # Get the current positions of the trackbars
    brightness = cv2.getTrackbarPos('Brightness', 'image') - 100
    contrast = cv2.getTrackbarPos('Contrast', 'image') / 50.0
    threshold = cv2.getTrackbarPos('Threshold', 'image')
    blur = cv2.getTrackbarPos('Blur', 'image')
    edge = cv2.getTrackbarPos('Edge Detection', 'image')

    # Adjust brightness and contrast
    adjusted = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)

    # Apply Gaussian Blur if blur trackbar is not at 0
    if blur > 0:
        ksize = (2 * blur + 1, 2 * blur + 1)  # kernel size must be odd
        adjusted = cv2.GaussianBlur(adjusted, ksize, 0)

    # Apply threshold if threshold trackbar is not at 0
    if threshold > 0:
        _, adjusted = cv2.threshold(adjusted, threshold, 255, cv2.THRESH_BINARY)

    # Apply edge detection if edge detection trackbar is not at 0
    if edge > 0:
        adjusted = cv2.Canny(adjusted, 50, 150)

    # Display the updated image
    cv2.imshow('image', adjusted)

# Load an image
img = cv2.imread('image.jpg')  # Replace with your image path
if img is None:
    print("Error loading image")
    exit()

# Create a window
cv2.namedWindow('image')

# Create trackbars for adjusting brightness, contrast, threshold, blur, and edge detection
cv2.createTrackbar('Brightness', 'image', 100, 200, update_image)
cv2.createTrackbar('Contrast', 'image', 50, 100, update_image)
cv2.createTrackbar('Threshold', 'image', 0, 255, update_image)
cv2.createTrackbar('Blur', 'image', 0, 20, update_image)
cv2.createTrackbar('Edge Detection', 'image', 0, 1, update_image)

# Display the original image
cv2.imshow('image', img)

# Wait until user presses the ESC key
while True:
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the ESC key
        break

# Destroy all windows
cv2.destroyAllWindows()
