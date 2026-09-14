# Raspberry Pi Automatic Temperature Fan Control

A lightweight Python script that automatically monitors your Raspberry Pi's CPU temperature and controls a 5V/3.3V DC cooling fan using a transistor switch circuit. 

It keeps the Pi completely silent when running cool and triggers the fan automatically when under high processor load.

## 🚀 Features
* **Smart Temperature Hysteresis:** The fan turns on at 55°C and cools the system down to 45°C before shutting off, preventing the fan from rapidly toggling on/off.
* **Low Overhead:** Uses the `gpiozero` library to evaluate state changes efficiently without spamming system resources or hardware pins.
* **Boot Integration:** Configured to run automatically as a background system service via `systemd`.

## 🛠️ Hardware Requirements
* **Raspberry Pi** (Any model with a 40-pin header)
* **5V or 3.3V DC Fan**
* **NPN Transistor** (e.g., 2N2222, BC547)
* **1kΩ Resistor** (Protects the GPIO pin)
* **Flyback Diode** (e.g., 1N4148 - optional but recommended)

### Wiring
* **Fan Positive (+):** Connected to Physical Pin 2 or 4 (5V Power)
* **Fan Negative (-):** Connected to Transistor Collector (C)
* **Transistor Emitter (E):** Connected to Physical Pin 30 or 34 (GND)
* **Transistor Base (B):** Connected through a 1kΩ Resistor to Physical Pin 31 (GPIO 6)

## 📦 Installation & Setup

1. Clone this repository to your Raspberry Pi:
   ```bash
   git clone https://github.com
   cd YOUR_REPO_NAME
   ```

2. Make sure the `gpiozero` library is installed:
   ```bash
   sudo apt update
   sudo apt install python3-gpiozero
   ```

3. Test the script manually:
   ```bash
   python3 fan_control.py
   ```

## 🤖 Running at Boot (Systemd Service)

To make this script run seamlessly in the background whenever your Pi turns on:

1. Create a service file:
   ```bash
   sudo nano /etc/systemd/system/fancontrol.service
   ```
2. Paste the following configuration (adjust the path to your file if necessary):
   ```ini
   [Unit]
   Description=Raspberry Pi Custom Fan Control Service
   After=multi-user.target

   [Service]
   Type=simple
   ExecStart=/usr/bin/python3 /home/pi/YOUR_REPO_NAME/fan_control.py
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```
3. Enable and start the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable fancontrol.service
   sudo systemctl start fancontrol.service
   ```
