import cv2
import numpy as np


def main():
    # load the image
    image = cv2.imread("task.png")

    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define the lower and upper limit for pink color
    lower = np.array([160, 100, 100], dtype="uint8")
    upper = np.array([170, 255, 255], dtype="uint8")

    # find the colors within the specified boundaries
    mask = cv2.inRange(hsv_img, lower, upper)

    # getting the image having pink color with black background
    output = cv2.bitwise_and(image, image, mask=mask)

    # show the images
    cv2.imshow("images", output)
    cv2.waitKey(0)

    # pass


if __name__ == '__main__':
    main()
