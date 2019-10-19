import cv2


def main():
    img = cv2.imread("task.png")


    im = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow("tested image", im)
    cv2.waitKey()
    cv2.destroyAllWindows()
    pass


if __name__ == '__main__':
    main()
