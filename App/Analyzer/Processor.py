import numpy
import tensorflow
import cv2
from .Variables import *

class InputPropcessor:
    def __init__(self):
        print("Image Processor is connected🚀🚀")
    def preprocessInput(self,image_path):
        image_array=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
        image_array=cv2.resize(image_array,resize_dimension)
        image_array=numpy.expand_dims([image_array],axis=-1)
        return image_array

class ModelProcessor:
    def __init__(self):
        print("🚀Model Processor is Initialized🚀🚀")
    def setModel(self,ModelPath):
        self.model=tensorflow.keras.models.load_model(ModelPath)
        print("Model is Connected")
    def predictClass(self,image_array):
        print(image_array.shape)
        prediction=self.model.predict(image_array)
        return class_list[numpy.argmax(prediction[0])]
    def predictFacturePossibility(self,image_array,class_name):
        model=tensorflow.keras.models.load_model(mapping[class_name])
        print("Bone Facture Predictor is connected")
        print(image_array.shape)
        prediction=model.predict(image_array)
        return facture_possibilities[numpy.argmax(prediction[0])],prediction[0][numpy.argmax(prediction[0])]

