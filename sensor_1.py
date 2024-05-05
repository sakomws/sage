import time

class LEDSimulator:
    def __init__(self):
        self.green_led = "Solid Green"
        self.blue_led = "Solid Blue"
        self.red_led = "Solid Red"
        self.battery_level = 100
        self.coordinates = (0, 0)
        self.collision_warning = False

    def update_battery_level(self, level):
        self.battery_level = level

    def update_coordinates(self, x, y):
        self.coordinates = (x, y)

    def set_collision_warning(self, status):
        self.collision_warning = status

    def simulate(self):
        while True:
            if self.battery_level < 20:
                self.green_led = "Blinking Green"
            else:
                self.green_led = "Solid Green"

            if self.collision_warning:
                self.red_led = "Blinking Red"
            else:
                self.red_led = "Solid Red"

            print("Green LED:", self.green_led)
            print("Blue LED:", self.blue_led)
            print("Red LED:", self.red_led)
            print()

            time.sleep(1)

# Example usage
simulator = LEDSimulator()
simulator.update_battery_level(15)
simulator.set_collision_warning(True)
simulator.simulate()