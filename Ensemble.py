import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import load_model
import os


MODEL_PTH = os.getcwd()
model = load_model(MODEL_PTH+"/weights/dense_NET.h5")
model_2 = load_model(MODEL_PTH+"/weights/inception_v3.h5")

class Ensemble:

    #Image Path - absolute path of the Input Image
    
    def Result(self, img_array):
        #plt.imshow(img_array)
        #plt.show()
        
        #128 DenseNet
        new_img_array = cv2.resize(img_array, (128, 128))
        #new_img_array = img_array.resize((128,128))
        dt = []
        dt.append(new_img_array)
        X = np.array(dt)
        X = X/255
        val = model.predict(X)

        #256 Inception V3
        new_img_array_2 = cv2.resize(img_array, (224, 224))
        #new_img_array_2 = img_array.resize((224, 224))
        dt_2 = []
        dt_2.append(new_img_array_2)
        X_2 = np.array(dt_2)
        X_2 = X_2/255
        val_2 = model_2.predict(X_2)

        preds = [val, val_2]
        weights = [0.5,0.5]
        weighted_preds = np.tensordot(preds, weights, axes=((0),(0)))


        if weighted_preds > 0.5:
            print("COVID")
            return "1"
        else:
            print("NORMAL")
            return "0"

