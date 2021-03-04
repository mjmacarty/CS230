import sys

def display_menu():
    print(
        """
    Welcome to StockTracker
    1. Track Watchlist
    2. Edit Watchlist
    3. Add Watchlist
    4. Delete Watchlist
    5. Exit    
        """
    )
def track():
    pass

def edit_list():
    pass

def add_list():
    pass

def delete_list():
    pass



actions = {'1': track, '2' : edit_list, '3' : add_list, '4' : delete_list}

def main():
    display_menu()
    choice = input("Enter your choice: ")
    if choice in '1234':
        actions[choice]()
    elif choice == '5':

        sys.exit(0)
    else:
        print (f"{choice} is not a valid selection")



if __name__ == "__main__":
    main()