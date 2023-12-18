class PowerCalculator:
    def __init__(self):
        self.x = float(input("Enter the base value (x): "))
        self.n = int(input("Enter the exponent value (n): "))
    
    def calculate_power(self):
        result = 1.0
        if self.n < 0:
            self.x = 1.0 / self.x
            self.n = -self.n
        while self.n > 0:
            if self.n % 2 == 1:
                result *= self.x
            self.x *= self.x
            self.n //= 2
        return result
num=int(input("enter the number: "))
calculator = PowerCalculator(num)
print(calculator.calculate_power())
