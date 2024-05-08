import cv2

img  = cv2.imread("pikachu.png", 0)
cv2.imshow("Pikachu image", img)
cv2.waitKey (5000)
cv2.destroyAllWindows()
