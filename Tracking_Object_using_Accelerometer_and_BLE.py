from bluepy.btle import UUID, Peripheral
import struct
import math

# Define the UUIDs of the Accelerometer Service and Characteristic
ACCELEROMETER_SERVICE_UUID = UUID("0000FFE1-0000-1000-8000-00805F9B34FB")
ACCELEROMETER_CHARACTERISTIC_UUID = UUID("0000FFE1-0000-1000-8000-00805F9B34FB")

# Connect to the BLE Beacon
peripheral = Peripheral("12:34:56:78:90:00")
accelerometer_service = peripheral.getServiceByUUID(ACCELEROMETER_SERVICE_UUID)
accelerometer_characteristic = accelerometer_service.getCharacteristics(ACCELEROMETER_CHARACTERISTIC_UUID)[0]

while True:
    # Read the accelerometer data
    data = accelerometer_characteristic.read()
    x, y, z = struct.unpack("<hhh", data)

    # Calculate the magnitude of the acceleration vector
    magnitude = math.sqrt(x*x + y*y + z*z)

    # Detect whether the tag is moving or stationary
    if magnitude < 0.1:
        print("Tag is stationary")
    else:
        print("Tag is moving")
