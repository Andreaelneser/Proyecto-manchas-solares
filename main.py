import cv2
import matplotlib.pyplot as plt
import glob
import os

def plotImg(img):
    if len(img.shape) == 2:
        plt.imshow(img, cmap='gray')
        plt.show()
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()

path = 'D:/Documents/Universidad/Lala/Hola/PROYECTO/Sol'
path_file = os.path.join(path, 'Sol*.jpg')
images = glob.glob(path_file)

for img_name in images:
    img = cv2.imread(img_name)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binary_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 131, 15)
    plotImg(binary_img) #imagen en threshold
    _, _, boxes, _ = cv2.connectedComponentsWithStats(binary_img)

    boxes = boxes[1:]
    filtered_boxes = []
    for x, y, w, h, pixels in boxes:
        if pixels > 3 and h < 200 and w < 200 and h > 0 and w > 0: #tamaño de manchas
            filtered_boxes.append((x, y, w, h))

    for x, y, w, h in filtered_boxes:
        rectangulo = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2) #dibujo de las cajas sobre las manchas

    plotImg(img)

cv2.destroyAllWindows()
