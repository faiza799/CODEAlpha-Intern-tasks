import cv2
from ultralytics import YOLO

# --- 1. Load Pre-trained Model ---
# YOLOv8 nano model download hoga (fastest for real-time)
model = YOLO('yolov8n.pt')


# --- 2. Real-time Video Input ---
# 0 ka matlab hai default webcam
cap = cv2.VideoCapture(0)

print("Starting Object Detection... Press 'q' to exit.")

while cap.isOpened():
    success, frame = cap.read()

    if success:
        # --- 3. Run YOLOv8 Tracking ---
        # persist=True se object IDs save rehti hain frame-to-frame
        results = model.track(frame, persist=True)

        # --- 4. Visualize Results ---
        # Bounding boxes aur labels draw karne ke liye
        annotated_frame = results[0].plot()

        # Display output
        cv2.imshow("CodeAlpha Object Detection & Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()