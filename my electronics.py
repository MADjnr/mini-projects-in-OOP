class ElectronicDevice:

    def __init__(self, voltage, weight, height, color):
        self.voltage = voltage
        self.weight = weight
        self.height = height
        self.color = color


class TV(ElectronicDevice):

    def __init__(self, voltage, weight, height, color, max_num_channels):
        ElectronicDevice.__init__(self, voltage, weight, height, color)
        self.max_num_channels = max_num_channels

class Computer(ElectronicDevice):

    def __init__(self, voltage, weight, height, color, memory, hard_drive):
        ElectronicDevice.__init__(self, voltage, weight, height, color)
        self.memory = memory
        self.hard_drive = hard_drive

class Desktop(Computer):

    def __init__(self, voltage, weight, height, color, memory, hard_drive, monitor_size):
        Computer.__init__(self, voltage, weight, height, color, memory, hard_drive)
        self.monitor_size = monitor_size

class Laptop(Computer):

    def __init__(self, voltage, weight, height, color, memory, hard_drive, has_mouse_pad):
        Computer.__init__(self, voltage, weight, height, color, memory, hard_drive)
        self.has_mouse_pad = has_mouse_pad



