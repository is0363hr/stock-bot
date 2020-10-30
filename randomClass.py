# ---------------------------------------------------------
# import
# ---------------------------------------------------------

# import vital tools
import pandas as pd
import numpy as np
# from matplotlib import pyplot as plt
# import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics, linear_model
# from selenium import webdriver
# import requests
# import json
import pickle
import time


# ---------------------------------------------------------
# method
# ---------------------------------------------------------


def randomForest(data, target):

    model = RandomForestRegressor(n_estimators=1000)

    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.27)

    # model making and prediction
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    # make result score and get accuracy score
    testUpDown = []
    for test in y_test:
        if test > 0:
            testUpDown.append(1)
        else:
            testUpDown.append(-1)
    predUpDown = []
    for pred in y_pred:
        if pred > 0:
            predUpDown.append(1)
        else:
            predUpDown.append(-1)
    # print("確率："+str(metrics.accuracy_score(testUpDown, predUpDown)))

    result_test = metrics.accuracy_score(testUpDown, predUpDown)

    return result_test


def randomForestPredict(data, target, predict):
    # model = RandomForestRegressor(n_estimators=1000)

    # model making and prediction
    # model.fit(data, target)

    # filename = 'stock_nomura_model.sav'
    # pickle.dump(model, open(filename, 'wb'))

    model = pickle.load(open('stock_nomura_model.sav', 'rb'))
    result_pred = model.predict(predict)

    for pred in result_pred:
        if pred > 0:
            result = 1
        else:
            result = -1

    return result


def sgd(data, target):
    model = linear_model.SGDRegressor(max_iter=1000)

    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.27)

    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    # make result score and get accuracy score
    testUpDown = []
    for test in y_test:
        if test > 0:
            testUpDown.append(1)
        else:
            testUpDown.append(-1)
    predUpDown = []
    for pred in y_pred:
        if pred > 0:
            predUpDown.append(1)
        else:
            predUpDown.append(-1)
    # print("確率："+str(metrics.accuracy_score(testUpDown, predUpDown)))

    result_test = metrics.accuracy_score(testUpDown, predUpDown)

    return result_test


def csv_read():
    count = 0
    features = []
    # ETFfeatures = []
    train = pd.read_csv("stockPriceData.csv")
    train.head()

    columns_num = len(train.columns)

    for d1 in train.columns:
        if count > 3 and count < columns_num - 1:
            features.append(d1)
        count = count + 1
    data = train[features]
    target = train["(株)野村総合研究所：翌日比"]

    predict = train.iloc[1:2, 4:-1]

    return data, target, predict


class StockPridict():
    def processing_accuracy(self):
        dataset = csv_read()
        result = randomForest(dataset[0], dataset[1])
        print(result)
        return result

    def processing_predict(self):
        dataset = csv_read()
        result = randomForestPredict(dataset[0], dataset[1], dataset[2])
        print(result)
        return result
    # ---------------------------------------------------------
    # declaration
    # ---------------------------------------------------------


    # ---------------------------------------------------------
    # processing
    # ---------------------------------------------------------
    # result = randomForest(data, target)
    # result2 = sgd(data, target)


if __name__ == "__main__":
    test = StockPridict()
    # print(test.processing_accuracy)
    # print(test.processing_predict)
    start = time.time()
    test.processing_accuracy()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    start = time.time()
    test.processing_predict()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
