import cv2 as cv

name = 'movie.Mjpeg'

#video = cv.VideoCapture(0)  # Using camera 
video = cv.VideoCapture(name)  # Use video already available
subtractor = cv.createBackgroundSubtractorMOG2(40, 50)

while True:
    ret, frame = video.read()

    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)

        if cv.waitKey(5) == ord('x'):
            break
    else:                          
        video = cv.VideoCapture(name)

cv.destroyAllWindows()
video.release()