from models.MusicCenter import MusicCenter
from models.RadioReceiver import RadioReceiver
from models.TapeRecorder import TapeRecorder
from models.Television import Television
from models.VacuumCleaner import VacuumCleaner
from models.WashingMachine import WashingMachine

bosh = MusicCenter("Music center", 400, 25, 1, 40)
print(bosh.get_music_center())
print(str(bosh))
samsung = WashingMachine("Washing machine", 500, 66, 9)
print(samsung.get_washing_machine())
philips = VacuumCleaner("Vacuum cleaner", 70, 4, False)
print(philips.get_vacuum_cleaner())
kivi = Television("TV", 60, 8, 43)
print(kivi.get_television())
giradischi = TapeRecorder("Tape recorder", 25, 2, 50)
print(giradischi.get_radio_receiver())
okord = RadioReceiver("Radio receiver", 20, 3, 20)
print(okord.get_radio_receiver())
