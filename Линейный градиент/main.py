import numpy as np
import matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

def move_array(size):
    trialImage = np.zeros((size*2, size*2, 3), dtype="uint8")
    trialImage = lineGradient(trialImage)
    image = np.zeros((size, size, 3), dtype="uint8")
    for i in range(len(trialImage)):
        for j in range(len(trialImage[i])):
            if(j+size<len(trialImage) and i+size<len(trialImage)):
                image[i][j]=trialImage[i][j+i]
    plt.imshow(image)
    plt.show()
def lineGradient(image):
    for i, v in enumerate(np.linspace(0, 1, image.shape[0])):
        r = lerp(color1[0], color2[0], v)
        g = lerp(color1[1], color2[1], v)
        b = lerp(color1[2], color2[2], v)
        image[:, i, :] = [r, g, b]
    return image
color1 = [227,113,0]
color2 = [0,113,227]
imageSize = 100
move_array(imageSize)

