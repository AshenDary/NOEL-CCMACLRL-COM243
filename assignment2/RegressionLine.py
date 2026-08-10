import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([52, 57, 61, 65, 70])

# Regression parameters
m = 4.4
b = 47.8

# Predicted y values (for plotting the line)
x_line = np.linspace(0, 6, 100)
y_line = m * x_line + b

# Plot
plt.figure(figsize=(7, 5))
plt.scatter(x, y, color='blue', label='Actual Data', zorder=3)
plt.plot(x_line, y_line, color='red', label=f'Regression Line: y = {m}x + {b}')

plt.title('Hours Studied vs Exam Score')
plt.xlabel('Hours Studied (x)')
plt.ylabel('Exam Score (y)')
plt.legend()
plt.grid(True)
plt.savefig('regression_plot.png', dpi=150)
plt.show()
