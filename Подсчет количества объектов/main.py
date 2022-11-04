import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

arrayImage = np.load("ps.npy.txt")
s = 0
obj=0
mask1 = np.array([[1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 0, 0],
                  [1, 1, 0, 0],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1]])

mask2 = np.array([[1, 1, 0, 0, 1, 1],
                  [1, 1, 0, 0, 1, 1],
                  [1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1]])

mask3 = np.array([[1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1],
                  [1, 1, 0, 0, 1, 1],
                  [1, 1, 0, 0, 1, 1]])

mask4 = np.array([[1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [0, 0, 1, 1],
                  [0, 0, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1]])

mask5 = np.array([[1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1]])
masks = np.array([mask1, mask2, mask3, mask4,mask5], dtype=object)
for mask in masks:
    r = ndimage.binary_hit_or_miss(arrayImage, mask)
    s += np.sum(r)
    obj+=1
    print("Количество фигур под номером ",obj," равно:",np.sum(r))
print("Общее количество фигур равно: ",s)
