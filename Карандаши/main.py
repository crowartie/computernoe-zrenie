import os
import matplotlib.pyplot as plt
from skimage import color
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
import numpy as np
from skimage import morphology


def colorCorrectionImg(trialImg):
    grayImg = color.rgb2gray(trialImg)
    thresholdImg = threshold_otsu(grayImg)
    trialImg = grayImg < thresholdImg
    trialImg = morphology.binary_dilation(trialImg)
    return trialImg


def countingPencils(newImage):
    countPencils = 0
    l = label(newImage)
    regions = regionprops(l)
    for region in regions:
        if region.image.shape[0] > 1600 or region.image.shape[1] > 1600:
            if region.image.shape[0] > region.image.shape[1]:
                if np.sum(region.image[region.image.shape[0] // 2]) > 70:
                    countPencils += 1
            else:
                s = 0
                for w in range(region.image.shape[0]):
                    s += region.image[w][region.image.shape[1] // 2]
                if s > 70:
                    countPencils += 1

    return countPencils


directory = 'images'
files = os.listdir(directory)
photos = filter(lambda x: x.endswith('.jpg'), files)
allCountPencils = 0
for filePhoto in photos:
    img = plt.imread(directory + '/' + filePhoto)
    newImage: object = colorCorrectionImg(img)
    CountPencils = countingPencils(newImage)
    print(f"{filePhoto}: Кол-во карандашей на данном изображении равно {CountPencils}.")
    allCountPencils += CountPencils
print(f"Кол-во карандашей на всех фото равно {allCountPencils}")
