#Importing the required libraries
import numpy as np
from SVM_P import SVM
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#Making a synthetic dataset from the sklean library
X, y = datasets.make_blobs(n_samples=200, n_features=2, centers=2, cluster_std=1.05, random_state=4000)
y = np.where(y <= 0, -1, 1)

#Splitting the dataset into Training and Testing sets
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=12)



#Initializing our classifier and fitting the dataset that we are given
clf = SVM(lr = 0.001, l_param=0.001)
clf.fit(X_train, y_train)
approx = clf.predict(X_test)

#Checking the Accuracy of the model that we created.
def Accuracy(y_true, y_pred):
    return np.sum(y_true == y_pred) / len(y_true)
print("The accuracy of the model is:",Accuracy(y_test,approx))


#Visualizing the linear decision boundary that our model created using graph
def visualize_svm():
        def get_hyperplane_value(x, w, b, offset):
            return (-w[0] * x + b + offset) / w[1]

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.scatter(X[:, 0], X[:, 1], marker="o", c=y)

        x0_1 = np.amin(X[:, 0])
        x0_2 = np.amax(X[:, 0])

        x1_1 = get_hyperplane_value(x0_1, clf.m, clf.c, 0)
        x1_2 = get_hyperplane_value(x0_2, clf.m, clf.c, 0)

        x1_1_m = get_hyperplane_value(x0_1, clf.m, clf.c, -1)
        x1_2_m = get_hyperplane_value(x0_2, clf.m, clf.c, -1)

        x1_1_p = get_hyperplane_value(x0_1, clf.m, clf.c, 1)
        x1_2_p = get_hyperplane_value(x0_2, clf.m, clf.c, 1)

        ax.plot([x0_1, x0_2], [x1_1, x1_2], "y--")
        ax.plot([x0_1, x0_2], [x1_1_m, x1_2_m], "k")
        ax.plot([x0_1, x0_2], [x1_1_p, x1_2_p], "k")

        x1_min = np.amin(X[:, 1])
        x1_max = np.amax(X[:, 1])
        ax.set_ylim([x1_min - 3, x1_max + 3])

        plt.show()

visualize_svm()