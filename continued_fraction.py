# -*- coding: utf-8 -*-
# @author Lyle
# version 5-19

from decimal import *


def continued_fraction(x):
    '''
    calc continued_fraction approximate
    generate a continued_fraction list
    '''
    a = []
    a.append(int(x))
    x -= a[-1]
    while x != 0 and len(a) < 30:
        a.append(int(1/x))
        x = (1/x) - a[-1]
    return a


def calc_continued_fraction(x):
    '''
    use continued fraction list 
    calc continued fraction approximate
    '''
    a = Decimal(0.0)
    for i in x[::-1]:
        a = (1/(i+a))
    return 1/a


def rational_continued_fraction(x, y):
    '''
    calc rational fraction's continued fraction approximate
    '''
    if x < y:
        x, y = y, x
    k = x/y
    p, q, m, n = 0, 1, 1, 0

    while x != 0 and y != 0:
        k = x/y
        p, q = q, p + q * k
        m, n = n, m + n * k
        x, y = y, x % y
        # print k, q, n, x, y

if __name__ == '__main__':
    '''
    getcontext().prec = 100
    while True:
        x = continued_fraction(Decimal(input()))
        print x
        print calc_continued_fraction(x)
    '''
    while True:
        x, y = map(int, raw_input().split())
        rational_continued_fraction(x, y)
