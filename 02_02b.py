from collections import deque


def palindrome_checker(word):
    # create a deque
    word_deque = deque(word)
    # check if the deque is a palindrome
    while len(word_deque) > 1:
        print(word_deque)
        if word_deque.popleft() != word_deque.pop():
            return False
    return True

def main():
    
    print(palindrome_checker("racecar"))
    return

if __name__ == "__main__":
    main()