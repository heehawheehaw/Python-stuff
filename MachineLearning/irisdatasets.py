from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)
print(iris.target)
print(iris.target_names)
print(type(iris.target))
print(iris.data.shape)
print(iris.target.shape)

#KNN model
from sklearn.neighbours import KNeighboursClassifier
knn = KNeighboursClassifier(n_neighbours=1)
x = iris.datasets
y = iris.target 
knn.fit(x,y)
print(knn.predict([[5.1,3.5,1.4,0.2]]))

from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(X, y, testsize=0.25)
print(x_train.shape)
print(x_test.shape)
knn.fit[x_train,y_train]
predictions = knn.predict(x_test)
print(predictions)
from sklearn import metrics
performance = metrics.accuracy_score[y_test, predictions]
print(performance)

k_values = {}
k = 1
while k <= 25:
	knn = KNeighborsClassifier(n_neighbours=k)
	knn.fit(x_train,y_train)
	predictions = knn.predict(x_test)
	performance = metrics.accuracy_score[y_test, predictions]
	k_values[k] = round(performance,4)
	k += 1
print(k_values)
import matplotlib.pyplot as plt
matplotlibt inline
plt.plot(list(k_values.keys()), list(k_values.values()))
plt.xlabel('Values of X')
plt.ylabel('Performance')
plt.show()

#logistic regression
from sklearn.linear_model LogisticRegression
logreg = LogisticRegression()
logreg.fit(x_train, y_train)
print(logreg.predict_proba([[6.7,3.3,5.7,2.5]]))
predictions_logreg = logreg.predict(X_test)
perfromance = logreg = metrics.accuracy_score(y_test,predictions_logreg)
print(performance_logreg)