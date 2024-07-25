import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import VGG16, ResNet50
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.layers import Embedding, LSTM, Dense, Input
from tensorflow.keras.models import Model
def extract_features(image_path, model_name='VGG16'):
    if model_name == 'VGG16':
        model = VGG16(include_top=False, weights='imagenet', pooling='avg')
    elif model_name == 'ResNet50':
        model = ResNet50(include_top=False, weights='imagenet', pooling='avg')
    else:
        raise ValueError("Unsupported model name")
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    features = model.predict(image)
    return features
def create_caption_model(vocab_size, max_length, feature_dim):
    inputs1 = Input(shape=(feature_dim,))
    fe1 = Dense(256, activation='relu')(inputs1)
    inputs2 = Input(shape=(max_length,))
    se1 = Embedding(vocab_size, 256, mask_zero=True)(inputs2)
    se2 = LSTM(256)(se1)
    decoder1 = Dense(256, activation='relu')(se2)
    outputs = Dense(vocab_size, activation='softmax')(decoder1)
    model = Model(inputs=[inputs1, inputs2], outputs=outputs)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

