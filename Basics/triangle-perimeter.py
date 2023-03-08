
class triangle():

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        calc_peri = self.side1 + self.side2 + self.side3
        return calc_peri


value1 = triangle(1, 2, 3)
result = value1.perimeter()
print(f"=> Perimeter = {result} units.")
