# importing the required packages
import pyautogui
import cv2
import numpy as np

# Specify resolution
resolution = (1920, 1080)
tracker = cv2.legacy.TrackerCSRT_create()
# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "Recording1.avi"

# Specify frames rate. We can choose any
# value and experiment with it
fps = 60.0


# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)
cap =  pyautogui.screenshot()

success, frame = cap.read()
bbox = cv2.selectROI("Tracking",frame, False)
tracker.init(frame, bbox)

def drawBox(img,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3 )
    cv2.putText(img, "Tracking", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # cv2.rectangle(img,(15,15),(200,90),(255,0,255),2)
    # cv2.putText(img, "Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 2);
    # Write it to the output file
    out.write(frame)

    # Optional: Display the recording screen
    cv2.imshow('Live', frame)
    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img, "Lost", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.rectangle(img,(15,15),(200,90),(255,0,255),2)
    cv2.putText(img, "Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 2);
    cv2.putText(img, "Status:", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2);


    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    if fps>60: myColor = (20,230,20)
    elif fps>20: myColor = (230,20,20)
    else: myColor = (20,20,230)
    cv2.putText(img,str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2);

    cv2.imshow("Tracking", img)

    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
