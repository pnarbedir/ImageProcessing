import cv2 as cv


image = cv.imread("tumor.jpg")
cv.imshow("Orijinal",image)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
edged = cv.Canny(gray, 30, 50)
cv.imshow("Canny Edge Detection",edged)
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.imshow("Contoured Image",edged)


cv.drawContours(image, contours, -1, (255,255,255),3)
cv.imshow("Contours",image)
cv.waitKey(0)
cv.destroyAllWindows()