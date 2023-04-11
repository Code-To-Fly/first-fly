from tello_solectric_pl import TelloEDU
from time import sleep

print("Początek testów... tworzymy obiekt i próbujemy połączyć się, a potem wystartować...")
dron = TelloEDU()

if dron.connect():
    print("Połączenie udane - start...")
    dron.takeoff()
    sleep(2)
    print("I lądujemy...")
    dron.land()
else:
    print("Połączenie nieudane - nic nie testujemy...")

print("Koniec testu")

