import os
import pickle
import re
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from tensorflow.keras import utils
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization, SpatialDropout1D, Embedding, Flatten, Activation
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer

a = os.listdir('writers')
print(a)

FILE_DIR = 'writers'                     # Папка с текстовыми файлами
SIG_TRAIN = 'обучающая'                   # Признак обучающей выборки в имени файла
SIG_TEST = 'тестовая'                    # Признак тестовой выборки в имени файла
CLASS_LIST = []
text_train = []
text_test = []

for file_name in os.listdir(FILE_DIR):
    # print(file_name)
    m = re.match('\((.+)\) (\S+)_', file_name)
    if m:
        # print(m[1], m[2])
        class_name = m[1]
        subset_name = m[2].lower()
        is_train = SIG_TRAIN in subset_name
        is_test = SIG_TEST in subset_name

        if is_train or is_test:
            if class_name not in CLASS_LIST:
                #print(f'Adding a class "{class_name}"')
                CLASS_LIST.append(class_name)
                text_train.append('')
                text_test.append('')

            cls = CLASS_LIST.index(class_name)  # searching for index of added class name
            # print(f'Adding file "{file_name}" in the class "{CLASS_LIST[cls]}", {subset_name} selection.')
            print(FILE_DIR, file_name, cls)


            with open(f'{FILE_DIR}/{file_name}', 'r', encoding="utf8") as f:
                text = f.read()
                
            subset = text_train if is_train else text_test
            subset[cls] += ' ' + text.replace('\n', ' ')

CLASS_COUNT = len(CLASS_LIST)





