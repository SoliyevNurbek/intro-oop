class Mobile:

    def __init__(self, name: str, color: str, price: float, ram: int, quantity: int):
        self.name  = name
        self.color = color
        self.price = price
        self.ram   = ram
        self.quantity = quantity

    def info(self) -> str:
        pass
    def Total(self) -> float:
        return self.quantity*self.price



m1 = Mobile('Samsung s21', 'black', 700.00, 6, 34)
m2 = Mobile('Ihone 12 pro', 'gray', 600.00, 4, 21)

print(m1.Total())
print(m2.Total())
