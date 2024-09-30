import cv2
from deepface import DeepFace
import pandas as pd
import os
from datetime import datetime

# Paths
images_path = r"C:\Users\gsais\OneDrive\Desktop\MEDITHON 24\emotion.py"
excel_path = r"C:\Users\gsais\OneDrive\Desktop\MEDITHON 24\Emo.xlsx"

# Create the images directory if it doesn't exist
if not os.path.exists(images_path):
    os.makedirs(images_path)

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start capturing video
cap = cv2.VideoCapture(0)

# Initialize variables
capture_count = 0
emotion_counts = {}
total_counts = {'total': 0, 'danger': 0, 'safe': 0}

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
        face_roi = frame[y:y + h, x:x + w]

        # Analyze the face for emotion
        try:
            analysis = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            emotion = analysis[0]['dominant_emotion']
            emotion_probability = analysis[0]['emotion'][emotion]
            capture_count += 1
            total_counts['total'] += 1

            # Update emotion counts
            if emotion not in emotion_counts:
                emotion_counts[emotion] = 0
            emotion_counts[emotion] += 1

            # Determine if the emotion is considered "danger" or "safe"
            if emotion in ['angry', 'fear']:
                total_counts['danger'] += 1
            else:
                total_counts['safe'] += 1

            # Draw rectangle around face and label with predicted emotion
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, f"{emotion} ({emotion_probability:.2f})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            
            # Save captured frame with emotion label
            image_filename = os.path.join(images_path, f"frame_{capture_count}.jpg")
            cv2.imwrite(image_filename, frame)
        except Exception as e:
            print(f"Error analyzing face: {e}")

    # Display the resulting frame
    cv2.imshow('Real-time Emotion Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()

# Save the emotion data to Excel
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%H:%M:%S")

# Create a DataFrame for the collected data
data = []
for emotion, count in emotion_counts.items():
    data.append({'Date': date_str, 'Time': time_str, 'Emotion': emotion})

df = pd.DataFrame(data)

# Save or append data to the existing Excel file
try:
    if os.path.exists(excel_path):
        with pd.ExcelWriter(excel_path, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name='EmotionData', index=False)
    else:
        with pd.ExcelWriter(excel_path, mode='w', engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='EmotionData', index=False)

    # Save the summary of counts and probabilities
    summary = {
        'Date': date_str,
        'Time': time_str,
        'Total Captures': total_counts['total'],
        'Danger Emotions': total_counts['danger'],
        'Safe Emotions': total_counts['safe'],
        'Emotion Counts': emotion_counts
    }

    summary_df = pd.DataFrame([summary])

    # Append summary to the existing Excel file
    with pd.ExcelWriter(excel_path, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
        summary_df.to_excel(writer, sheet_name='Summary', index=False)

except PermissionError as e:
    print(f"Permission Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
