# main.py
from src.detect_accident import detect_accident
from src.alert_service import send_email_alert

def main():
    video_path =r"D:\real_time_accident_detection\test 2 video.mp4"  # Example video path
    if detect_accident(video_path):
        print("Accident detected! Sending alerts...")
        send_email_alert()
    else:
        print("No accidents detected.")

if __name__ == "__main__":
    main()
