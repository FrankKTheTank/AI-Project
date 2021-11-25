from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os

#print(cv2.imread("C:/Users/Frank/Desktop/Pics/yellowBrick.PNG").shape)
train = ImageDataGenerator(rescale=1/255)
validation = ImageDataGenerator(rescale=1/255)

trainDataset = train.flow_from_directory('C:/Users/Frank/Desktop/Pics/3003 Brick 2x2',
                                         target_size=(200, 200), batch_size=3, class_mode='binary')

validationDataset = validation.flow_from_directory('C:/Users/Frank/Desktop/Pics/3003 Brick 2x2',
                                         target_size=(200, 200), batch_size=3, class_mode='binary')

#print(trainDataset.class_indices)
#print(trainDataset.classes)

"""create a neronal network"""
model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(16,(3,3), activation='relu',input_shape=(200,200,3)), # 16 filter with each size 3*3
  tf.keras.layers.MaxPool2D(2,2),
  tf.keras.layers.Conv2D(32,(3,3), activation='relu',input_shape=(200,200,3)), # 32 filter
  tf.keras.layers.MaxPool2D(2,2),
  tf.keras.layers.Conv2D(64,(3,3), activation='relu',input_shape=(200,200,3)), # 64 filter
  tf.keras.layers.MaxPool2D(2,2),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(units=512, activation="relu"),
  tf.keras.layers.Dense(units=1, activation="sigmoid")
])

"""compile model"""
model.compile(loss="binary_crossentropy", optimizer= tf.keras.optimizers.SGD() , metrics=["accuracy"])

"""train model"""
model.fit(trainDataset, batch_size=128, epochs=10, validation_data=validationDataset)

model.save('C:/Users/Frank/Desktop/MyModel/testModel')

dir_path= 'C:/Users/Frank/Desktop/Pics/Test'

for i in os.listdir(dir_path):
    img = image.load_img(dir_path + '//' + i, target_size=(200,200,3))
    plt.imshow(img)
    plt.show()

    X = image.img_to_array(img)
    X = np.expand_dims(X,axis=0)
    images = np.vstack([X])
    val = model.predict(images)
    if val == 0:
        print('Oben')
    else:
        print('Unten')










# Create a dataset.
#dataset = keras.preprocessing.image_dataset_from_directory('C:/Users/Frank/Desktop/Pics', batch_size=1, image_size=(479, 329))

# For demonstration, iterate over the batches yielded by the dataset.
#for data, labels in dataset:
#    print(data.shape)  # (64, 200, 200, 3)
#    print(data.dtype)  # float32
#    print(labels.shape)  # (64,)
#    print(labels.dtype)  # int32