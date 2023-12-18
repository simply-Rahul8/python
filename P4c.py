class IntegerToRoman:
    def __init__(self, num):
        self.num = num
        self.table = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
    
    def convert_to_roman(self):
        res = ""
        for cap, roman in self.table:
            d, m = divmod(self.num, cap)
            res += roman * d
            self.num = m
        return res
num = int(input("Enter an integer: "))
converter = IntegerToRoman(num)
print(converter.convert_to_roman())
