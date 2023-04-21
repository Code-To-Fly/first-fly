from tello_solectric_pl import TelloEDU
import logging

print("Początek testów... tworzymy obiekt i próbujemy połączyć się, a potem pobrać podstawowe informacje...")
dron = TelloEDU(True)
TelloEDU.LOGGER.setLevel(logging.DEBUG)

if dron.connect():
    print("Połączenie udane - rozpoczynam...")
    battery = dron.get_battery()
    temp = dron.get_temperature()
    print(f"Status: Bateria: {battery}% / Temperatura: {temp} C")
else:
    print("Połączenie nieudane - nic nie testujemy...")

print("Koniec testu")

