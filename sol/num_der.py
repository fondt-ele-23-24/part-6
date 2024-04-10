def num_der1(x, f, eps=1e-9):
    return (f(x + eps) - f(x)) / eps


def num_der2(x, f, eps=1e-9):
    return (f(x + 0.5* eps) - f(x - 0.5*eps)) / eps