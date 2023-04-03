# -*- coding: utf-8 -*-
"""epm-checkpoint.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TVliQD8YXRVEZh4carMi2mwWWpHtmKtq
"""

#!/usr/bin/env python
# coding: utf-8

"""# Convolutional Neural Network

### Importing the libraries

In[1]:
"""

import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator

"""In[2]:"""

tf.__version__

"""## Part 1 - Data Preprocessing"""





"""### Preprocessing the Training set

In[33]:
"""

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
training_set = train_datagen.flow_from_directory('/content/drive/MyDrive/train',
                                                 target_size = (64,64),
                                                 batch_size = 128,
                                                 class_mode = 'categorical',
                                                color_mode = 'grayscale')

from google.colab import drive
drive.mount('/content/drive')

"""### Preprocessing the Test set

In[34]:
"""

test_datagen = ImageDataGenerator(rescale = 1./255)
test_set = test_datagen.flow_from_directory('/content/drive/MyDrive/validation',
                                            target_size = (64,64),
                                            batch_size = 128,
                                            class_mode = 'categorical',
                                           color_mode = 'grayscale')

"""## Part 2 - Building the CNN

### Initialising the CNN

In[35]:
"""

cnn = tf.keras.models.Sequential()

"""### Step 1 - Convolution

In[36]:
"""

cnn.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', input_shape=[64,64, 1]))

"""### Step 2 - Pooling

In[37]:
"""

cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

"""### Adding a second convolutional layer

In[38]:
"""

cnn.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

"""### Step 3 - Flattening

In[39]:
"""

cnn.add(tf.keras.layers.Flatten())

"""### Step 4 - Full Connection

In[40]:
"""

cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))

"""### Step 5 - Output Layer

In[41]:
"""

cnn.add(tf.keras.layers.Dense(units=7, activation='softmax'))

"""## Part 3 - Training the CNN

### Compiling the CNN

In[42]:
"""

cnn.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

"""### Training the CNN on the Training set and evaluating it on the Test set

In[43]:
"""

cnn.fit(x=training_set, validation_data = test_set,verbose =1, epochs = 100)

"""## Part 4 - Making a single prediction on each emotion

In[80]:
"""

import numpy as np
from PIL import Image
test_image=image.load_img('/content/drive/MyDrive/1.jpg',
                          target_size=(128,128),color_mode='grayscale')
im=test_image
im

"""In[81]:"""

import numpy as np
from keras.preprocessing import image
test_image=image.load_img('C:/Users/Rachna.Goel/OneDrive - Unilever/Documents/Emotions predicting Model/prediction images/4.jpg',
                            target_size=(64,64),color_mode='grayscale')
test_image=image.img_to_array(test_image)
test_image=np.expand_dims(test_image,axis=0)
result=cnn.predict(test_image)

"""In[82]:"""

display(test_image)

"""In[83]:"""

if result[0][0]==1:
    print("Emotion predicted: Angry");
elif result[0][1]==1:
    print("Emotion predicted: Disgust");
elif result[0][2]==1:
    print("Emotion predicted: Fear");
elif result[0][3]==1:
    print("Emotion predicted: Happy");
elif result[0][4]==1:
    print("Emotion predicted: Neutral");
elif result[0][5]==1:
    print("Emotion predicted: Sad");
else:
    print("Emotion predicted: Surprised")
training_set.class_indices

"""In[84]:"""

result

"""In[ ]:"""