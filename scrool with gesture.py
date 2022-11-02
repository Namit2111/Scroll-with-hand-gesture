import cv2
import mediapipe as mp
import time
import pyautogui
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
##cap.set(cv2.CV_CAP_PROP_FPS, 60)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)
hand_detector = mp.solutions.hands.Hands()
drawing_utils= mp.solutions.drawing_utils
s_width,s_height = pyautogui.size()
index_x,index_y,midd_y,t = 0,0,0,1
pre_x , pre_y = 0,0
while True:
    _,frame =  cap.read()
    frame = cv2.flip(frame,1)
    height , width = frame.shape[:2]
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id ,landmark in enumerate(landmarks):
                x = int(landmark.x*width)
                y = int(landmark.y*height)
                if id==8:
##                    cv2.circle(img = frame,center=(x,y),radius = 10,color=(255,255,0))
                    index_x = s_width/width*x
                    index_y = s_height/height*y
                if id == 12:
                     midd_y = s_height/height*y
                if midd_y - index_y>50:
                    t = 0
        
        if t == 0 :
            if index_x - pre_x > 300:
                pyautogui.press("right")
                
                        
                    

            if pre_x - index_x >300:
                pyautogui.press("left")
                        
            if index_y - pre_y>200:
                pyautogui.press("up")
            if pre_y - index_y > 200:
                
                pyautogui.press("down")


            
        pre_x = index_x
        pre_y = index_y
        time.sleep(0.01)
                    
            
    cv2.imshow('VM',frame)
    cv2.waitKey(1)
