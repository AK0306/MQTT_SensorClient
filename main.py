# Complete project details at https://RandomNerdTutorials.com
#
import machine,time
from Lib.onewire import OneWire
from Lib.ds18x20 import DS18X20

ds_pin = machine.Pin(4)

ds_sensor = DS18X20(OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    print(rom)
    print(ds_sensor.read_temp(rom))
  time.sleep(5)