import os
import time
from gpiozero import OutputDevice

temp_log = [];
fan_pin = 6;
on_temp = 55.0;
off_temp = 45.0;
fan = OutputDevice(fan_pin);


def get_pi_temp():
   with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
      temp = int(file.read()) / 1000
      return temp

print("Pi Temperature Control Script Started...")
print(f"Target ON: {on_temp}°C | Target OFF: {off_temp}°C")
try:
   while True:
      temp = get_pi_temp()
      if temp > on_temp and not fan.value:
         fan.on()
         print(f"[{time.strftime('%X')}] CPU is {temp}°C: Fan turned ON")
      elif temp <= off_temp and fan.value:
         fan.off()
         print(f"[{time.strftime('%X')}] CPU is {temp}°C: Fan turned OFF")
      ##temp_log.append(temp)
      time.sleep(5)
except KeyboardInterrupt:
   print(f'monitoring stopped by user')

