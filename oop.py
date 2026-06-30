import math

class Fraction:                             # Builidng a class for fraction

    def __init__(self, num, den):               # making it in simplest form automatically
        # simplify fraction automatically
        gcd = math.gcd(num, den)
        self.num = num // gcd
        self.den = den // gcd

    def __str__(self):
        if self.den == 1:                       # if base is 1 then it will return only numerator
            return str(self.num)
        else:
            return f"{self.num}/{self.den}"
    
    def __add__(self, other):                               # addition of two fractions
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __sub__(self, other):                            # subtraction of two fractions                                     
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __mul__(self, other):                        # multiplication of two fractions                         
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __truediv__(self, other):                  # division of two fractions  
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)
    
    def __eq__(self, other):                    # checking equality of two fractions
        return self.num * other.den == self.den * other.num
    



# User input
n = int(input("Enter numerator of first fraction: "))
d = int(input("Enter denominator of first fraction: "))
o = input('''Enter operator (+, -, *, /, ==): 
          1."+"for addition
          2."-" for subtraction                 
          3."*" for multiplication
          4."/" for division
          5."==" for equality check
            ''')                        # explaining the operator to user
f1 = Fraction(n, d)

n2 = int(input("Enter numerator of second fraction: "))
d2 = int(input("Enter denominator of second fraction: "))
f2 = Fraction(n2, d2)

if o == "+":                                # using conditional statements to perform the operation based on user input
    print(f"{f1} + {f2} = {f1 + f2}")
elif o == "-":
    print(f"{f1} - {f2} = {f1 - f2}")
elif o == "*":
    print(f"{f1} * {f2} = {f1 * f2}")
elif o == "/":
    print(f"{f1} / {f2} = {f1/f2}")
elif o == "==":
    print(f"{f1} == {f2} = {f1 == f2}")
else:
    print("Invalid operator.")
