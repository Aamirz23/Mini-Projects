import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

mpHands = mp.solutions.hands

hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mpDraw = mp.solutions.drawing_utils

pTime = 0
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    all_hands = []  # ✅ ALWAYS define

    if results.multi_hand_landmarks:
        h, w, _ = img.shape

        for handLms in results.multi_hand_landmarks:
            hand_points = []

            for id in tipIds:
                lm = handLms.landmark[id]
                cx, cy = int(lm.x * w), int(lm.y * h)
                hand_points.append((cx, cy))

                cv2.circle(img, (cx, cy), 7, (0, 255, 0), cv2.FILLED)

            all_hands.append(hand_points)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # 🔥 Draw glowing lines ONLY if 2 hands detected
    if len(all_hands) == 2:
        hand1, hand2 = all_hands

        for i in range(len(tipIds)):
            x1, y1 = hand1[i]
            x2, y2 = hand2[i]

            # 🔥 Glow effect
            for thickness in range(20, 0, -5):
                overlay = img.copy()
                cv2.line(overlay, (x1, y1), (x2, y2), (255, 0, 255), thickness)
                cv2.addWeighted(overlay, 0.2, img, 0.8, 0, img)

            # Bright core line
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if pTime != 0 else 0
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()