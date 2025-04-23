# Assignment-today-
def compare_root_finding_methods(f, df, a=None, b=None, x0=None, tol=1e-6, max_iter=100):
    """
    Compare Bisection and Newton-Raphson methods in terms of steps to convergence.

    Parameters:
    f (function): Function whose root is sought.
    df (function): Derivative of f (required for Newton-Raphson).
    a, b (float): Interval [a, b] for Bisection (must have f(a)*f(b) < 0).
    x0 (float): Initial guess for Newton-Raphson.
    tol (float): Tolerance for convergence.
    max_iter (int): Maximum allowed iterations.

    Returns:
    dict: Results for both methods, including root, steps, and success status.
    """
    results = {
        'Bisection': {'root': None, 'steps': 0, 'converged': False},
        'Newton-Raphson': {'root': None, 'steps': 0, 'converged': False}
    }

    # Bisection Method
    if a is not None and b is not None:
        if f(a) * f(b) >= 0:
            print("Bisection method requires f(a) and f(b) to have opposite signs.")
        else:
            for i in range(max_iter):
                c = (a + b) / 2
                if abs(f(c)) < tol or (b - a) / 2 < tol:
                    results['Bisection']['root'] = c
                    results['Bisection']['steps'] = i + 1
                    results['Bisection']['converged'] = True
                    break
                elif f(a) * f(c) < 0:
                    b = c
                else:
                    a = c
            else:
                results['Bisection']['root'] = (a + b) / 2
                results['Bisection']['steps'] = max_iter

    # Newton-Raphson Method
    if x0 is not None:
        x = x0
        for i in range(max_iter):
            df_x = df(x)
            if abs(df_x) < 1e-10:  # Avoid division by zero
                print("Newton-Raphson failed: Derivative near zero.")
                break
            x_next = x - f(x) / df_x
            if abs(x_next - x) < tol:
                results['Newton-Raphson']['root'] = x_next
                results['Newton-Raphson']['steps'] = i + 1
                results['Newton-Raphson']['converged'] = True
                break
            x = x_next
        else:
            results['Newton-Raphson']['root'] = x
            results['Newton-Raphson']['steps'] = max_iter

    return results
