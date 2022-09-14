import cv2

############### Tracker Types #####################

#tracker = cv2.TrackerBoosting_create()
#tracker = cv2.TrackerMIL_create()
#tracker = cv2.TrackerKCF_create()
#tracker = cv2.TrackerTLD_create()

trackers = cv2.legacy.MultiTracker_create()
#tracker = cv2.legacy.TrackerMOSSE_create()

########################################################


cap = cv2.VideoCapture('Four trap.mp4')
#cap = cv2.VideoCapture('2')
# TRACKER INITIALIZATION
#ret, frame = cap.read()
#bbox = cv2.selectROI("Tracking",frame, False)
#tracker.init(frame, bbox)

success, frame = cap.read()

k=5

for i in range (k):
    cv2.imshow('Frame',frame)
    bbox_i = cv2.selectROI('Frame',frame)
    tracker_i = cv2.legacy.TrackerTLD_create()
    trackers.add(tracker_i,frame,bbox_i)

# def drawBox(img,bbox):
#      x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
#      cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3 )
#      cv2.putText(img, "Tracking", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
def drawBox(img,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3 )
    cv2.putText(img, "Tracking", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


while True:


    timer = cv2.getTickCount()
     # f = open("test.txt","a")
     # f.write(str(bbox))
     # f.write('\n')
    if success:
         drawBox(frame,bbox_i)
    else:
         cv2.putText(frame, "Lost", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.rectangle(frame,(15,15),(200,90),(255,0,255),2)
    cv2.putText(frame, "Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 2);
    cv2.putText(frame, "Status:", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2);
    #
    #
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    if fps>60: myColor = (20,230,20)
    elif fps>20: myColor = (230,20,20)
    else: myColor = (20,20,230)
    cv2.putText(frame,str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2);
    #
    cv2.imshow("Tracking", frame)
    sucess, frame = cap.read()
    if not success:
        break
    (success, boxes) = trackers.update(frame)
    for box in boxes:
        (x,y,w,h) = [int(a) for a in box]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('Frame',frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
        #import object_tracking

cap.release()
