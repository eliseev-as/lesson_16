class Cash():
    amount = 0

    def __init__(self, amount=amount):
        self.amount = amount

    def top_up(self, x):
        self.amount += x

    def count_1000(self):
        print(self.amount // 1000)

    def take_away(self, x):
        balance = self.amount - x
        if balance >= 0:
            self.amount = balance
        else:
            print("Недостаточно денег")
