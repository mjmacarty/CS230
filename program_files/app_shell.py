import sys
import pandas_datareader as pdr
from time import time, sleep

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
def track(watchlist):
    pass

def edit_list():
    pass

def add_list():
    watchlist = []
    while True:
        symbol = input("Enter a ticker symbol: ").upper()
        if symbol == '':
            break
        if symbol not in watchlist:
            watchlist.append(symbol)
    return sorted(watchlist)

def delete_list():
    pass



actions = {'1': track, '2' : edit_list, '3' : add_list, '4' : delete_list}

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice in '1234':
            actions[choice]()
        elif choice == '5':
            print("Thank you for using stocktracker!")
            sys.exit(0)
        else:
            print (f"{choice} is not a valid selection")



if __name__ == "__main__":
    main()