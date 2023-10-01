import smbus
import time

I2C_ADDRESS = 0x23
CONTROL_REGISTER = 0x00
DATA_REGISTER = 0x0C

bus = smbus.SMBus(1)

bus.write_byte_data(I2C_ADDRESS, CONTROL_REGISTER, 0x03)  

def read_light_intensity():
    light_data = bus.read_word_data(I2C_ADDRESS, DATA_REGISTER)
    light_intensity = light_data / 1.2
    return light_intensity

def categorize_light_intensity(intensity):
    if intensity > 10000:
        return "Too Bright"
    elif intensity > 5000:
        return "Bright"
    elif intensity > 2000:
        return "Medium"
    elif intensity > 500:
        return "Dark"
    else:
        return "Too Dark"

try:
    while True:
        intensity = read_light_intensity()
        category = categorize_light_intensity(intensity)
        print(f"Light Intensity: {intensity} lux - Category: {category}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by the user.")
