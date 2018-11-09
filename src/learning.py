import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.model_selection import train_test_split


class Leraning:
    def __init__(self):
        pass

    def predictcurryday(self, currydatas):
        x_train = np.array(currydatas[0])  # カレーの日に1が立っている(ex: [0,0,1,0,0], [1,0,0,0,0],...)
        y_train = np_utils.to_categorical(currydatas[1])  # DBのweekの情報(ex: [2, 0, ...])
        x_train, test_xdata, y_train, test_ydata = train_test_split(x_train, y_train, test_size=0.1)  # テスト用データ分割

        # ニューラルネットワーク作成
        model = Sequential()
        # 隠れ層
        model.add(Dense(200, input_dim=5, activation='relu'))
        model.add(Dense(200, activation='relu'))
        model.add(Dense(200, activation='relu'))
        # 出力層
        model.add(Dense(5, activation='softmax'))

        model.compile('rmsprop', 'categorical_crossentropy', metrics=['accuracy'])
        model.fit(x_train, y_train, nb_epoch=20)  # 学習

        predict = model.predict(test_xdata)
        res = []
        for var in range(0, len(predict)):
            # 予測した中で最大値のものをカレーの日の予想とする
            pos = predict[var].argmax()
            week = [0, 0, 0, 0, 0]
            week[pos] = 1
            res.append(week)

        return res


