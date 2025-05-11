def f(x):
    return x**3 - x - 2  # Example function

def f_prime(x):
    return 3*x**2 - 1  # Derivative of f(x)

def newton_raphson(x0, tol=1e-6, max_iter=100):
    steps = 0
    while steps < max_iter:
        fx = f(x0)
        dfx = f_prime(x0)
        if abs(fx) < tol:
            break
        x0 = x0 - fx / dfx
        steps += 1
    return steps

def bisection(a, b, tol=1e-6, max_iter=100):
    steps = 0
    if f(a) * f(b) >= 0:
        return -1  # Root not guaranteed in interval
    while (b - a)/2.0 > tol and steps < max_iter:
        mid = (a + b) / 2.0
        if f(mid) == 0:
            break
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
        steps += 1
    return steps

def compare_methods():
    nr_steps = newton_raphson(x0=1.5)
    bis_steps = bisection(a=1, b=2)
    
    print(f"Newton-Raphson method converged in {nr_steps} steps")
    print(f"Bisection method converged in {bis_steps} steps")

compare_methods()