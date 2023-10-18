import cv2
import numpy as np

# Load an image from file
image = cv2.imread("down.jpeg")

    # Define a kernel for erosion
kernel = np.ones((5, 5), np.uint8)  # You can adjust the kernel size as needed

    # Apply erosion to the image
eroded_image = cv2.erode(image, kernel, iterations=1)

    # Display the original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

