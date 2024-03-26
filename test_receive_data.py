import serial
import re

def parse_arduino_msg(data_txt):
    pattern = r"masse: (.+),stable: (.+)"
    match = re.search(pattern, data_txt)

    # If match is found, extract values and return them
    if match:
        masse = float(match.group(1))
        is_stable = match.group(2)=='1'
        return {"masse":masse, "stable": is_stable}
    else:
        return {"masse":0, "stable": False}


def read_arduino_data(arduino):
    # readline() blocks until a whole line is returned by the arduino
    data_txt = arduino.readline().decode().strip()
    data = parse_arduino_msg(data_txt)
    masse = data["masse"]
    tension_pos = data["tension"]
    