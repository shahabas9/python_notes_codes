class ChemistShopInventory:
    def __init__(self):
        self.inventory = self.load_inventory()

    def load_inventory(self):
        try:
            with open('inventory.txt', 'r') as file:
                inventory_data = file.readlines()
            inventory = {}
            for item in inventory_data:
                name, quantity = item.strip().split(',')
                inventory[name] = int(quantity)
        except FileNotFoundError:
            inventory = {}
        return inventory

    def save_inventory(self):
        with open('inventory.txt', 'w') as file:
            for item, quantity in self.inventory.items():
                file.write(f"{item},{quantity}\n")

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def sell_item(self, item, quantity):
        if item in self.inventory:
            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                print(f"Sold {quantity} {item}(s).")
            else:
                print(f"Insufficient quantity of {item} in inventory.")
        else:
            print(f"{item} not found in inventory.")

    def display_inventory(self):
        print("\nCurrent Inventory:")
        print("------------------------------")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")
        print("------------------------------")

def main():
    chemist_shop = ChemistShopInventory()

    while True:
        print("\nOptions:")
        print("1. Add Item to Inventory")
        print("2. Sell Item from Inventory")
        print("3. Display Inventory")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity to add: "))
            chemist_shop.add_item(item, quantity)
            chemist_shop.save_inventory()

        elif choice == '2':
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity to sell: "))
            chemist_shop.sell_item(item, quantity)
            chemist_shop.save_inventory()

        elif choice == '3':
            chemist_shop.display_inventory()

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



