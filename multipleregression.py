
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Select Age and BMI features
diabetes_X = diabetes_X[:, [0, 2]]

# Split into training and testing data
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# Create Linear Regression model
regr = linear_model.LinearRegression()

# Train the model
regr.fit(diabetes_X_train, diabetes_y_train)

# Predict the test data
diabetes_y_pred = regr.predict(diabetes_X_test)

# Display results
print("Coefficients:\n", regr.coef_)
print("Intercept:\n", regr.intercept_)

print(
    "Mean squared error:\n",
    mean_squared_error(diabetes_y_test, diabetes_y_pred)
)

print(
    "Coefficient of determination: %.2f"
    % r2_score(diabetes_y_test, diabetes_y_pred)
)

# Prepare data for 3D plotting
x = diabetes_X_test[:, 0]
y = diabetes_X_test[:, 1]

# Create 3D plots
fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

axes = [ax1, ax2, ax3]

# Plot actual diabetes values
for ax in axes:
    ax.scatter(
        x, y, diabetes_y_test,
        color="#70b3f0",
        s=20,
        alpha=0.7
    )

    ax.set_xlabel("Age", fontsize=12)
    ax.set_ylabel("BMI", fontsize=12)
    ax.set_zlabel("Diabetes", fontsize=12)

# Set different viewing angles
ax1.view_init(elev=28, azim=120)
ax2.view_init(elev=4, azim=114)
ax3.view_init(elev=60, azim=-165)

# Display R2 score
r2 = r2_score(diabetes_y_test, diabetes_y_pred)
fig.suptitle("R2 = %.2f" % r2, fontsize=20)

fig.tight_layout()
plt.show()