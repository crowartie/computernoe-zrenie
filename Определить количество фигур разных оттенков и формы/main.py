import matplotlib.pyplot as plt
import numpy as np
from skimage import color
from skimage.measure import label, regionprops

image = plt.imread("balls_and_rects.png")
grayImage = color.rgb2gray(image)
grayImage[grayImage > 0] = 1
labeled = label(grayImage)
image_hsv = color.rgb2hsv(image)
regions = regionprops(labeled)
figures = {"rectangle": {}, "circle": {}}
for region in regions:

    c = image_hsv[round((region.coords[0][0] + region.image.shape[0] / 2))][
        round((region.coords[0][1] + region.image.shape[1] / 2))][0]
    if region.area / (region.image.shape[0] * region.image.shape[1]) == 1:
        if c in figures["rectangle"]:
            figures["rectangle"][c] += 1
        else:
            figures["rectangle"][c] = 1
    else:
        if c in figures["circle"]:
            figures["circle"][c] += 1
        else:
            figures["circle"][c] = 1
for i in figures:
    if i == "rectangle":
        nameFigure = "Прямоугольников"
    else:
        nameFigure = "Кругов"
    for key, value in figures[i].items():
        print(f"{nameFigure} с оттенком {key} найдено {value} шт.")
print(f"Кол-во прямоугольников равно:{np.sum(list(figures['rectangle'].values()))}")
print(f"Кол-во кругов равно:{np.sum(list(figures['circle'].values()))}")
print(f"Кол-во фигур равно:{np.sum(list(figures['rectangle'].values())) + np.sum(list(figures['circle'].values()))}")
