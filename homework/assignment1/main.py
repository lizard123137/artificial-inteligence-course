import numpy as np

from matplotlib import pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as kNN
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC as SVM
from sklearn.tree import DecisionTreeClassifier as DT
from sklearn.tree import plot_tree

#
# Loading and processing data
#

dataset = load_diabetes()

X = dataset.data
y = dataset.target

mask = y >= 150
y[mask] = 1
y[~mask] = 0

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state = 41
)

#
# Creating models and training
#

accuracies = []
confusion_matricies = []
models = [
    kNN(n_neighbors = 4),   # k=4 -> 4 neighbors
    SVM(),                  # by default C=1.0
    DT()                    # default settings
]

for model in models:
    model.fit(X_train, y_train);
    y_pred = model.predict(X_test)
    accuracies.append(accuracy_score(y_test, y_pred))
    confusion_matricies.append(confusion_matrix(y_test, y_pred))

#
# Displaying test results
#

plt.figure(figsize = (20, 10))
tree_vis = plot_tree(
    models[2],
    feature_names = dataset.feature_names,
    class_names = ['Tak', "Nie"],
    fontsize = 8,
    filled = True
)

plt.figure(figsize = (20, 10))
plt.bar(["kNN", "Maszyna Wektorow Nosnych", "Drzewo Decyzyjne"], accuracies)
plt.title("Dokladnosci modeli")
plt.xlabel("Model")
plt.ylabel("Dokladnosc")

# For testing purposes print confusion_matrices
print("kNN")
print(confusion_matricies[0])
print("SVM")
print(confusion_matricies[1])
print("DT")
print(confusion_matricies[2])

plt.show()
