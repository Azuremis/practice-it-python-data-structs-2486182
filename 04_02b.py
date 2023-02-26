from collections import namedtuple, defaultdict
from pprint import pprint
from csv import reader

def main():
    #add code here
    #read data/OrderItems.csv
    #Create workable objects with each line
    # OrderItemID,OrderID,ProductID,Quantity
    res = defaultdict(int)
    with open('data/OrderItems.csv', 'r') as open_csv:
        read = reader(open_csv)
        OrderItem = namedtuple("OrderItem", next(read))
        for line in read:
            Item = OrderItem(*line)
            res[Item.ProductID] += int(Item.Quantity)
    pprint(dict(res))



    return

if __name__ == "__main__":
    main()