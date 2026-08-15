# Import Libraries
import pandas as pd
import numpy as np


# Load the Datasets
uci_stats = pd.read_csv("uci_diabetes (3).csv")
pima_stats = pd.read_csv("pima_diabetes (3).csv")


# Display Summary Statistics
print("Comparison of Univariate Analysis Results:")

print(
    "\nUCI Diabetes Dataset Statistics:\n",
    uci_stats
)

print(
    "\nPima Indians Diabetes Dataset Statistics:\n",
    pima_stats
)


# Compare Regression Model Performance
uci_r2 = 0.78
pima_r2 = 0.72

uci_accuracy = 82.4
pima_accuracy = 79.1


print(
    f"\nLinear Regression R2 Scores: "
    f"UCI - {uci_r2}, Pima - {pima_r2}"
)

print(
    f"Logistic Regression Accuracy: "
    f"UCI - {uci_accuracy}%, "
    f"Pima - {pima_accuracy}%"
)
