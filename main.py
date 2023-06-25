import cv2
import mediapipe as mp

finger_tips = [8, 12, 16, 20]
thumb_tip = 4

# Initialising default webcam
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()  # Initialises a hand object
mpDraw = mp.solutions.drawing_utils # Initialising drawing module to draw landmarks

while True:

    success, img = cap.read()  # Reading each frame and storing in img
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # OpenCV takes image in BGR format, so first we convert it to RGB
    # format
    results = hands.process(imgRGB)  # Process the image and identify the hands

    # multi_hand_landmarks detects hands and returns a list of 21 landmarks
    if results.multi_hand_landmarks:  # If any hand is detected
        for handLms in results.multi_hand_landmarks:  # Iterate over all the hands detected in frame
            lm_list = []
            for lm in handLms.landmark: # Iterate over all landmarks in a hand
                lm_list.append(lm)
            #STOP
            if lm_list[8].y < lm_list[7].y and lm_list[12].y < lm_list[11].y and lm_list[16].y < lm_list[15].y and \
                    lm_list[20].y < lm_list[19].y and lm_list[4].y < lm_list[3].y and lm_list[12].y < lm_list[9].y < \
                    lm_list[0].y:
                cv2.putText(img, 'STOP', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

            # YOO
            if lm_list[8].y < lm_list[7].y and lm_list[16].y > lm_list[15].y and \
                    lm_list[20].y < lm_list[19].y and lm_list[12].y > lm_list[9].y:
                cv2.putText(img, 'YOOO', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

            # AWESOME
            if lm_list[7].y < lm_list[8].y < lm_list[4].y and lm_list[12].y < lm_list[11].y and \
                    lm_list[16].y < lm_list[15].y and \
                    lm_list[20].y < lm_list[19].y and lm_list[4].y < lm_list[3].y and lm_list[12].y < lm_list[9].y < \
                    lm_list[0].y:
                cv2.putText(img, 'AWESOME', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

            # PEACE
            if lm_list[8].y < lm_list[7].y and lm_list[12].y < lm_list[11].y and lm_list[16].y > lm_list[15].y and \
                    lm_list[20].y > lm_list[19].y and lm_list[4].y < lm_list[3].y:
                cv2.putText(img, 'PEACE', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

            finger_fold_status = []
            if lm_list[0].x < lm_list[9].x:  # If hand is Left Hand
                for tip in finger_tips:
                    print('LEFT HAND')
                    if lm_list[tip].x < lm_list[tip-3].x:
                        finger_fold_status.append(True)
                    else:
                        finger_fold_status.append(False)
            else:  # Hand is Right
                for tip in finger_tips:
                    print('RIGHT HAND')
                    if lm_list[tip].x > lm_list[tip - 3].x:
                        finger_fold_status.append(True)
                    else:
                        finger_fold_status.append(False)
            # print(finger_fold_status)

            if all(finger_fold_status):
                if lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y:
                    print("THUMBS UP")
                    cv2.putText(img, "THUMBS UP", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

                if lm_list[thumb_tip].y > lm_list[thumb_tip-1].y > lm_list[thumb_tip-2].y:
                    print("THUMBS DOWN")
                    cv2.putText(img, "THUMBS DOWN", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            # HAND_CONNECTIONS connects or draws the lines
            # draw_landmarks draws all 21 points in a hand using img and landmarks (handLms)

    cv2.imshow("HAND GESTURES", img)  # Shows the camera input. We can give any name instead of 'Image'
    cv2.waitKey(1)  # To hold the output window
