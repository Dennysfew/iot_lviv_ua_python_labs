from models.HomeAppliances import HomeAppliances


class Television(HomeAppliances):

    def __init__(self, name: str, price: int, weight: int, size_of_screen: int):
        super().__init__(name, price, weight)
        self.size_of_screen = size_of_screen

    def get_television(self) -> str:
        return "The name is {} price is {} weight {} has the screen of size {}".format(self.name, self.price,
                                                                                       self.weight, self.size_of_screen)
