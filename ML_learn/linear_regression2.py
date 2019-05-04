#!/usr/bin/python 
# -*- coding:utf-8 -*-
# 与逻辑回归比较组
# 数据为分数和学习时间

from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

# 载入数据
data = pd.read_csv('quiz.csv')
used_features = ["Last Score", "Hours Spent"]
X = data[used_features].values
scores = data["Score"].values

X_train = X[:11]
X_test = X[11:]
print("Xtest:\n", X_test)
y_train = scores[:11]
y_test = scores[11:]

# 训练
regr = LinearRegression()
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)

# 这就很尴尬了，这么准的？训练矩阵给错了，也能训练~~
print("y_pred:", y_pred)

# 画点
plt.scatter(data["Hours Spent"], scores, color="blue")
# plt.scatter(data["Hours Spent"], data["Score"])
# 画线
plt.plot(data["Hours Spent"][11:], y_pred,  color="red", linewidth=2)

plt.xticks()
plt.yticks()
plt.show()