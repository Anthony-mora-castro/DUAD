class Bus():
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.passenger_counter = 0
    
    def add_passenger(self):
        if self.passenger_counter < self.max_capacity:
            self.passenger_counter +=1
            print(f'A subido un pasajero, hay {self.passenger_counter} pasajeros a bordo')
        else:
            print(f'El bus esta lleno, no se pueden subir mas pasajeros')

    def remove_passenger(self):
        if self.passenger_counter > 0 :
            self.passenger_counter -= 1
            print(f'Un pasajero a bajado del bus, quedan {self.passenger_counter} a bordo ')
        else:
            print(f'No hay pasajeros a bordo')

bus = Bus(2)

bus.add_passenger()
bus.add_passenger()
bus.remove_passenger()



