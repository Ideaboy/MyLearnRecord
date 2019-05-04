#!/usr/bin/python 
# -*- coding:utf-8 -*-
# 2019-5-1 20:36:45
# 朴素贝叶斯分类器 - 极简（频率=概率）

import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# 载入数据
data = pd.read_csv("career_data.csv")

# 将分类变量转为数值变量
data["985_cleaned"] = np.where(data["985"] == "Yes", 1, 0)
data["education_cleaned"] = np.where(data["education"] == "bachlor", 1,
                                     np.where(data["education"] == "master", 2,
                                              np.where(data["education"] == "phd", 3, 4)
                                              )
                                     )
data["skill_cleaned"] = np.where(data["skill"] == "C++", 1,
                                 np.where(data["skill"] == "Java", 2, 3
                                          )
                                 )
data["enrolled_cleaned"] = np.where(data["enrolled"] == "Yes", 1, 0)
# 分割数据
X_train, X_test = train_test_split(data, test_size=0.1, random_state=int(time.time()))

# 初始化分类器
gnb = GaussianNB()
used_features = [
    "985_cleaned",
    "education_cleaned",
    "skill_cleaned"
]

# 训练分类器
gnb.fit(
    X_train[used_features].values,
    X_train["enrolled_cleaned"]
)
print("X[].values", X_train[used_features].values)
print(X_train[used_features])
print(X_train["985_cleaned"])
print(type(X_train))


y_pred = gnb.predict(X_test[used_features])

# 打印结果
print("Number of mislabeled points out of a total {} points : {},performance {:05.2f}".format(
    X_test.shape[0],
    (X_test["enrolled_cleaned"] != y_pred).sum(),
    100 * (1 - (X_test["enrolled_cleaned"] != y_pred).sum() / X_test.shape[0])
))

print(X_test["enrolled_cleaned"])
print("y_pred:", y_pred)

print((X_test["enrolled_cleaned"] != y_pred))

# 看看数据格式
# for d in used_features:
#     print(d)
#     print(data[d])
