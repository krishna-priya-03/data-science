
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import svm

# Load breast cancer dataset
cancer = datasets.load_breast_cancer()

# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data,
    cancer.target,
    test_size=0.3,
    random_state=109
)

# Create SVM classifier
clf = svm.SVC(kernel='linear')

# Train the model
clf.fit(X_train, y_train)

# Predict test data
y_pred = clf.predict(X_test)

# Display actual and predicted values
print("Actual values:", y_test)
print("Predicted values:", y_pred)

# Calculate performance measures
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))