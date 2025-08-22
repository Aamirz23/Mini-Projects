import cv2
import time

# Load the Haar cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture
cap = cv2.VideoCapture(0)
photo_taken = False  # Flag to avoid taking multiple photos quickly

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for faster processing
    frame = cv2.resize(frame, (640, 400))

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.1, 
        minNeighbors=6, 
        minSize=(120, 120)
    )

    # If face(s) detected
    if len(faces) > 0:
        # Draw rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Take a photo only once per detection
        if not photo_taken:
            timestamp = int(time.time())
            filename = f"face_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"[INFO] Photo saved: {filename}")
            photo_taken = True
            photo_timer = time.time()

    # Reset the photo flag after 3 seconds
    if photo_taken and time.time() - photo_timer > 6:
        photo_taken = False

    # Display the result
    cv2.imshow("Smooth Face Detector", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
