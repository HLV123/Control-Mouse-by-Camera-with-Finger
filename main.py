import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Cấu hình
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Trạng thái
is_left_held = False
last_right_click = False
last_left_click = False

def is_fist(landmarks):
    """Kiểm tra nắm tay"""
    fingers = []
    # Ngón cái
    if landmarks[4].x > landmarks[3].x:
        fingers.append(1)
    else:
        fingers.append(0)
    # 4 ngón còn lại
    for i in [8, 12, 16, 20]:
        if landmarks[i].y < landmarks[i-2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return sum(fingers) == 0

def is_open_palm(landmarks):
    """Kiểm tra dơ cả bàn tay"""
    fingers = []
    # Ngón cái
    if landmarks[4].x > landmarks[3].x:
        fingers.append(1)
    else:
        fingers.append(0)
    # 4 ngón còn lại
    for i in [8, 12, 16, 20]:
        if landmarks[i].y < landmarks[i-2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return sum(fingers) == 5

# Khởi tạo camera
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5) as hands:
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        
        if results.multi_hand_landmarks:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                label = handedness.classification[0].label
                landmarks = hand_landmarks.landmark
                
                # Tay phải
                if label == "Right":
                    # Ngón trỏ duỗi - di chuột
                    if landmarks[8].y < landmarks[6].y and not is_open_palm(landmarks):
                        index_tip = landmarks[8]
                        x = int(index_tip.x * screen_w)
                        y = int(index_tip.y * screen_h)
                        pyautogui.moveTo(x, y)
                        last_right_click = False  # Reset trạng thái tay phải
                    
                    # Cả bàn tay phải - click phải một lần
                    elif is_open_palm(landmarks):
                        if not last_right_click:
                            pyautogui.rightClick()
                            last_right_click = True
                
                # Tay trái
                elif label == "Left":
                    # Ngón trỏ duỗi - giữ chuột trái
                    if landmarks[8].y < landmarks[6].y and not is_open_palm(landmarks):
                        if not is_left_held:
                            pyautogui.mouseDown()
                            is_left_held = True
                        last_left_click = False  # Reset trạng thái tay trái
                    # Cả bàn tay trái - click trái một lần
                    elif is_open_palm(landmarks):
                        if not last_left_click:
                            pyautogui.click()
                            last_left_click = True
                    else:
                        if is_left_held:
                            pyautogui.mouseUp()
                            is_left_held = False
                
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        cv2.imshow('Hand Gesture Mouse Control', frame)
        
        if cv2.waitKey(5) & 0xFF == 27:  # ESC
            break

cap.release()
cv2.destroyAllWindows()