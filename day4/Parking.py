from abc import ABC ,abstractmethod
class vehicle():
    def __init__(self):
        self.__name=name
        self.__number=number
        self.__spotstat=spotstat
    def set_name(self,name):
        self.__name=name
    def set_number(self,number):
        self.__number=number
    def set_spotstat(self,spotstat):
        self.__spotstat=spotstat
    @abstractmethod
    def calculate_parking_fee(self, hours):
        pass
    @abstractmethod
    def display(self):
        pass
    def get_name():
        return self.name
    def get_number():
        return self.number
    def get_spotstat():
        return self.spotstat
    
class bike(vehicle):
    def __init__(self,name,number,spotstat):
        super().__init__(name,number,spotstat)
    def calculate_parking_fee(self, hours):
        return hours * 2  # Example: $2 per hour
    def display(self):
        print(f"Bike: {self.get_name()} {self.get_number()}, Plate: {self.get_spotstat()}")
class bike(vehicle):
    def __init__(self,name,number,spotstat):
        super().__init__(name,number,spotstat)
    def calculate_parking_fee(self, hours):
        return hours * 5  # Example: $2 per hour
    def display(self):
        print(f"car: {self.get_name()} {self.get_number()}, Plate: {self.get_spotstat()}")
class Truck(vehicle):
    def __init__(self,name,number,spotstat):
        super().__init__(name,number,spotstat)
    def calculate_parking_fee(self, hours):
        return hours * 9  # Example: $2 per hour
    def display(self):
        print(f"Bike: {self.get_name()} {self.get_number()}, Plate: {self.get_spotstat()}")
class ParkingSpot():
    def __init__(self,s):
        self.s=s
        self.occupied=False
        self.vehicle=vehicle
        pass
    def assign():
        if occupied is False:
            occupied=True
    def remove_():
        if occupied is True:
            occupied=False










class ParkingLot:
    def __init__(self):
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        for spot in self.spots:
            print(spot.get_status())

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if not spot.occupied:
                if spot.assign(vehicle):
                    print(f"Vehicle parked in a {spot.size} spot.")
                    return
        print("No suitable spot available.")

    def unpark_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.occupied and spot.vehicle.get_number() == vehicle.get_number():
                spot.remove_vehicle()
                print(f"Parking fee for vehicle {vehicle.get_plate_number()}: ${vehicle.calculate_parking_fee(2)}")  # Example: 2 hours
                return
        print(f"Vehicle {vehicle.get_number()} not found in parking lot.")


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Processed payment of ${amount} via Cash.")


class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processed payment of ${amount} via Card.")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processed payment of ${amount} via UPI.")
def main():
    
    lot = ParkingLot()

    
    lot.add_spot(ParkingSpot('S'))
    lot.add_spot(ParkingSpot('M'))
    lot.add_spot(ParkingSpot('L'))
    lot.add_spot(ParkingSpot('XL'))

    bike = Bike("Honda", "CBR", "ABC123")
    car = Car("Toyota", "Corolla", "XYZ456")
    suv = SUV("Nissan", "Xterra", "LMN789")
    truck = Truck("Ford", "F150", "DEF101")

    lot.park_vehicle(bike)
    lot.park_vehicle(car)
    lot.park_vehicle(suv)
    lot.park_vehicle(truck)

    lot.show_spots()

    lot.unpark_vehicle(car)

    payment_method = input("Enter payment method (cash/card/upi): ").lower()
    amount = 5  
    if payment_method == 'cash':
        payment = CashPayment()
    elif payment_method == 'card':
        payment = CardPayment()
    elif payment_method == 'upi':
        payment = UPIPayment()
    else:
        print("Invalid payment method.")
        return

    payment.process_payment(amount)

main()
