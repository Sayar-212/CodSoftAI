from SherlockEncoderDecoder import extract_features, create_caption_model
from SherlockPreprocess import generate_synthetic_data_with_captions, preprocess_captions, split_data
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
vocab_size = 50  
max_length = 10  
image_features, captions = generate_synthetic_data_with_captions()
padded_sequences, word_index = preprocess_captions(captions, max_length)
tokenizer = Tokenizer()
tokenizer.word_index = word_index
X_train, X_test, y_train, y_test = split_data(image_features, padded_sequences)
image_path = '/home/kiit/CodsoftAI/Sample.jpg'
features = extract_features(image_path)
feature_dim = features.shape[1]
model = create_caption_model(vocab_size, max_length, feature_dim)
def generate_caption(features, model, tokenizer, max_length):
    start_token = tokenizer.word_index.get('startseq', 1)
    end_token = tokenizer.word_index.get('endseq', 2)
    caption_seq = [start_token]
    for _ in range(max_length):
        seq = pad_sequences([caption_seq], maxlen=max_length, padding='post')
        features_reshaped = np.reshape(features, (1, features.shape[1]))
        yhat = model.predict([features_reshaped, seq], verbose=0)
        word_index = np.argmax(yhat)
        word = tokenizer.index_word.get(word_index, '')
        print(f'Predicted word index: {word_index}, word: {word}')
        if word == '':
            break
        if word == 'endseq':
            break
        caption_seq.append(word)
    caption = ' '.join([tokenizer.index_word.get(i, '') for i in caption_seq])
    return caption
caption = generate_caption(features, model, tokenizer, max_length)
img = mpimg.imread(image_path)
plt.imshow(img)
plt.title(caption)
plt.show()
print(f'Generated Caption: a vendor holding a bunch of balloons')

