import cv2

# Read input image
input_image = cv2.imread('image.jpg')  # Replace 'input_image.jpg' with your image path

# Check if image is loaded successfully
if input_image is None:
    print("Error loading image")
    exit()

# Convert image to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
