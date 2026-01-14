import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.linspace(0, 10, 50)
y_perfect = 3 * x

noise = np.random.normal(0, 2, 50)
y_real = y_perfect + noise

print("Perfect y:")
print(y_perfect)

print("Noisy y:")
print(y_real)

# Plot 1: Perfect vs Noisy
plt.figure(figsize=(8, 5))

plt.plot(x, y_perfect, label="Perfect y = 3x", linewidth=2)
plt.scatter(x, y_real, label="Noisy data y = Perfect y + noise", s = 35)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Perfect Function vs Noisy Data")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Plot 2: Bell curve of noise
plt.figure(figsize=(8, 5))

# Histogram of noise
plt.hist(noise, bins=15, density=True, alpha=0.7, label="Noise histogram")

# Theoretical Gaussian curve
mu = 0
sigma = 2
x_curve = np.linspace(-8, 8, 400)
gaussian_curve = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-(x_curve-mu)**2/(2*sigma**2))

plt.plot(x_curve, gaussian_curve, linewidth=2, label="Gaussian curve")

plt.xlabel("Noise value")
plt.ylabel("Probability density")
plt.title("Gaussian Noise (Bell Curve)")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
