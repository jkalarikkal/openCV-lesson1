import cv2

image = cv2.imread("pikachu.png", -1)

cv2.imwrite("Pika.png", image)
print("Successfully saved")