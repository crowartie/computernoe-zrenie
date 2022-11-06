import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

countA, countB, count8, count0, count1, countW, \
countX, countStar, countTire, countSlash, \
countP, countD = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0


def lakes(imageSym):
    reverseImage = ~imageSym
    intArrayImage = np.array(reverseImage, dtype=object)
    for i in range(intArrayImage.shape[0]):
        for j in range(intArrayImage.shape[1]):
            if intArrayImage[i][j]:
                intArrayImage[i][j] = 1
            else:
                intArrayImage[i][j] = 0
    l = label(intArrayImage)
    regions = regionprops(l)
    countLakes = 0
    borderImage = 0
    for region in regions:
        for i in region.coords:
            if i[0] == 0 or i[1] == 0 or i[0] == reverseImage.shape[0] - 1 or i[1] == reverseImage.shape[1] - 1:
                borderImage = 1
                break
        if borderImage == 0:
            countLakes += 1
        else:
            borderImage = 0
    return countLakes, np.max(l) - countLakes


def recognize(img):
    countLakes, countBays = lakes(img.image)
    if countLakes == 0:
        # X or / or * or 1 or - or W
        if np.all(img.image):
            return '-'
        elif countBays == 2:
            return "/"
        elif countBays == 3:
            return "1"
        elif countBays == 4:
            return "X"
        elif countBays == 5:

            if img.image.shape[1] > 20:
                return "W"
            else:
                return "*"
    elif countLakes == 1:
        # D or P or A or 0
        if countBays == 2:
            if img.image[img.image.shape[0] // 2, img.image.shape[1] // 2] == 1:
                return "P"
            else:
                return "D"
        elif countBays == 3:
            return "A"
        elif countBays == 4:
            return "0"

    elif countLakes == 2:
        # 8 or B
        if countBays == 2:
            return "B"
        else:
            return "8"


symbols = plt.imread("symbols.png")
binary = np.sum(symbols, 2)
binary[binary > 0] = 1
labeled = label(binary)

regions = regionprops(labeled)

for region in regions:
    symbol = recognize(region)
    if symbol == "A":
        countA += 1
    elif symbol == "B":
        countB += 1
    elif symbol == "8":
        count8 += 1
    elif symbol == "0":
        count0 += 1
    elif symbol == "1":
        count1 += 1
    elif symbol == "W":
        countW += 1
    elif symbol == "X":
        countX += 1
    elif symbol == "*":
        countStar += 1
    elif symbol == "-":
        countTire += 1
    elif symbol == "/":
        countSlash += 1
    elif symbol == "P":
        countP += 1
    elif symbol == "D":
        countD += 1

arrSymbols = [countA, countB, count8, count0, count1, countW, countX, countStar, countTire, countSlash, countP, countD]
print("A:", countA, "частота равна", countA / (np.sum(arrSymbols) / 100), "%\nB:", countB, "частота равна",
      countB / (np.sum(arrSymbols) / 100), "% \n8:", count8, "частота равна", count8 / (np.sum(arrSymbols) / 100),
      "%\n0:", count0, "частота равна", count0 / (np.sum(arrSymbols) / 100), "%\n1:", count1, "частота равна",
      count1 / (np.sum(arrSymbols) / 100), "% \nW:", countW, "частота равна", countW / (np.sum(arrSymbols) / 100),
      "%\nX:", countX, "частота равна", countX / (np.sum(arrSymbols) / 100), "%\n*:", countStar, "частота равна",
      countStar / (np.sum(arrSymbols) / 100), "%\n-:", countTire, "частота равна",
      countTire / (np.sum(arrSymbols) / 100), "%\n/:", countSlash, "частота равна",
      countSlash / (np.sum(arrSymbols) / 100),
      "%\nP:", countP, "частота равна", countP / (np.sum(arrSymbols) / 100), "% \nD:", countD, "частота равна",
      countD / (np.sum(arrSymbols) / 100), "%")

print("Суммарное кол-во символов: ", np.sum(arrSymbols))
