import cv2

# Load an image from file
image = cv2.imread("down.jpeg")
    # Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the Canny edge detection
edges = cv2.Canny(gray_image, 100, 200)  # You can adjust the threshold values as needed

    # Display the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

