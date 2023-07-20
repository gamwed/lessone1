# class Student:
#     """
#     Describe clss Student.
#     """
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#     def __str__(self):
#         return f'{self.surname} {self.name[0]}'
#
# class Group:
#     def __int__(self, title):
#         self.title = title
#         self.student = []
#     def add_student(self, student, Student):
#
#     def __str__(self):
#         res = ""
#         for student in self.student:
#             res += f'{student}\n'
#         return  res
#
# st_1 = Student('Sasha', 'Myronenko')
# st_2 = Student('Masha', 'Romanenko')


# class Student:
#
#     """
#     Describes class Student.
#     """
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f'{self.surname} {self.name}'
#
#
# class Group:
#
#     def __init__(self, title, max_students=10):
#         self.title = title
#         self.__students = set()
#         self.max_students = max_students
#
#     def add_student(self, student: Student):
#         if isinstance(student, Student) and len(self.__students) < self.max_students:
#             self.__students.add(student)
#
#     def __str__(self):
#         res = ''
#         for student in self.__students:
#             res += f'{student}\n'
#         return res
#
#
# st_1 = Student('Oleh', 'Tymchuk')
# st_2 = Student('Ivan', 'Ivanov')
# group = Group('Python PRO')
# group.add_student(st_1)
# group.add_student(st_2)
# print(group)

# Task 1

# class Product:
#
#     """"
#     Продукт
#     """
#
#     def __init__(self, name, price, description):
#         self.name = name
#         self.price = price
#         self.description = description
#
#     def __str__(self):
#         return f"{self.name} - ${self.price:.2f}\nDescription: {self.description}\n"
#
#
# class Cart:
#
#     """"
#     Корзина
#     """
#
#     def __init__(self):
#         self.products = {}
#
#     def add_product(self, product, quantity=1):
#         if product in self.products:
#             self.products[product] += quantity
#         else:
#             self.products[product] = quantity
#
#     def remove_product(self, product, quantity=1):
#         if product in self.products:
#             self.products[product] -= quantity
#             if self.products[product] <= 0:
#                 del self.products[product]
#
#     def calculate_total(self):
#         total_cost = 0
#         for product, quantity in self.products.items():
#             total_cost += product.price * quantity
#         return total_cost
#
#     def __str__(self):
#         if not self.products:
#             return "Cart is empty."
#         cart_info = "Cart:\n"
#         for product, quantity in self.products.items():
#             cart_info += f"{product.name} - ${product.price:.2f} x {quantity}\n"
#         cart_info += f"Total: ${self.calculate_total():.2f}"
#         return cart_info
#
#
# # Создание нескольких экземпляров класса Product
#
# apple = Product("Apple", 0.99, "Fresh and juicy apples")
# bread = Product("Bread", 2.49, "Whole grain bread")
# milk = Product("Milk", 1.99, "Fresh cow milk")
#
# # Создание экземпляра класса Cart
# cart = Cart()
#
# # Добавление продуктов в корзину
# cart.add_product(apple, 5)
# cart.add_product(bread, 2)
# cart.add_product(milk, 3)
#
# # Удаление продукта из корзины
# cart.remove_product(bread, 1)
#
# # Вывод информации о корзине
# print(cart)

# Task 2
class Meal:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price:.2f} UAH\nDescription: {self.description}\n"


class Category:
    def __init__(self, name):
        self.name = name
        self.meals = []

    def add_meal(self, meal):
        self.meals.append(meal)

    def __str__(self):
        category_info = f"{self.name}:\n"
        for meal in self.meals:
            category_info += str(meal)
        return category_info


class Menu:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def __str__(self):
        menu_info = "Restaurant Menu:\n"
        for category in self.categories:
            menu_info += str(category)
        return menu_info


class Order:
    def __init__(self):
        self.meals = []
        self.total_price = 0

    def add_meal(self, meal):
        self.meals.append(meal)
        self.total_price += meal.price

    def __str__(self):
        order_info = "Order:\n"
        for meal in self.meals:
            order_info += f"{meal.name} - {meal.price:.2f} UAH\n"
        order_info += f"Total: {self.total_price:.2f} UAH"
        return order_info


meal1 = Meal("Spaghetti", "Classic Italian pasta", 12.99)
meal2 = Meal("Salad", "Fresh mixed greens with dressing", 8.49)
meal3 = Meal("Cake", "Decadent chocolate cake", 6.99)

category1 = Category("Main Courses")
category1.add_meal(meal1)
category1.add_meal(meal2)

category2 = Category("Desserts")
category2.add_meal(meal3)

menu = Menu()
menu.add_category(category1)
menu.add_category(category2)

print(menu)

order = Order()
order.add_meal(meal1)
order.add_meal(meal3)

print(order)