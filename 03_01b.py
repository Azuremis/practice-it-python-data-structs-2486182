from collections import namedtuple

def can_take_order(driver, num_packages):
    return driver.car_capacity >= num_packages

def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    #check if they can take a certain order, given their car's capacity.
    Driver = namedtuple("Driver", ['name', 'car_model', 'car_capacity'])
    
    # delivery drivers
    jokes_driver = Driver('Tyrone', 'Toyota Prius', 7)
    crazy_driver = Driver('Don', 'Ford Mustang', 4)
    fast_driver = Driver('Dwayne', 'Honda Civic', 3)

    print(fast_driver)
    print(can_take_order(fast_driver, 5))
    return

if __name__ == "__main__":
    main()