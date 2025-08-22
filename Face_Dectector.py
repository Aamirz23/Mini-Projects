import cv2
import time

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
photo_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab a frame!")
        break
 # Convert to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

 # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    for(x, y , w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if len(faces) > 0:
        photo_count += 1

        filename = f"face_photo_{photo_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"[INFO] Face detected. Photo saved as {filename}")
        time.sleep(2)  # Pause for 2 seconds to avoid rapid multiple captures

        cv2.imshow("Face Detector", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
