class Terrestrial:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print(f"{self.name} is driving on land.")

    def stop(self):
        print(f"{self.name} has stopped.")


class Aquatic:
    def __init__(self, name):
        self.name = name

    def sail(self):
        print(f"{self.name} is sailing on water.")

    def anchor(self):
        print(f"{self.name} has anchored.")


class AmphibiousVehicle(Terrestrial, Aquatic):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
        Terrestrial.drive(self)

    def stop(self):
        Terrestrial.stop(self)

    def sail(self):
        Aquatic.sail(self)

    def anchor(self):
        Aquatic.anchor(self)

    def switch_mode(self):
        print(f"{self.name} is switching between land and water modes.")


amphibious_car = AmphibiousVehicle(name="AmphiCar")

amphibious_car.drive()
amphibious_car.stop()

amphibious_car.sail()
amphibious_car.anchor()

amphibious_car.switch_mode()