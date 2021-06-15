import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

# Range of blue color in HSV
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# Range of red color in HSV
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])

# Range of yellow color in HSV
lower_yellow = np.array([22, 93, 0])
upper_yellow = np.array([45, 255, 255])

# Range of green color in HSV
lower_green = np.array([25, 52, 72])
higher_green = np.array([102, 255, 255])


while True:
    # Take each frame
    _, frame = capture.read()

    # # Displaying the current frame
    # cv.imshow('frame', frame)
    # if cv.waitKey(10) == ord('q'):
    #     break
    #
    # # Setting values for base colors
    # b = frame[:, :, :1]
    # g = frame[:, :, 1:2]
    # r = frame[:, :, 2:]
    #
    # # Computing the mean
    # b_mean = np.mean(b)
    # g_mean = np.mean(g)
    # r_mean = np.mean(r)
    #
    # # Displaying the prominent color
    # if b_mean > g_mean and b_mean > r_mean:
    #     print("Blue")
    #
    # if g_mean > r_mean and g_mean > b_mean:
    #     print("Green")
    #
    # else:
    #     print("Red")

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Threshold the HSV to a certain color range
    mask = cv.inRange(hsv, lower_yellow, upper_yellow)

    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 1000:
            # Drawing a rectangle around contour
            # cv.drawContours(frame, contour, -1, (0, 255, 0), 2)
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print(area)

    cv.imshow('frame', frame)
    if cv.waitKey(10) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
