import serial
import re

def parse_arduino_msg(data_txt):
    pattern = r"masse: (.+),tension position: (.+)"
    match = re.search(pattern, data_txt)

    # If match is found, extract values and return them
    if match:
        masse = match.group(1)
        tension = match.group(2)
        return {"masse":masse, "tension": tension}
    else:
        return {"masse":0, "tension": 0}


def read_arduino_data(arduino):
    # readline() blocks until a whole line is returned by the arduino
    data_txt = arduino.readline().decode().strip()
    data = parse_arduino_msg(data_txt)
    masse = data["masse"]
    tension_pos = data["tension"]
    