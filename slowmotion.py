import cv2

video_capture = cv2.VideoCapture('video.mp4')
if not video_capture.isOpened():
    print("Error: Video not found or could not be opened.")
    exit()
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
slow_motion_factor = 0.5
fast_motion_factor = 10.5
while True:
    ret, frame = video_capture.read()

    if not ret:
        break
    cv2.imshow('Video (Slow Motion)', frame)
    cv2.waitKey(int(1000 / (video_capture.get(cv2.CAP_PROP_FPS) * slow_motion_factor)))
    cv2.imshow('Video (Fast Motion)', frame)
    cv2.waitKey(int(1000 / (video_capture.get(cv2.CAP_PROP_FPS) * fast_motion_factor)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  
video_capture.release()
cv2.destroyAllWindows()

