import matplotlib.pyplot as plt
import pyautogui as pg
from mss import mss
import time
from skimage import color
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
import numpy as np
from skimage import morphology


def getCoords(region):
    X = []
    Y = []
    for x, y in region.coords:
        X.append(x)
        Y.append(y)
    return np.min(X), np.max(X), np.min(Y), np.max(Y)


def distantion(l, countObj):
    position = []
    regions = regionprops(l)
    if countObj == 1:
        x_min, x_max, y_min, y_max = getCoords(regions[0])
        return y_min, x_min, y_max
    else:
        minObj = regions[0]
        for region in regions:
            if minObj.coords[0][0] > region.coords[0][0]:
                minObj = region
        x_min, x_max, y_min, y_max = getCoords(minObj)
        return y_min, x_min, y_max

    # print(np.min(position))


def scrWindow():
    im1 = pg.screenshot(region=(470, 288, 280, 56))
    grayImg = color.rgb2gray(im1)
    thresholdImg = threshold_otsu(grayImg)
    trialImg = grayImg < thresholdImg
    trialImg = morphology.binary_erosion(trialImg)
    trialImg = morphology.binary_dilation(trialImg)
    trialImg = morphology.binary_dilation(trialImg)
    return trialImg


def scrInnerCircle(widthObj, heightObj):
    im1 = pg.screenshot(region=(470 + widthObj + 25, 288 + (56 - heightObj) - 2, widthObj, heightObj))
    grayImg = color.rgb2gray(im1)
    thresholdImg = threshold_otsu(grayImg)
    trialImg = grayImg < thresholdImg
    trialImg = morphology.binary_erosion(trialImg)
    trialImg = morphology.binary_dilation(trialImg)
    trialImg = morphology.binary_dilation(trialImg)
    return trialImg


def getPixel(mss, monitor):
    # print(monitor['left'],monitor['top'])
    RGBA = np.array(mss.grab(monitor))

    return RGBA[0][0][0], RGBA[0][0][1], RGBA[0][0][2], RGBA[0][0][3]


def scannObj(firstMove):
    if firstMove == 0:
        time.sleep(1)
        firstMove = 1
    distanceToTheObject, theHighestPoint, rightmostPoint = distantion(label(scr), np.max(label(scr)))
    heightObj = 63 - theHighestPoint
    widthObj = rightmostPoint - distanceToTheObject
    print(widthObj, heightObj)
    # print(width, height)
    # plt.imshow(scr)
    # plt.show()
    return widthObj, heightObj, firstMove


def scannInnerCircle(widthObj, heightObj):
    monitor = {'left': int(470 + (pow(widthObj, 1.3))),
               'top': 288 + 56 - int(heightObj / 2) + 1,
               'width': 1,
               'height': 1
               }
    while True:
        scr = scrInnerCircle(widthObj, heightObj)
        r, g, b, a = getPixel(mss(), monitor)
        if r == 83 and g == 83 and b == 83 and a == 255 or np.max(label(scr)) != 0:
            action()
            # plt.imshow(scr)
            # plt.show()
            # print(r, g, b, a)


def action():
    pg.press('space')


firstMove = 0
numAction = 0
width, height = 0, 0
widthObj, heightObj = 0, 0
while True:
    scr = scrWindow()

    if numAction == 0:
        if np.max(label(scr)) != 0:
            widthObj, heightObj, firstMove = scannObj(firstMove)
            numAction = 1
            print(f"расположение координаты{750, 337 - int(heightObj / 2)}")

    elif numAction == 1:
        scannInnerCircle(widthObj, heightObj)
        numAction = 0
