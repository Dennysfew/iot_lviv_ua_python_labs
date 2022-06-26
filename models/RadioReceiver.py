from models.HomeAppliances import HomeAppliances


class RadioReceiver(HomeAppliances):

    def __init__(self, name: str, price: int, weight: int, number_of_saved_station: int):
        super().__init__(name, price, weight)
        self.number_of_saved_station = number_of_saved_station

    def __str__(self):
        return f'The name is {self.name} price is {self.price} weight {self.weight},' \
               f'number of station that you can save:{self.number_of_saved_station} '
