import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

# Make a scatter plot
plt.scatter(x, y, color="blue", label="Data points", s=100, marker="o")

# Add a new point
plt.scatter(3.5, 6, color="red", label="New point", s=100, marker="*")

# Titles and labels
plt.title("Simple Test Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# Show plot
plt.show()

# Keep window open when running from terminal
input("Press Enter to exit...")
