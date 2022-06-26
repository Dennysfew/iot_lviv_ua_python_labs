from models.HomeAppliances import HomeAppliances


class VacuumCleaner(HomeAppliances):

    def __init__(self, name: str, price: int, weight: int, washing_func: bool):
        super().__init__(name, price, weight)
        self.washing_func = washing_func

    def __str__(self):
        return f'The name is {self.name} price is {self.price} weight {self.weight}, has washing func: ' \
               f'{self.washing_func}'
