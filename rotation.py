import cv2
original_image = cv2.imread('screen.png')
height, width = original_image.shape[:2]
clockwise_rotation_angle = 45
counterclockwise_rotation_angle = -45
clockwise_rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), clockwise_rotation_angle, 1)
counterclockwise_rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), counterclockwise_rotation_angle, 1)
rotated_clockwise = cv2.warpAffine(original_image, clockwise_rotation_matrix, (width, height))
rotated_counterclockwise = cv2.warpAffine(original_image, counterclockwise_rotation_matrix, (width, height))
cv2.imshow('Original Image', original_image)
cv2.imshow('Clockwise Rotation', rotated_clockwise)
cv2.imshow('Counterclockwise Rotation', rotated_counterclockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()
