from vehicle import Vehicle, Car, Aeroplane

volvo = Car("Volvo", 100, 5)

learjet = Aeroplane("My_lear", 600, 25)

learjet.introduce()

volvo.introduce()

volvo.emergency_stop()

learjet.fly()

volvo.wind_windows_down()

learjet.raise_landing_gear()


