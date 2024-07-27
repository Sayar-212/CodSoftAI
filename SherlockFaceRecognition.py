import cv2
import numpy as np
import face_recognition
import os

# Initialize lists for storing known face encodings and their names
known_face_encodings = []
known_face_names = []

# Load the known face "Sample2.jpg" from the file system
def load_known_face():
    # Path to the known face image
    known_face_image_path = "/home/kiit/CodsoftAI/Sample2.jpg"
    
    # Check if the file exists
    if not os.path.exists(known_face_image_path):
        print(f"File not found: {known_face_image_path}")
        return
    
    # Load the image file
    image = face_recognition.load_image_file(known_face_image_path)
    
    # Generate the face encoding for the person in the image
    encoding = face_recognition.face_encodings(image)[0]
    
    # Append the encoding and the person's name to the respective lists
    known_face_encodings.append(encoding)
    known_face_names.append("Sample2")

# Load the known face
load_known_face()

# Path to the input image for face detection and recognition
image_path = "/home/kiit/CodsoftAI/Sample2.jpg"

# Check if the file exists before proceeding
if not os.path.exists(image_path):
    print(f"File not found: {image_path}")
else:
    # Load the input image
    image = face_recognition.load_image_file(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Find all the faces and face encodings in the input image
    face_locations = face_recognition.face_locations(rgb_image)
    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    # List to store the names of detected faces
    face_names = []
    for face_encoding in face_encodings:
        # Check if the face matches any known face encoding
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = None  # Set default to None instead of "Unknown"

        # Find the closest match
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    # Draw boxes around detected faces and label them
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Draw a box around the face
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

        if name:
            # Draw a label with the name below the face
            cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Convert the image back to BGR for OpenCV display
    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Display the resulting image
    cv2.imshow('Image', bgr_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
