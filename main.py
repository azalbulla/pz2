# main.py
from modulis.modul1 import plot_xy, print_table_xy
from modulis.modul2 import func_cube, func_square, func_circle_area, func_sin, func_cos, func_abs
from modulis.modul3 import timer, debug

def frange(a, b, step):
    out, x = [], a
    if step > 0:
        while x <= b:
            out.append(x)
            x += step
    else:
        while x >= b:
            out.append(x)
            x += step
    return out

def choose_func():
    print("Выбери функцию (номер):")
    print("1) func_cube(x)")
    print("2) func_square(x)")
    print("3) func_circle_area(x) — π*x^2 (аргумент как радиус)")
    print("4) func_sin(x)")
    print("5) func_cos(x)")
    print("6) func_abs(x)")
    ch = input("Твой выбор: ").strip()
    mapping = {
        "1": (func_cube, "func_cube(x)"),
        "2": (func_square, "func_square(x)"),
        "3": (func_circle_area, "func_circle_area(x)"),
        "4": (func_sin, "func_sin(x)"),
        "5": (func_cos, "func_cos(x)"),
        "6": (func_abs, "func_abs(x)"),
    }
    return mapping.get(ch, (func_cube, "func_cube(x)"))

@timer
@debug
def compute_y(f, X):
    return [f(x) for x in X]

if __name__ == "__main__":
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    step = float(input("Введите шаг: "))
    f, fname = choose_func()

    X = frange(a, b, step)
    Y = compute_y(f, X)

    print(f"\nФункция: {fname}")
    print_table_xy(X, Y)
    print("\nОкно графика откроется отдельно.")
    plot_xy(X, Y, a=min(a, b), b=max(a, b), title=fname)
