import os
import csv


class CarBase:

    car_type = ""

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        pass

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):

    car_type = "car"

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        return


class Truck(CarBase):

    car_type = "truck"

    def __init__(self, brand, photo_file_name, carrying, body_whl: str):
        super().__init__(brand, photo_file_name, carrying)

        spl = body_whl.split("x")[:3]
        spl.extend([""]*(3-len(spl)))
        whl = [float(x) if x else 0.0 for x in spl]
        self.body_width = whl[0]
        self.body_height = whl[1]
        self.body_length = whl[2]
        return

    def get_body_volume(self):
        return self.body_length * self.body_height * self.body_width


class SpecMachine(CarBase):

    car_type = "spec_machine"

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        return


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)

        for row in reader:
            car = get_car(row)
            if car is not None:
                car_list.append(car)

    return car_list


def get_car(lst: list):
    car = None
    if len(lst) != 7:
        return car

    brand = lst[1]
    photo_file_name = lst[3]
    carrying = float(lst[5])

    if lst[0] == "car":
        passenger_seats_count = int(lst[2])
        car = Car(brand, photo_file_name, carrying, passenger_seats_count)
    elif lst[0] == "truck":
        body_whl = lst[4]
        car = Truck(brand, photo_file_name, carrying, body_whl)
    elif lst[0] == "spec_machine":
        extra = lst[6]
        car = SpecMachine(brand, photo_file_name, carrying, extra)

    return car
