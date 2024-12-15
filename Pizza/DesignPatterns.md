## **Design Patterns in Pizza Restaurant**

### **1. Factory Pattern**

**Description**:  
The **Factory Pattern** is a creational pattern that provides a way to create objects without specifying the exact class of object that will be created.

**Before the Pattern**:  
We would directly instantiate the pizza objects in the main program, which would make the code harder to extend when adding new types of pizzas.

**After the Pattern**:  
Now, the code uses the **PizzaFactory** class to create the pizza objects. This abstraction makes the code more maintainable and extensible by allowing easy addition of new pizza types.

**Code Example**:
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type == "Margherita":
            return Margherita()
        elif pizza_type == "Pepperoni":
            return Pepperoni()
        else:
            raise ValueError("Invalid Pizza Type")

# Usage:
pizza = PizzaFactory.create_pizza("Margherita")

---

### **2. Decorator Pattern**
**Description**:
The Decorator Pattern is a structural pattern that allows for dynamic extension of object functionality. It provides an alternative to subclassing for extending functionality.

**Before the Pattern**:
We would need to subclass the pizza class every time we want to add a new topping. This would lead to a bloated class hierarchy.

**After the Pattern**:
The decorator pattern allows us to add new toppings without modifying the base pizza class or creating new subclasses. This makes the code more flexible and maintainable.

**Code Example**:
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

# Usage:
pizza = Margherita()
pizza = Cheese(pizza)  # Adds Cheese topping

---

### **3. Strategy Pattern**
**Description**:
The Strategy Pattern is a behavioral pattern that allows selecting an algorithm or behavior at runtime. It is used to define a family of algorithms and make them interchangeable.

**Before the Pattern**:
The payment logic would be tightly coupled with the rest of the order handling code, making it hard to extend or replace.

***After the Pattern**:
We can add new payment methods without modifying the existing system. Each payment method is encapsulated in a separate class that implements a common interface.

**Code Example**:
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

---

### **Overengineering in the Pizza Restaurant Project**
**Concept:**
Overengineering occurs when the complexity of a solution exceeds what is necessary to solve the problem. In the context of the pizza restaurant project, overengineering could arise from adding unnecessary abstractions, interfaces, or overly complex solutions for simple problems.

**Example of Overengineering:**
For instance, implementing separate classes for each type of pizza topping, when they could have been handled by a single class or a more straightforward solution, could be considered overengineering.

**Code Example**:
class CheeseTopping:
    def add_topping(self, pizza: Pizza):
        pizza = Cheese(pizza)
        return pizza

class OlivesTopping:
    def add_topping(self, pizza: Pizza):
        pizza = Olives(pizza)
        return pizza
