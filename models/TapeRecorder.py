from models.HomeAppliances import HomeAppliances


class TapeRecorder(HomeAppliances):

    def __init__(self, name: str, price: int, weight: int, number_of_musics: int):
        super().__init__(name, price, weight)
        self.number_of_musics = number_of_musics


    def get_radio_receiver(self) -> str:
        return "The name is {} price is {} weight {} has the number of musics equel: {}".format(self.name, self.price,
                                                                                                self.weight,
                                                                                                self.number_of_musics)
