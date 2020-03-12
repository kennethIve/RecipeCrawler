
from keras.models import Model
import tensorflow as tf
import numpy as np

modelPath = "C:\\Users\\jpkhuang\\Desktop\\Crawler\\RecipeScrapy\\tensorflow\\detect.tflite"
print("loading tflite model")
#interpreter = tf.lite.Interpreter(model_path="model\detect.tflite")
interpreter = tf.lite.Interpreter(model_path=modelPath)
interpreter.allocate_tensors()

print("testing model")
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
