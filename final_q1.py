import cv2

# Choose the tracker type
tracker_types = {
    "BOOSTING": cv2.legacy.TrackerBoosting_create,
    "MIL": cv2.TrackerMIL_create,
    "KCF": cv2.TrackerKCF_create,
    "TLD": cv2.legacy.TrackerTLD_create,
    "MEDIANFLOW": cv2.legacy.TrackerMedianFlow_create,
    "MOSSE": cv2.legacy.TrackerMOSSE_create,
    "CSRT": cv2.TrackerCSRT_create
}

# Initialize the tracker
tracker_type = "CSRT"  # Change this to try different trackers
tracker = tracker_types[tracker_type]()

# Open a video file or a webcam stream
video = cv2.VideoCapture("fire4.mp4")  # Replace with 0 for webcam

# Check if video opened successfully
if not video.isOpened():
    print("Could not open video")
    exit()

# Read the first frame
ok, frame = video.read()
if not ok:
    print("Cannot read video file")
    exit()

# Define an initial bounding box
bbox = cv2.selectROI(frame, False)

# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)

while True:
    # Read a new frame
    ok, frame = video.read()
    if not ok:
        break

    # Start timer
    timer = cv2.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(frame)

    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    # Draw bounding box
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display tracker type on frame
    cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

    # Display result
    cv2.imshow("Tracking", frame)

    # Exit if ESC pressed
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the ESC key
        break

# Release video capture
video.release()
cv2.destroyAllWindows()
