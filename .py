import cv2
cap = cv2.VideoCapture(0) #capture photo
while True:  #live video streaming
        status, photo = cap.read() 
        a = photo[100:300, 250:450] #crop the face from live video streaming
        photo[0:200, 0:200] = a  #put the crop photo on top corner
        cv2.imshow("My photo", photo)
        
        if cv2.waitKey(100)==13:  #to stop the live video streaming
            break

cv2.destroyAllWindows()
cap.release()
