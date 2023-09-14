import cv2
image = cv2.imread('your image path')
image = cv2.resize(image, (800, 600))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), cv2.BORDER_DEFAULT)
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 10)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
compartment_count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 400 and area < 1200:
        compartment_count += 1
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
print(f"Number of compartments: {compartment_count}")
cv2.imshow('Image with Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
