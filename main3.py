import cv2
image = cv2.imread("pikachu.png", 1)
B,G,R = cv2.split(image)

cv2.imshow("BlueSaturation", B)
cv2.imshow("RedSaturation", R)
cv2.imshow("GreenSaturation", G)

cv2.waitKey(5000)
cv2.destroyAllWindows