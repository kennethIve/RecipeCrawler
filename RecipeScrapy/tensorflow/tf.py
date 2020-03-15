
from keras.models import Model
import tensorflow as tf
import numpy as np

#modelPath = "C:\\Users\\jpkhuang\\Desktop\\Crawler\\RecipeScrapy\\tensorflow\\detect.tflite"
modelPath = "C:\\FYP\\python_code\\RecipeCrawler\\RecipeScrapy\\tensorflow\\detect.tflite"
print("loading tflite model")
#interpreter = tf.lite.Interpreter(model_path="model\detect.tflite")
interpreter = tf.lite.Interpreter(model_path=modelPath)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

# 函数 `get_tensor()` 会返回一份张量的拷贝。
# 使用 `tensor()` 获取指向张量的指针。
tflite_results = interpreter.get_tensor(output_details[0]['index'])

print(input_data)
# 对比结果。
for  tflite_result in tflite_results:
  print(tflite_result) 