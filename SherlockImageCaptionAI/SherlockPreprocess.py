import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
def generate_synthetic_data_with_captions():
    captions = [
        "a man riding a horse",
        "a group of people standing in front of a building",
        "a dog playing with a ball",
        "a cat sitting on a sofa",
        "a vendor holding a bunch of balloons" 
    ]
    features = np.random.rand(len(captions), 4096) 
    return features, captions
def preprocess_captions(captions, max_length):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(captions)
    sequences = tokenizer.texts_to_sequences(captions)
    padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')
    return padded_sequences, tokenizer.word_index
def split_data(image_features, padded_sequences):
    X_train, X_test, y_train, y_test = train_test_split(image_features, padded_sequences, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

