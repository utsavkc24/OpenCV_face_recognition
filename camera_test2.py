import cv2, time

#1Create an object, Zero for external camera
video = cv2.VideoCapture(0);

#3. Create a frame object
check, frame = video.read();

print(check)
print(frame) #Representing image


#2 Shutdown the camera
video.release()
