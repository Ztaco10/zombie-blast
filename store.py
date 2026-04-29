import time
import json
import os

with open(os.path.join(os.path.dirname(__file__), "shop.json")) as f:
    STORE_ITEMS = json.load(f)["items"]

def print_banner():
    print("""
  _____ _______ ____  _____  ______
 / ____|__   __/ __ \|  __ \|  ____|
| (___    | | | |  | | |__) | |__
 \___ \   | | | |  | |  _  /|  __|
 ____) |  | | | |__| | | \ \| |____
|_____/   |_|  \____/|_|  \_\______|
    """)

def print_menu(coins):
    print(f"  Coins: {coins}\n")
    print("  What would you like to buy?\n")
    for i, item in enumerate(STORE_ITEMS, start=1):
        print(f"  [{i}] {item['name']} - {item['price']} coins")
    print(f"  [{len(STORE_ITEMS) + 1}] Return to Battle")
    print()

def enter_store(coins):
    print_banner()
    time.sleep(0.3)

    while True:
        print_menu(coins)

        choice = input("  Enter your choice: ").strip()
        print()

        if not choice.isdigit():
            print("  Invalid choice, try again.\n")
            continue

        choice = int(choice)

        if choice == len(STORE_ITEMS) + 1:
            print("  Returning to battle...\n")
            time.sleep(0.4)
            return coins

        if 1 <= choice <= len(STORE_ITEMS):
            item = STORE_ITEMS[choice - 1]
            if coins >= item["price"]:
                coins -= item["price"]
                print(f"  You bought a {item['name']}! Remaining coins: {coins}\n")
            else:
                print(f"  Not enough coins! Need {item['price']}, you have {coins}.\n")
            time.sleep(0.3)
        else:
            print("  Invalid choice, try again.\n")

if __name__ == "__main__":
    enter_store(100)
