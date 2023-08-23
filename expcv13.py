import cv2
import numpy as np
cap = cv2.VideoCapture('C://Users//ILIFE//Videos//LEO//leo.mp4')
src_points = np.float32([[200, 300], [5, 2], [0, 4], [6, 0]])
dst_points = np.float32([[0, 0], [4, 0], [0, 1], [4, 6]])
M = cv2.getPerspectiveTransform(src_points, dst_points)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    transformed_frame = cv2.warpPerspective(frame, M, (frame.shape[1], frame.shape[0]))
    cv2.imshow('Perspective Transformed Video', transformed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


