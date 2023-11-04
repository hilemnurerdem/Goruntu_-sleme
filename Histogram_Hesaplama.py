#Hilem Nur Erdem 02215076005
# Gerekli kütüphaneler içe aktarılır.
import cv2
import numpy as np
from matplotlib import pyplot as plt

fotograf = cv2.imread('aslan.jpg', 0)

# Bir dizi olan 'hist' oluşturulur ve 256 elemanlı olarak başlatılır.
hist = np.zeros(256)
[w, h] = np.shape(fotograf)

for v in range(0, h):
    for u in range(0, w):
        i = fotograf[u, v]
        hist[i] = hist[i] + 1

for i in range(0, 256):
    print(i, "=", hist[i])

# Ekranda bir tuşa basılana kadar pencerenin açık kalmasını sağlar.
cv2.waitKey(0)

histHesapla = cv2.calcHist([fotograf], [0], None, [256], [0, 256])

plt.plot(hist, color='#000000')

# Grafiği ekranda gösterir.
plt.show()
