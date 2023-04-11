from tello_solectric_pl import TelloEDU
from time import sleep

print("Początek testów... tworzymy obiekt i próbujemy połączyć się, a potem wystartować...")
dron = TelloEDU(info_all=True)

if dron.connect():
    print("Połączenie udane - start...")
    dron.takeoff()
    sleep(2)
    # pobieramy informacje o statusie drona
    height = dron.get_height()
    battery = dron.get_battery()
    print(f"Dron na wysokości {height}; bateria naładowana: {battery}")
    print("I lądujemy...")
    dron.land()
else:
    print("Połączenie nieudane - nic nie testujemy...")

print("Koniec testu")

