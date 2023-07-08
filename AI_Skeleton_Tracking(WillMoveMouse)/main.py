# TechVidvan Human pose estimator
# import necessary packages
import win32api, win32con, win32gui
import cv2
import mediapipe as mp
import numpy as np
import pyautogui
# initialize Pose estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
screen_size = (1920, 1080)  # 螢幕的寬度和高度，根據實際情況調整
# 建立 OpenCV 視窗
cv2.namedWindow("Screen", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Screen", screen_size[0] // 2, screen_size[1] // 2)
screen_width, screen_height = pyautogui.size()
left = int((screen_width - 800) / 2)
top = int((screen_height - 600) / 2)
pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# create capture object

movemouse = False
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    # read frame from capture object

    try:
        if cv2.waitKey(1) == ord('f'):
            movemouse = True
        # convert the frame to RGB format
        RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # process the RGB frame to get the result
        results = pose.process(RGB)

        print(results.pose_landmarks)
        if results.pose_landmarks:
    # 獲取頭部關鍵點的座標
            head_landmark = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE]
            head_x = int(head_landmark.x * frame.shape[1])
            head_y = int(head_landmark.y * frame.shape[0])
    
            # 移動滑鼠到頭部座標
            pyautogui.moveTo(head_x, head_y)
           
        # draw detected skeleton on the frame
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # show the final output
        cv2.imshow('人體骨架追蹤', frame)
    except:
        break
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
