import cv2
import numpy as np

# Load an image from file
image = cv2.imread("down.jpeg")
    # Define a kernel for dilation
kernel = np.ones((10, 10), np.uint8)  # You can adjust the kernel size as needed

    # Apply dilation to the image
dilated_image = cv2.dilate(image, kernel, iterations=1)

    # Display the original and dilated images

cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
