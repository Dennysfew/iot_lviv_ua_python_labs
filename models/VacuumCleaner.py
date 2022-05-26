from models.HomeAppliances import HomeAppliances


class VacuumCleaner(HomeAppliances):

    def __init__(self, name: str, price: int, weight: int, washing_func: bool):
        super().__init__(name, price, weight)
        self.washing_func = washing_func

    def get_vacuum_cleaner(self) -> str:
        return "The name is {} price is {} weight {}, has washing func: {}".format(self.name, self.price, self.weight,
                                                                                   self.washing_func)
