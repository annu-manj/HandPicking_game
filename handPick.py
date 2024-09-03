import time
import mediapipe as mp # type: ignore
import cv2
import numpy as np
from mediapipe.framework.formats import landmark_pb2 # type: ignore
import random

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
score = 0

x_enemy = random.randint(50, 600)
y_enemy = random.randint(50, 400)

def enemy():
    global score, x_enemy, y_enemy
    cv2.circle(image, (x_enemy, y_enemy), 25, (0, 200, 0), 5)

video = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while video.isOpened():
        _, frame = video.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        imageHeight, imageWidth, _ = image.shape
        
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        
        color = (0,0,0)
        text = cv2.putText(image, "Score", (480, 30), font, 1, color, 2, cv2.LINE_AA)
        text = cv2.putText(image, str(score), (590, 30), font, 1, color, 2, cv2.LINE_AA)
        
        enemy()
        
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                )
                
                for point in mp_hands.HandLandmark:
                    normalizedLandmark = hand.landmark[point]
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                        normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight
                    )

                    if point == mp_hands.HandLandmark.INDEX_FINGER_TIP:
                        try:
                            cv2.circle(image, (pixelCoordinatesLandmark[0], pixelCoordinatesLandmark[1]), 25, (0, 200, 0), 5)

                            # Calculate the distance between index finger tip and the enemy
                            distance = np.sqrt((pixelCoordinatesLandmark[0] - x_enemy) ** 2 +
                                               (pixelCoordinatesLandmark[1] - y_enemy) ** 2)

                            # If the distance is less than a certain threshold (e.g., 25 pixels), consider it a touch
                            if distance < 25:
                                print("Touched!")
                                x_enemy = random.randint(50, 600)
                                y_enemy = random.randint(50, 400)
                                score += 1
                        except:
                            pass
        
        cv2.imshow("Hand Tracking Game", image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            print("Final Score:", score)
            break

video.release()
cv2.destroyAllWindows()
