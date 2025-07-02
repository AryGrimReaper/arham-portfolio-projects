from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
iris = load_iris()
X = iris.data   # Features (petal/sepal sizes)
y = iris.target # Labels (0=setosa, 1=versicolor, 2=virginica)

# Split the data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print("Prediction accuracy:", accuracy)

# Predict a sample manually
sample = [[5.1, 3.5, 1.4, 0.2]]  # Example flower
predicted_class = model.predict(sample)[0]
print("Predicted flower class:", iris.target_names[predicted_class])

