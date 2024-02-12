class Vehicle():
    def __init__(self, name, max_speed, seating):
        self.name = name
        self.max_speed = max_speed
        self.seating = seating
    
    def start_up(self):
        print(f"{self.name} is starting up")

    def shut_down(self):
        print(f"{self.name} is shutting down")
    
    def introduce(self):
        print(f"This is a {self.name} with a max speed of {self.max_speed} and seating of {self.seating}")


class Car(Vehicle):
    def emergency_stop(self):
        print(f"{self.name} is executing am emergency stop")

    def change_tyres(self):
        print(f" {self.name} is executing am e,mergency stop")
    
    def wind_windows_down(self):
        print(f"{self.name} is winding windows down")


class Aeroplane(Vehicle):
    def fly(self):
        print(f"{self.name} is flying")
    
    def raise_landing_gear(self):
        print(f"{self.name} is raising landing gear")
