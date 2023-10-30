import smbus
import time

DEVICE = 0x23

POWER_DOWN = 0x00
POWER_ON = 0x01
RESET = 0x07
ONE_TIME_HIGH_RES_MODE_1 = 0x20

bus = smbus.SMBus(1)

def convertToNumber(data):
    result = (data[1] + (256 * data[0])) / 1.2
    return result

def categorizeLightLevel(light_level):
    if light_level > 1000:
        return "Too Bright"
    elif light_level > 500:
        return "Bright"
    elif light_level > 100:
        return "Medium"
    elif light_level > 10:
        return "Dark"
    else:
        return "Too Dark"

def readLight(addr=DEVICE):
    data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE_1)
    light_level = convertToNumber(data)
    return light_level

def main():
    while True:
        light_level = readLight()
        category = categorizeLightLevel(light_level)
        print("Light Level : " + format(light_level, '.2f') + " lx (" + category + ")")
        time.sleep(0.5)

if __name__ == "__main__":
    main()
