from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        """Convert the fraction to a string for printing."""
        return f"{self.__numerator}/{self.__denominator}"

    def simplify(self):
        """Simplify the fraction."""
        divisor = gcd(self.__numerator, self.__denominator)
        self.__numerator //= divisor
        self.__denominator //= divisor
        return self

    def __add__(self, other):
        """Add two fractions."""
        num = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        denom = self.__denominator * other.__denominator
        return Fraction(num, denom).simplify()

    def __sub__(self, other):
        """Subtract two fractions."""
        num = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        denom = self.__denominator * other.__denominator
        return Fraction(num, denom).simplify()

    def __mul__(self, other):
        """Multiply two fractions."""
        num = self.__numerator * other.__numerator
        denom = self.__denominator * other.__denominator
        return Fraction(num, denom).simplify()

    def __truediv__(self, other):
        """Divide two fractions."""
        if other.__numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        num = self.__numerator * other.__denominator
        denom = self.__denominator * other.__numerator
        return Fraction(num, denom).simplify()

    @staticmethod
    def from_float(value):
        """Convert a float to a fraction."""
        denominator = 10 ** len(str(value).split(".")[1])  # Number of decimal places
        numerator = int(value * denominator)
        return Fraction(numerator, denominator).simplify()

    @classmethod
    def identity_fraction(cls):
        """Return the identity fraction (1/1)."""
        return cls(1, 1)


# آزمایش کلاس Fraction
if __name__ == "__main__":
    # نمونه‌سازی از کسرها
    fraction1 = Fraction(3, 4)
    fraction2 = Fraction(5, 6)

    # جمع، تفریق، ضرب و تقسیم
    print(f"جمع: {fraction1 + fraction2}")
    print(f"تفریق: {fraction1 - fraction2}")
    print(f"ضرب: {fraction1 * fraction2}")
    print(f"تقسیم: {fraction1 / fraction2}")

    # ساده‌سازی
    fraction3 = Fraction(15, 24)
    print(f"کسر قبل از ساده‌سازی: {fraction3}")
    print(f"کسر بعد از ساده‌سازی: {fraction3.simplify()}")

    # تبدیل عدد اعشاری به کسر
    decimal_fraction = Fraction.from_float(0.75)
    print(f"کسر تبدیل شده از عدد 0.75: {decimal_fraction}")

    # کسر هویت
    identity = Fraction.identity_fraction()
    print(f"کسر هویت: {identity}")
