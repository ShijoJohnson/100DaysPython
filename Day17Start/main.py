# class Car:
#     def __init__(self, seats):
#         self.seats = seats
#         self.spare_tires = 1
#         print(f"Seats is {self.seats}")
#
#     def enter_race_mode(self, seats):
#         self.seats = seats
#
#
# car = Car(4)
# print(car.seats, car.spare_tires)
# car.enter_race_mode(2)
# print(car.seats, car.spare_tires)


class Instagram:
    def __init__(self, username):
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


messi = Instagram("Messi")
print(f"Messi Initial is {messi.username}, {messi.following}, {messi.followers}")
shijo = Instagram("Shijo")
shijo.follow(messi)
print(f"Messi is {messi.username}, {messi.following}, {messi.followers}")
print(f"Shijo is {shijo.username}, {shijo.following}, {shijo.followers}")
