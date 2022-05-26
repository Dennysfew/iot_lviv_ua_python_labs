from models.HomeAppliances import HomeAppliances


class RadioReceiver(HomeAppliances):

    def __init__(self, name: str, price: int, weight: int, number_of_saved_station: int):
        super().__init__(name, price, weight)
        self.number_of_saved_station = number_of_saved_station

    def get_radio_receiver(self) -> str:
        return "The name is {} price is {} weight {}, number of station that you can save: ".format(
            self.name,
            self.price,
            self.weight,
            self.number_of_saved_station)
