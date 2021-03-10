import json


# The Car class:
class Car:
    def __init__(self, brand, model, consumption, plateNum, pricePerHour, pricePerDay, pricePerWeek, availability):
        self.brand = brand
        self.model = model
        self.consumption = consumption
        self.plateNum = plateNum
        self.pricePerHour = pricePerHour
        self.pricePerDay = pricePerDay
        self.pricePerWeek = pricePerWeek
        self.availability = availability
        self.user_renter = None

# Prints only the brand, model and plate number of car, but it can be changed
    def __str__(self):
        return self.brand + "; " + self.model + "; " + self.plateNum


# The User class
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

# The Manager class
class Manager:
    cars_list = []

    def __init__(self):

        # extracting from JSON file
        with open("cars.json", "r") as car_list:
            data = json.load(car_list)
            for c in data:
                car = Car(brand=c["brand"], model=c["model"], consumption=c["consumption"], plateNum=c["plateNum"],
                          pricePerHour=c["pricePerHour"], pricePerDay=c["pricePerDay"], pricePerWeek=c["pricePerWeek"],
                          availability=c["availability"])
                self.cars_list.append(car)

    # Method that prints all available cars
    def show_available_cars(self):
        print("Cars available: ")
        for obj in self.cars_list:
            if obj.availability:
                print(obj)
        print("\n")

    # Method that counts available cars
    def check_available_cars(self, car_list):
        count = 0
        for c in car_list:
            if c.availability:
                count += 1
        return count

    # Method that makes the order
    def make_order(self, car_list, period, user):
        count = self.check_available_cars(car_list)
        for c in car_list:
            price = 0
            if not c.availability:
                print("This " + c.brand + " " + c.model + " is not available \n")
                continue
            c.availability = False
            c.user_renter = user
            if period == "hour":
                price += c.pricePerHour
            if period == "day":
                price += c.pricePerDay
            if period == "week":
                price += c.pricePerWeek
            if count > 3:
                price = round(price * 0.7)
            print(
                "The renting price for this " + c.brand + " " + c.model + " is " + price.__str__() + " a "
                + period + " rented by: " + c.user_renter.username + " \n")

# instancing Manager
manager = Manager()

# First showing all available cars
manager.show_available_cars()

# User Stoqn orders two cars
manager.make_order([manager.cars_list[2],
                    manager.cars_list[6]
                    ],
                   "day",
                   User("stoqn","stoqnov","stoqn@mail.com"))

# User Petar Trying to order cars, but some of them are not available
manager.make_order([manager.cars_list[0],
                    manager.cars_list[1],
                    manager.cars_list[2],
                    manager.cars_list[6],
                    manager.cars_list[8]
                    ],
                   "week",
                   User("petar","petarov","petar@mail.com"))

# showing remaining available cars
manager.show_available_cars()