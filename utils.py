import torch

def load_model():
    # Load the YOLOv5 model from Ultralytics' YOLOv5 repository
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    # Set the model to only detect specific classes (e.g., vehicle classes)
    # Vehicle classes might be 2 (car), 3 (motorcycle), 5 (bus), and 7 (truck) in the COCO dataset
    vehicle_classes = [2, 3, 5, 7]

    # Define a wrapper function for inference to filter out unwanted classes
    def predict(image):
        results = model(image)
        # Filter results to only include specified vehicle classes
        filtered_results = results.pandas().xyxy[0]  # Use Pandas for filtering
        return filtered_results[filtered_results['class'].isin(vehicle_classes)]
    
    return predict

# Usage Example:
# model = load_model()
# results = model('path/to/image.jpg')
# print(results)
