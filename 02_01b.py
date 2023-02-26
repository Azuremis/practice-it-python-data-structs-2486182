from collections import deque
def main():
    
    # create a deque
    foods = deque(maxlen=5)
    # add items to the deque
    foods.append("STA001") 
    ordered_foods = ["DES003", "STA002", "ENT004", "ENT001"]
    foods.extend(ordered_foods)
    # add an item to the left of the deque
    foods.appendleft("DES005")
    # add an item to the right of the deque
    foods.append("DES002")
    
    # print the deque
    print(foods)

if __name__ == "__main__":
    main()