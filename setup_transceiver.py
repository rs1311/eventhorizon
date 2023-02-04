import sys
import time

import serial

if __name__ == "__main__":

    # Welcome screen
    welcome_msg = "+-+-+-+-+-+-+-+ +-+-+\n"
    welcome_msg += "|W|e|l|c|o|m|e| |t|o|\n"
    welcome_msg += "+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+\n"
    welcome_msg += "|T|r|a|n|s|c|e|i|v|e|r| |S|e|t|u|p|\n"
    welcome_msg += "+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+\n"
    welcome_msg += "|P|r|o|g|r|a|m|\n"
    welcome_msg += "+-+-+-+-+-+-+-+\n"
    print(welcome_msg)

    print("Enter COM port:")
    print("-----------------------")
    com_port = input()

    print("\nTo configure a TT&C transceiver, enter 1")
    print("To configure a Payload transceiver, enter 2")
    print("------------------------------------------------")
    option = input("Enter mode:\n")

    print("\nEnter channel [000-127]:")
    print("-----------------------")
    channel = input()
    print()

    if 'COM' not in com_port:
        com_port = 'COM'+com_port

    ser = serial.Serial(com_port, baudrate=9600, timeout=2)

    ser.write(b"AT")
    time.sleep(1)
    ret = ser.readline()

    if ret != b"OK\r\n":
        print("Not ok, please retry")
        print("Operation aborted, no configuration was done")
        print("Check your connections again\n")
        sys.exit()
    else:

        ser.write(B"AT+P8")
        time.sleep(0.01)
        print(ser.readline())

        ser.write(B"AT+RX")
        time.sleep(0.01)
        print(ser.readline())
        print(ser.readline())
        print(ser.readline())
        print(ser.readline())
        print()

        print("AT commands output:")
        print("----------------------")

    at_channel_command = ("AT+" + channel).encode("utf-8")

    if option == "1":
        # Channel = 005
        ser.write(at_channel_command)
        time.sleep(0.01)
        print(ser.readline())

        # Baud rate = 9600
        ser.write(b"AT+B9600")
        time.sleep(0.01)
        print(ser.readline())

    elif option == "2":
        # Channel = 125
        ser.write(at_channel_command)
        time.sleep(0.01)
        print(ser.readline())

        # Baud rate = 115200
        ser.write(b"AT+B115200")
        time.sleep(0.01)
        print(ser.readline())

    print("\nConfiguration success!\n")
