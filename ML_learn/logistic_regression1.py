#!/usr/bin/python 
# -*- coding:utf-8 -*-
# 2019年5月3日14:16:31
# 对学生 成绩和读书时间 的分类问题

from sklearn.linear_model import LogisticRegression
import pandas as pd

# 载入数据
data = pd.read_csv('quiz.csv')
used_features = ["Last Score", "Hours Spent"]
X = data[used_features].values
scores = data["Score"].values

X_train = X[:11]
X_test = X[11:]

# 二项分类
passed = []
for i in range(len(scores)):
    if scores[i] >= 85:
        passed.append(2)
    elif scores[i] >= 60:
        passed.append(1)
    else:
        passed.append(0)
y_train = passed[:11]
y_test = passed[11:]

classifier = LogisticRegression(C=1e5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(y_pred)