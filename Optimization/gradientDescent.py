import numpy as np
import matplotlib.pyplot as plt

# Function to be minimized
def f(x, y):
    return x**2 + 10*y**2 + 5*np.sin(x)

# Gradient of f(x, y)
def grad_f(x, y):
    return np.array([2*x + 5*np.cos(x), 20*y])

# Gradient Descent 
def gradient_descent(f, grad_f, start, lr = 0.1, tol = 1e-6, max_steps = 1000):
    x, y = start
    losses = []
    path = []

    for i in range(max_steps):
        loss = f(x, y)
        losses.append(loss)
        path.append((x, y))

        grad = grad_f(x, y)
        grad_norm = np.linalg.norm(grad)

        print(f"Step {(i + 1):3d} | x={x:.6f}, y={y:.6f}, loss={loss:.6f}, grad_norm={grad_norm:.6f}")

        # stopping condition
        if grad_norm < tol:
            print("\nConverged!") #This means that gradient has reached possible minimum value
            break

        # update rule
        x -= lr * grad[0]
        y -= lr * grad[1]

    return x, y, losses, path


# Plot loss curve
def plot_loss(losses):
    plt.figure()
    plt.plot(losses)
    plt.xlabel("Iteration")
    plt.ylabel("Loss f(x,y)")
    plt.title("Gradient Descent Loss Curve")
    plt.grid(True)
    plt.show()


# Plot descent path
def plot_path(path):
    xs = [p[0] for p in path]
    ys = [p[1] for p in path]

    plt.figure()
    plt.plot(xs, ys, marker='o')
    plt.scatter(0, 0, color='red', label="Minimum (0,0)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gradient Descent Path")
    plt.legend()
    plt.grid(True)
    plt.show()


# Main Function
if __name__ == "__main__":

    start_point = (2.0, 1.0)
    learning_rate = 0.05

    print("Starting Gradient Descent...\n")

    x_final, y_final, losses, path = gradient_descent(
        f,
        grad_f,
        start=start_point,
        lr=learning_rate
    )

    print("\nFinal result:")
    print("x =", x_final)
    print("y =", y_final)
    print("f(x,y) =", f(x_final, y_final))
    print("grad_f = " , grad_f(x_final, y_final))

    plot_loss(losses)
    plot_path(path)
