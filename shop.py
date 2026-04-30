import time
import json
import os
import database
import login

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
    print("  What would you like to buy?\n")
    for i, item in enumerate(STORE_ITEMS, start=1):
        print(f"  [{i}] {item['name']} - {item['price']} coins")
    print(f"  [{len(STORE_ITEMS) + 1}] Return to Battle")
    print(f"  [{len(STORE_ITEMS) + 2}] Item Guide")
    print()
    print(f"  You have {coins} coins")

def enter_store():
    print_banner()
    time.sleep(0.3)

    while True:
        username = login.getUser()
        coins = database.getCoins(username)
        print_menu(coins)
        for item in STORE_ITEMS:
            database.addItem(item["name"], item["price"], item.get("description", ""))

        choice = input("  Enter your choice: ").strip()
        print()

        if not choice.isdigit():
            print("  Invalid choice, try again.\n")
            continue

        choice = int(choice)

        if choice == len(STORE_ITEMS) + 1:
            print("  Returning to battle...\n")
            time.sleep(0.4)
            return

        if choice == len(STORE_ITEMS) + 2:
            print("  --- Item Guide ---\n")
            for i, item in enumerate(STORE_ITEMS, start=1):
                print(f"  [{i}] {item['name']}")
            print()
            guide_choice = input("  Choose an item to learn more (or 0 to go back): ").strip()
            if guide_choice.isdigit():
                guide_choice = int(guide_choice)
                if 1 <= guide_choice <= len(STORE_ITEMS):
                    item = STORE_ITEMS[guide_choice - 1]
                    print(f"\n  {item['name']} ({item['price']} coins)")
                    print(f"  {item.get('description', 'No description available.')}\n")
                    temp = input("Press enter to continue\n")
            continue

        if 1 <= choice <= len(STORE_ITEMS):
            item = STORE_ITEMS[choice - 1]

            if coins >= item["price"]:
                coins -= item["price"]
                database.updateCoins(username, coins)
                database.addInventory(username, item["name"])

                print(f"  You bought a {item['name']}! Remaining coins: {coins}\n")
            
            else:
                print(f"  Not enough coins! Need {item['price']}, you have {coins}.\n")

            time.sleep(0.3)
        else:
            print("  Invalid choice, try again.\n")
"""
if __name__ == "__main__":
    from mathGame import mathGame
    game = mathGame("add", "easy")
    game.coins = 100
    enter_store(game)
"""