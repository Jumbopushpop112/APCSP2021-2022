cars = ["Ford", "BMW", "Volvo", "Toyota"]
cars.sort()
cars.append("Chevy")
print(cars)
removedCar = cars.pop(2)
print("Removed car",removedCar)
cars.append("Volvo")
print("After a 2nd volvo has eben added")
print(cars)
things = [False, "0.4", True, 1]
if False not in things:
    print("False is not there!")
else:
    print("False is there!")
#while ___ not in someList:
    #
    #do something like add to the list avoid duplicates