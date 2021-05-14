#coding:utf-8
from sklearn import neural_network
import numpy as np
import sys
from sklearn.model_selection import train_test_split

x = np.zeros((996, 12))
y = np.zeros(996, dtype=int)

f = open("C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_predict\\similarity_class_matrtix.txt")
lines = f.readlines()
now = -1
for line in lines:
    now += 1
    t = line.split(" ")
    if len(t) == 2:
        y[int(now/2)] = int(t[1])
    else:
        for i in range(12):
            x[int(now/2), i] = float(t[i])

#print(x)
#print(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.01)
mlp = neural_network.MLPClassifier(hidden_layer_sizes=(300), activation="relu",
                                   solver='adam', alpha=0.0001, batch_size='auto',
                                   learning_rate="constant", learning_rate_init=0.01,
                                   power_t=0.5, max_iter=2000, tol=1e-4)
mlp.fit(x_train, y_train)
r = mlp.score(x_train, y_train)
print("accuracy:", r)
y_predict = mlp.predict(x_test)  # 预测
print(y_predict)
print(y_test)

print(mlp.score(x_test, y_test))