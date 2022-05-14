#!/home/khalid/miniconda3/bin/python

import sys
import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def our_accuracy_score(true, predicted):
    return (true == predicted).mean()

class StochasticLReg:
    def __init__(self, lr: int, epochs: int, probability_threshold: float = 0.5, random_state = None):
        self.lr = lr # The learning rate
        self.epochs = epochs # The number of training epochs
        self.probability_threshold = probability_threshold # If the output of the sigmoid function is > probability_threshold, the prediction is considered to be positive (True)
                                                           # otherwise, the prediction is considered to be negative (False)
        self.random_state = random_state # The random state will be used set the random seed for the sake of reproducability

    def _prepare_input(self, X):
        # Here, we add a new input with value 1 to each example. It will be multipled by the bias
        return np.concatenate(([1], X), axis=0)
    
    def _prepare_target(self, y):
        # Here, we convert True to +1 and False to -1
        return np.where(y, 1, -1)

    def _initialize(self, num_weights: int, stdev: float = 0.01):
        # Here, we initialize the weights using a normally distributed random variable with a small standard deviation
        # self.w = np.random.randn(num_weights) * stdev
        self.w = np.zeros(num_weights)

    def _gradient(self, X, y):
        wx = np.dot(X,self.w.T)
        exp = np.exp(y * wx)
        return - ((y*X) / (1+exp))

    def _update(self, X, y):
        self.w = self.w - self.lr * self._gradient(X,y)

    def fit(self, X, y):
        np.random.seed(self.random_state) # First, we set the seed
        X = self._prepare_input(X.T) # Then we prepare the inputs
        y = self._prepare_target(y) # and prepare the targets too
        self._initialize(X.shape[0]) # and initialize the weights randomly
        for ep in range(self.epochs): # Then we update the weights for a certain number of epochs
            self._update(X, y)
        return self # Return self to match the behavior of Scikit-Learn's LinearRegression fit()
    
    # def predict(self, X):
    #     X = self._prepare_input(X)
    #     return sigmoid(np.dot(X,self.w)) > self.probability_threshold


for line in sys.stdin:
    features = line.strip().split(",")
    features = np.array([float(x) for x in features])
    our_model = StochasticLReg(lr=0.001, epochs=1000, random_state=0).fit(features[:-1], features[-1])
    for i,w in enumerate(our_model.w):
        print(f'w{i}\t{w}')
