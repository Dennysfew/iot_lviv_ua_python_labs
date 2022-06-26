from models.HomeAppliances import HomeAppliances


class TapeRecorder(HomeAppliances):

    def __init__(self, name: str, price: int, weight: int, number_of_musics: int):
        super().__init__(name, price, weight)
        self.number_of_musics = number_of_musics

    def __str__(self):
        return f'The name is {self.name} price is {self.price} weight {self.weight} has the number of ' \
               f'musics equal: {self.number_of_musics}'

