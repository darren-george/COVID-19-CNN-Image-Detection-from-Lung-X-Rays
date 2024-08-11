# -*- coding: utf-8 -*-
"""xray_check.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/rani700/xray/blob/master/test.ipynb

## Copying model.h5 file
"""

# model.h5 file is also uploaded to github repo so can be downloaded from there directly
!wget = https://raw.githubusercontent.com/rani700/xray/master/model.h5

import matplotlib.pyplot as plt
import numpy as np
import cv2

def dice_coef(y_true, y_pred):
    y_true_f = keras.flatten(y_true)
    y_pred_f = keras.flatten(y_pred)
    intersection = keras.sum(y_true_f * y_pred_f)
    return (2. * intersection + 1) / (keras.sum(y_true_f) + keras.sum(y_pred_f) + 1)

def dice_coef_loss(y_true, y_pred):
    return -dice_coef(y_true, y_pred)

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

from keras.models import load_model
from keras import backend as keras
model = load_model('model.h5', custom_objects={'dice_coef_loss':                   
dice_coef_loss, 'dice_coef': dice_coef})

img_path = list(uploaded.keys())[0]

X_shape = 512

x_im = cv2.resize(cv2.imread(img_path),(X_shape,X_shape))[:,:,0]

op = model.predict((x_im.reshape(1, 512, 512, 1)-127.0)/127.0)

plt.imshow(x_im, cmap="bone", label="Input Image")
plt.title("Input")
plt.show()

plt.imshow(x_im, cmap="bone", label="Output Image")
plt.imshow(op.reshape(512, 512), alpha=0.5, cmap="jet")
plt.title("Output")
plt.show()

