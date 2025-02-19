#pre-problem

from math import gcd


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return str(newnum // common) + '/' + str(newden // common)

num1, den1, num2, den2 = map(int, input().split())
fraction1, fraction2 = Fraction(num1, den1), Fraction(num2, den2)
print(fraction1.__add__(fraction2))
