import matplotlib.pyplot as plt

def plot_xy(x, y, a=None, b=None, title="График X–Y"):
    if a is not None and b is not None:
        x2, y2 = [], []
        for xi, yi in zip(x, y):
            if a <= xi <= b:
                x2.append(xi)
                y2.append(yi)
    else:
        x2, y2 = x, y

    plt.figure()
    plt.plot(x2, y2)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)
    plt.grid(True)
    plt.show()

def print_table_xy(x, y):
    width = max(len(f"{val:.3f}") for val in (x + y))
    row_x = " ".join(f"{val:{width}.3f}" for val in x)
    row_y = " ".join(f"{val:{width}.3f}" for val in y)
    print("X:", row_x)
    print("Y:", row_y)

if __name__ == "__main__":
    import math
    xs = [i * 0.5 for i in range(-6, 7)]
    ys = [math.sin(t) for t in xs]
    print_table_xy(xs, ys)
    plot_xy(xs, ys, a=-2, b=2, title="sin(x) на [-2, 2]")
