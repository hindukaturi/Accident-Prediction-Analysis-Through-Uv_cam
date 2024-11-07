import cv2
import tensorflow as tf
import numpy as np

def detect_accident(video_path):
    # Load the pretrained model
    model_path = r'D:\real_time_accident_detection\model\model.h5'
    model = tf.keras.models.load_model(model_path)

    # Define classes for accidents and non-accidents
    CLASSES = {0: "Non-Accident", 1: "Accident"}

    def preprocess_frame(frame):
        """Preprocess video frame for model prediction."""
        frame = cv2.resize(frame, (224, 224))  # Resize to model input size
        frame = frame / 255.0  # Normalize
        frame = np.expand_dims(frame, axis=0)  # Add batch dimension
        return frame

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Couldn't open video.")
        return False
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Exit when no frames are left
        
        # Preprocess the frame and predict
        processed_frame = preprocess_frame(frame)
        predictions = model.predict(processed_frame)
        predicted_class = np.argmax(predictions)
        confidence = predictions[0][predicted_class]  # Confidence of the prediction

        label = CLASSES[predicted_class]
        print(f"Prediction: {label} | Confidence: {confidence:.2f}")

        # Display the frame with prediction
        cv2.putText(frame, f"{label} ({confidence:.2f})", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Video Frame", frame)

        # Stop the video if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return True  # Indicating that the video was processed successfully

# Example usage
video_path = r'D:\real_time_accident_detection\test 2 video.mp4'
detect_accident(video_path)