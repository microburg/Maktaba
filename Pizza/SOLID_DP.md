## **SOLID Principles and Design Patterns in Pizza Restaurant**

### **1. Factory Pattern**

**SOLID Principle Addressed:**
- **Single Responsibility Principle (SRP)**  
    The **PizzaFactory** class has the sole responsibility of creating pizza objects. It is responsible only for the creation process and doesn’t handle the pizza's logic.

**How the Factory Pattern Helps Implement the SOLID Principles:**
- It also adheres to the **Single Responsibility Principle** because the class is responsible solely for pizza creation, without taking on other tasks like payment or inventory management.

**Example Code:**
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type == "Margherita":
            return Margherita()
        elif pizza_type == "Pepperoni":
            return Pepperoni()
        else:
            raise ValueError("Invalid Pizza Type")

---

### **2. Decorator Pattern**
**SOLID Principle Addressed:**

**Liskov Substitution Principle (LSP)**
The **ToppingDecorator** and its subclasses can be substituted for the base pizza class without altering the expected behavior. Each topping is an extension of the pizza class, and the pizza’s functionality remains intact regardless of the toppings.

**How the Decorator Pattern Helps Implement the SOLID Principles:**
-Liskov Substitution Principle is followed because any topping class can be substituted for a base pizza class without affecting the overall functionality of the system.

**Example Code:**
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

---

### **3. Strategy Pattern (Payment Methods)**
**SOLID Principle Addressed:**

**Open/Closed Principle (OCP)**
The Strategy Pattern allows us to introduce new payment methods without modifying the existing codebase. This means we can add payment methods by creating new strategy classes, keeping the existing system intact.

**How the Strategy Pattern Helps Implement the SOLID Principles:**

-Open/Closed Principle is adhered to because new payment methods can be added by introducing new strategy classes without altering existing code.

**Example Code:**
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
