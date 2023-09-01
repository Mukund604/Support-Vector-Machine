#Importing the required Libraries
import numpy as np

class SVM:
    #Making a constructor function for our classifier
    def __init__(self, lr = 0.001, l_param = 0.1, n = 1000):
        self.lr = lr
        self.l_param = l_param
        self.n = n
        self.m = None
        self.c = None
        
    #Fit method
    def fit(self, X, y):
        n_samples, n_features = X.shape
        y_ = np.where(y <= 0, -1, 1)
        self.m = np.zeros(n_features)
        self.c = 0
        
        
        #Gradient descent 
        for _ in range(self.n):
            for idx,xi in enumerate(X):
                condition = y_[idx] * (np.dot(xi,self.m) - self.c) >= 1
                if(condition):
                    
                    dm =  (2 * self.l_param * self.m)
                    self.m -= self.lr * dm
                    
                else:
                    dm = (2 * self.l_param * self.m - np.dot(xi,y_[idx]))
                    dc = y_[idx]
                    
                    self.m -= self.lr * dm
                    self.c -= self.lr * dc
                    
    #Predicting the values from the above model that we created.
    def predict(self, X):
        approx = np.dot(X,self.m) - self.c
        return np.sign(approx)