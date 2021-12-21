from tensorflow.keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
from tensorflow import keras

"""create datasets of pictures from the directory"""
train = ImageDataGenerator(rescale=1/255)
trainDataset = train.flow_from_directory('C:/Users/Frank/Desktop/Lego',
                                         target_size=(400, 400), batch_size=64, class_mode='categorical')
validation = ImageDataGenerator(rescale=1/255)
validationDataset = validation.flow_from_directory('C:/Users/Frank/Desktop/LegoVal',
                                                   target_size=(400, 400), batch_size=64, class_mode='categorical')

"""create a neronal network"""
model = keras.models.Sequential([
    keras.layers.Conv2D(16,(3,3), activation='relu',input_shape=(400,400,3)), # 16 filter with each size 3*3
    keras.layers.MaxPool2D(2,2),
    keras.layers.Conv2D(32,(3,3), activation='relu',input_shape=(400,400,3)), # 32 filter
    keras.layers.MaxPool2D(2,2),
    keras.layers.Conv2D(64,(3,3), activation='relu',input_shape=(400,400,3)), # 64 filter
    keras.layers.MaxPool2D(2,2),
    keras.layers.Flatten(),
    keras.layers.Dense(units=512, activation="relu"),
    keras.layers.Dense(5, activation="softmax")
])

"""compile model"""
model.compile(loss="categorical_crossentropy", optimizer=keras.optimizers.SGD() , metrics=["accuracy"])

"""train model"""
history = model.fit(trainDataset, batch_size=64, epochs=5, validation_data=validationDataset)

"""save model"""
model.save('C:/Users/Frank/Desktop/MyModel/firstModel.h5')

"""Create diagramms of loss-function and correct-classification-rate"""
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, 'bo', label='Training')
plt.plot(epochs, val_acc, 'b', label='Validierung')
plt.plot('Korrektklassifizierungsrate Training/Validierung')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Verlust Training')
plt.plot(epochs, val_loss, 'b', label='Verlust Validierung')
plt.title('Wert der Verlustfunktion Training/Validierung')
plt.legend()
plt.show()