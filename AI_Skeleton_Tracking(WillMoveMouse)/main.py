import cv2
import mediapipe as mp

# 初始化 Mediapipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# 初始化視訊捕獲對象
cap = cv2.VideoCapture(0)  # 可以根據需要更改視訊鏡頭的索引

# 初始化 Pose 物件
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

    while True:
        # 讀取每一幀視訊
        ret, frame = cap.read()

        # 將視訊幀轉換為 RGB 格式
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 轉換為 Mediapipe 支持的格式
        img_height, img_width, _ = frame.shape
        input_img = cv2.resize(frame_rgb, (img_width, img_height))

        # 執行骨架追蹤
        results = pose.process(input_img)

        # 在視訊畫面上繪製骨架
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # 顯示視訊畫面
        cv2.imshow('AI Skeleton Tracking', frame)

        # 按下 'q' 鍵退出迴圈
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 釋放視訊捕獲對象
cap.release()

# 關閉視窗
cv2.destroyAllWindows()
