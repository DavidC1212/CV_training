import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

data = []


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        # print(img.shape)
        # print(type(img))
        if img is not None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # np.array(images.append(np.array(img)))
            images.append(img)

    if np.array(images).shape[0] != 20:
        print(folder)
    return np.array(images)


for folder in os.listdir(
        r'C:\Users\sus85\OneDrive\Desktop\CV\cv_David\CV_training\data_science\4_dimentionality_reduction\data\faces94\female'):
    path = os.path.join(
        r'C:\Users\sus85\OneDrive\Desktop\CV\cv_David\CV_training\data_science\4_dimentionality_reduction\data\faces94\female',
        folder)
    data.append(load_images_from_folder(path))

for folder in os.listdir(
        r'C:\Users\sus85\OneDrive\Desktop\CV\cv_David\CV_training\data_science\4_dimentionality_reduction\data\faces94\male'):
    path = os.path.join(
        r'C:\Users\sus85\OneDrive\Desktop\CV\cv_David\CV_training\data_science\4_dimentionality_reduction\data\faces94\male',
        folder)
    data.append(load_images_from_folder(path))

for folder in os.listdir(
        r'C:\Users\sus85\OneDrive\Desktop\CV\cv_David\CV_training\data_science\4_dimentionality_reduction\data\faces94\malestaff'):
    path = os.path.join(
        r'C:\Users\sus85\OneDrive\Desktop\CV\cv_David\CV_training\data_science\4_dimentionality_reduction\data\faces94\malestaff',
        folder)
    data.append(load_images_from_folder(path))


data = np.array(data)
data = np.array(data)
N, B, H, W = data.shape
data = data.reshape(-1, H, W)
mean_face = np.mean(data, axis=0)
var_face = np.std(data, axis=0)

data_normalized = (data - mean_face) / var_face

data_normalized = data_normalized.reshape(-1, N*B)

data_cov = np.cov(data_normalized)

w, v = np.linalg.eig(data_cov)

idx = w.argsort()[::-1]
idx = idx[:100]#Sort eigenvectors
eigvalues = w.real[idx]       #Take only real vectors
eigvectors = v.real[:,idx]

fig, ax = plt.subplots(1, 5, figsize=(15, 5))
for i in range(5):
    ax[i].imshow(eigvectors[:, i].reshape(200,180).astype('float64'), cmap='gray')

plt.show()