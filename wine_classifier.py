import pandas as pd
import numpy as np

data = pd.read_csv('https://s3.amazonaws.com/demo-datasets/wine.csv') #read directly from the link

numeric_data = data.drop('color', axis=1)

numeric_data = (numeric_data - np.mean(numeric_data)) / np.std(numeric_data)


import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit(numeric_data).transform(numeric_data)

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]
y = principal_components[:,1]
plt.plot(principal_components[:,0], principal_components[:,1])
plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1"); plt.ylabel("Principal Component 2")
plt.show()

def accuracy(predictions, outcomes):
    for i in predictions:
        for j in outcomes:
            if i==j:
                Percentage = 100*np.mean(predictions == outcomes)
    return Percentage

x = np.array([1,2,3])
y = np.array([1,2,4])

percentage = accuracy(x, y)

number_of_low_quality = accuracy(0, data["high_quality"])

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, data['high_quality'])
library_predictions = knn.predict(numeric_data)

predictions_accuracy = accuracy(library_predictions, data["high_quality"])

import random 

n_rows = data.shape[0]

random.seed(123)
selection = random.sample(range(n_rows), 10)

predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])

my_predictions = [knn_predict(p, predictors[training_indices,:], outcomes, k=5) for p in predictors[selection]]

percentage = accuracy(my_predictions, data.high_quality[selection] )
