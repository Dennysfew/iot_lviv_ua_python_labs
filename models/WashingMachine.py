from models.HomeAppliances import HomeAppliances


class WashingMachine(HomeAppliances):

    def __init__(self, name: str, price: int, weight: int, weight_maximum_load: int):
        super().__init__(name, price, weight)
        self.weight_maximum_load = weight_maximum_load

    def __str__(self):
        return f'The name is {self.name} price is {self.price} weight {self.weight} the weight maximum you can load ' \
               f'{self.weight_maximum_load}'
