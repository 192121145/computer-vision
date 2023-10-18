import cv2
original_image = cv2.imread('screen.png')
bigger_size = cv2.resize(original_image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
smaller_size = cv2.resize(original_image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Original Image', original_image)
cv2.imshow('Bigger Size', bigger_size)
cv2.imshow('Smaller Size', smaller_size)
cv2.waitKey(0)
cv2.destroyAllWindows()

