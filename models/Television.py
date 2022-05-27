from models.HomeAppliances import HomeAppliances


class Television(HomeAppliances):

    def __init__(self, name: str, price: int, weight: int, size_of_screen: int):
        super().__init__(name, price, weight)
        self.size_of_screen = size_of_screen

    def __str__(self):
        return f'The name is {self.name} price is {self.price} weight {self.weight} has the screen of ' \
               f'size {self.size_of_screen}'
