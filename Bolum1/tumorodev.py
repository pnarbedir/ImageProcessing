import cv2
#Goruntuyu ac
image = cv2.imread("tumor.jpg")
cv2.imshow("Orijinal",image)

#Grayscale'e cevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Canny kenar tespiti
edged = cv2.Canny(gray, 30, 40)
cv2.imshow("Canny Kenar Tespiti",edged)

#Kontur bulma
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow("Kontur Sonrasi Kenarlar",edged)
print("Bulunan kontur sayisi: " + str(len(contours)))

#Konturlarin cizimi

cv2.drawContours(image, contours, -1, (0,0,255),3)
cv2.imshow("Konturlar",image)
cv2.waitKey(0)
cv2.destroyAllWindows()