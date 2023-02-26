from collections import namedtuple
from csv import reader

def main():
    #read data/Customer.csv
    #Create workable objects with each line
    # CustomerID,FirstName,LastName,Email,Phone,Address,City,State,Zipcode
    with open('data/Customer.csv', 'r') as open_csv:
        read = reader(open_csv)
        Person = namedtuple("Person", next(read))
        for line in read:
            person = Person(*line)
            print(person.CustomerID, person.FirstName, person.LastName)
    

    return

if __name__ == "__main__":
    main()