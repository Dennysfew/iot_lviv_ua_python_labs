from models.HomeAppliances import HomeAppliances


class MusicCenter(HomeAppliances):

    def __init__(self, name: str, price: int, weight: int, max_volume: int, min_volume: int):
        super().__init__(name, price, weight)
        self.max_volume = max_volume
        self.min_volume = min_volume

    def get_music_center(self) -> str:
        return "The name is {} price is {} weight {}, max_volume {}, min_volume {}".format(self.name, self.price,
                                                                                           self.weight,
                                                                                           self.max_volume,
                                                                                           self.min_volume)

    def __str__(self):
        return "The name is {} price is {} weight {}, max_volume {}, min_volume {}".format(self.name, self.price,
                                                                                           self.weight,
                                                                                           self.max_volume,
                                                                                           self.min_volume)


