from abc import ABC, abstractmethod

# Inventory Manager
class InventoryManager:
    _instance = None
    _inventory = {
        "Margherita": 0,
        "Pepperoni": 5,
        "Cheese": 3,
        "Olives": 2,
        "Mushrooms": 34,
    }

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(InventoryManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory


# Abstract Pizza
class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


# Pizza Types
class Margherita(Pizza):
    def get_description(self) -> str:
        return "Margherita"

    def get_cost(self) -> float:
        return 5.0


class Pepperoni(Pizza):
    def get_description(self) -> str:
        return "Pepperoni"

    def get_cost(self) -> float:
        return 6.0


# Toppings
class ToppingDecorator(Pizza):
    def __init__(self, base_pizza: Pizza):
        self.base_pizza = base_pizza

    def get_description(self) -> str:
        return self.base_pizza.get_description()

    def get_cost(self) -> float:
        return self.base_pizza.get_cost()


class Cheese(ToppingDecorator):
    def get_description(self) -> str:
        return self.base_pizza.get_description() + ", Cheese"

    def get_cost(self) -> float:
        return self.base_pizza.get_cost() + 1.0


class Olives(ToppingDecorator):
    def get_description(self) -> str:
        return self.base_pizza.get_description() + ", Olives"

    def get_cost(self) -> float:
        return self.base_pizza.get_cost() + 0.5


class Mushrooms(ToppingDecorator):
    def get_description(self) -> str:
        return self.base_pizza.get_description() + ", Mushrooms"

    def get_cost(self) -> float:
        return self.base_pizza.get_cost() + 0.7


# Payment Methods
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class PayPal(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using PayPal.")


class CreditCard(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using Credit Card.")


def main():
    inventory_manager = InventoryManager()

    print("\nChoose your base:")
    print("1. Margherita ($5.0)")
    print("2. Pepperoni ($6.0)")

    pizza_choice = input("Enter the number of your choice: ")
    pizza = None

    if pizza_choice == '1' and inventory_manager.check_and_decrement("Margherita"):
        pizza = Margherita()
    elif pizza_choice == '2' and inventory_manager.check_and_decrement("Pepperoni"):
        pizza = Pepperoni()
    else:
        print("Error!")
        return

    while True:
        print("\nAvailable toppings:")
        print("1. Cheese ($1.0)")
        print("2. Olives ($0.5)")
        print("3. Mushrooms ($0.7)")
        print("4. Finish order")

        topping_choice = input("Enter the number of your choice: ")

        if topping_choice == "1" and inventory_manager.check_and_decrement("Cheese"):
            pizza = Cheese(pizza)
        elif topping_choice == "2" and inventory_manager.check_and_decrement("Olives"):
            pizza = Olives(pizza)
        elif topping_choice == "3" and inventory_manager.check_and_decrement("Mushrooms"):
            pizza = Mushrooms(pizza)
        elif topping_choice == "4":
            break
        else:
            print("Error!")

    print("\nYour order:")
    print(f"Description: {pizza.get_description()}")
    print(f"Total cost: ${pizza.get_cost():.2f}")

    print("\nChoose payment method:")
    print("1. PayPal")
    print("2. Credit Card")

    payment_choice = input("Enter the number of your choice: ")
    if payment_choice == "1":
        PayPal().pay(pizza.get_cost())
    elif payment_choice == "2":
        CreditCard().pay(pizza.get_cost())
    else:
        print("Error!")

    print("\nRemaining Inventory:")
    print(inventory_manager.get_inventory())


if __name__ == "__main__":
    main()
