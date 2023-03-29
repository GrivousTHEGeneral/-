# opencv object tracking
# object detection and tracking opencv
import cv2
import numpy as np

# Load Yolo
yolo_weight = "yolov3.weights"
yolo_config = "yolov3.cfg"
coco_labels = "coco.names"
net = cv2.dnn.readNet(yolo_weight, yolo_config)

classes = []
with open(coco_labels, "r") as f:
    classes = [line.strip() for line in f.readlines()]
num_classes = len(classes)
target_lables = ["person", "bottle"]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(num_classes, 3))
# Defining desired shape
fWidth = 800
fHeight = 600

# Below function will read video frames
cap = cv2.VideoCapture(0)

while True:
    read_ok, img = cap.read()

    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_DUPLEX
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            if label in target_lables:
                confidence_label = int(confidences[i] * 100)
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, f'{label, confidence_label}', (x - 0, y + 25), font, 1, color, 2)
                if label == "bottle":
                    cv2.putText(img, "Person drink", (int(0.5 * (x + w)), int(0.5 * (y + h + y))), font, 1, color, 2)
            else:
                continue
    cv2.imshow("Image", img)
    # Close video window by pressing 'x'
    if cv2.waitKey(1) & 0xFF == ord('0'):
        break
