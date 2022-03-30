# 即時辨識物件 加 用我們自己訓練的模組
import torch
import numpy as np
import cv2
import time
import speech
prev_time = 0


# import speech_recognition as sr  # 導入語音辨識模組 記得先去cmd安裝更新模組跟python
# import pyttsx3
#
# r = sr.Recognizer()
# engine = pyttsx3.init()



model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp10/weights/best.pt',force_reload=True)
# 我們自己訓練的

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue
    # frame = cv2.resize(frame,(600,480))
    # results = model(frame)
    # cv2.imshow('YOLO COCO 01', np.squeeze(results.render()))


    frame2 = cv2.resize(frame, (480, 480))
    results = model(frame2)                                 # 把frame丟到model裡面做處裡
    output_image = np.squeeze(results.render())             # 沒用squeeze 會顯示出"多維" 意義不大
    cv2.putText(output_image, f"FPS: {int(1 / (time.time()- prev_time))}",(2, 80), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)
                                                           # 記得在開頭定義prev_time = 0       輸出字體在螢幕上 弄起來可以看裡面需要什麼內容 像是 打什麼內容 位置 顏色 粗細

    prev_time = time.time()
    cv2.imshow("YOLO02", output_image)                      # 秀出畫面

    # speech.detect()
    # print(results.pandas().xyxy[0])                        #印出作標位置

    cv2.imshow('YOLO COCO 01', np.squeeze(results.render()))
    if cv2.waitKey(1) & 0xFF == 27:
        break

# def shut():
#     while cv2.waitKey(1) & 0xFF == 27:
#         break


cap.release()
cv2.destroyAllWindows()

