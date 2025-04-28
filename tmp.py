class Book:

    REGULAR: int = 0
    NEW_RELEASE: int = 1
    CHILDREN: int = 2

    def __init__(self, title: str, price_code: int):
        self.title = title
        self.price_code = price_code

    def get_charge(self, days_rented) -> float:
            amount = 0
            if self.price_code == Book.REGULAR:
                amount += 2
                if days_rented > 2:
                    amount += (days_rented - 2) * 1.5
            elif self.price_code == Book.NEW_RELEASE:
                amount += days_rented * 3
            elif self.price_code == Book.CHILDREN:
                amount += 1.5
                if days_rented > 3:
                    amount += (days_rented - 3) * 1.5
            return amount
    def get_frequent_renter_points(self, days_rented):
        points = 1
        if self.price_code == Book.NEW_RELEASE and days_rented > 1:
            points += 1
        return points
