# -*- coding: utf-8 -*-
"""Linear Regression Health Costs Calculator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ar6Mlhr9Dkk9SB8dvdw7xSDIXijWoVCP
"""

# Commented out IPython magic to ensure Python compatibility.
# Import libraries. You may or may not use all of these.
!pip install -q git+https://github.com/tensorflow/docs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

try:
  # %tensorflow_version only exists in Colab.
#   %tensorflow_version 2.x
except Exception:
  pass
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling

# Import data
!wget https://cdn.freecodecamp.org/project-data/health-costs/insurance.csv
raw_dataset = pd.read_csv('insurance.csv')
raw_dataset.tail()

dataset = raw_dataset.copy()

dataset = pd.get_dummies(dataset, columns=['sex', 'smoker', 'region'], prefix='', prefix_sep='')

train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop('expenses')
test_labels = test_features.pop('expenses')

normalizer = tf.keras.layers.Normalization(axis=-1)
normalizer.adapt(np.array(train_features))

linear_model = tf.keras.Sequential([
    normalizer,
    layers.Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.L2(0.01)),  # Adding regularization
    layers.Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.L2(0.01)),   # More neurons
    layers.Dense(units=1)
])


linear_model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='mse',
    metrics=[keras.metrics.MeanAbsoluteError()]
    )

# Early stopping to prevent overfitting
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss', patience=20, restore_best_weights=True
)

history = linear_model.fit(
    train_features,
    train_labels,
    batch_size=128,
    epochs=1000,
    verbose=0,
    validation_data=(test_features, test_labels),
    callbacks=[early_stopping]

)

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch

def plot_loss(history):
  plt.plot(history.history['loss'], label='loss')
  plt.plot(history.history['val_loss'], label='val_loss')
  #plt.ylim([0, 10])
  plt.xlabel('Epoch')
  plt.ylabel('Error [XP]')
  plt.legend()
  plt.grid(True)

plot_loss(history)

# Generate generalization metrics
score = linear_model.evaluate(test_features, test_labels, verbose=0)
print(f'Test loss: {score[0]} / Test mae: {score[1]}')

# Test loss: 356347232.0 / Test mae: 14124.3623046875

# RUN THIS CELL TO TEST YOUR MODEL. DO NOT MODIFY CONTENTS.
# Test model by checking how well the model generalizes using the test set.
mae = linear_model.evaluate(test_features, test_labels, verbose=0)

print("Testing set Mean Abs Error: {:5.2f} expenses".format(mae[1]))

if mae[1] < 3500:
  print("You passed the challenge. Great job!")
else:
  print("The Mean Abs Error must be less than 3500. Keep trying.")

# Plot predictions.
test_predictions = linear_model.predict(test_features).flatten()

a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True values (expenses)')
plt.ylabel('Predictions (expenses)')
lims = [0, 50000]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims,lims)