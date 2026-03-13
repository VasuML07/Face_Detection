#a library used for computer vision taks
import cv2
#loads haar cascade model,cascade classifier is trained model to detect objects
face_cascade = cv2.CascadeClassifier(
    #this is a built in path inside opencv where pretrained haar models are there
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
#this one opens a vidoe source and 0 is default webcam
cap = cv2.VideoCapture(0)
#this is used to run a continous loop for eeading frames in real time
while True:
    #ret is a boolean value which us true when frame captured false when doesn't
    #frame is actual image captured form video
    ret, frame = cap.read()
    #if camera fails to capture a frame break and stop recording
    if not ret:
        break
    #convert frames to grayscale for simpler computation
    #cv2.cvtColor(image, conversion_type)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detectmultiscale scans searches for face at multiple scales
    faces = face_cascade.detectMultiScale(
        gray,
        #it tells how much the image size is reduced at each step
        #samller value better scanning
        scaleFactor=1.3,
        #it specifies how many times a region should be detected to accept it as face
        minNeighbors=5,
        #stes minimum size to detect a face
        minSize=(30,30)
    )
    #returns list of rectangles
    '''x → top-left x coordinate
       y → top-left y coordinate
       w → width
       h → height'''
    for (x, y, w, h) in faces:
        #open cv uses BGR so this means blue = 255 and green & red = 0
        #thickness is 2 pixels
        #draws bounding box image top-left corner bottom-right corner color_thickness
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    #if one face detected it tells face detected
    if len(faces) > 0:
        text = "Face Detected"
        color = (0,255,0)
    else:
        text = "Face Not Detected"
        color = (0,0,255)
    #this puts text on screen
    cv2.putText(
        frame,
        text,
        #co-ordinates
        (20,40),
        #open cb built in font
        cv2.FONT_HERSHEY_SIMPLEX,
        #font size
        1,
        color,
        #thickness
        2
    )
    #displays frame in window
    cv2.imshow("Face Detection", frame)
    #waits millisecond for keyboard input
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
#stops webcam acsess
cap.release()
cv2.destroyAllWindows()
