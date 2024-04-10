import math

def add(x, y):
    return [vx + vy for vx, vy in zip(x, y)]


def times(x, y):
    return [vx * vy for vx, vy in zip(x, y)]


def vpow(x, n):
    return [vx**n for vx in x]

