# # №1
#
# class Pizza:
#     def __init__(self, dough, sauce, toppings):
#         self.dough = dough
#         self.sauce = sauce
#         self.toppings = toppings
#
#     def prepare(self):
#         print("Готовим пиццу...")
#         # код для приготовления пиццы
#
#     def bake(self):
#         print("Выпекаем пиццу...")
#         # код для выпекания пиццы
#
#     def cut(self):
#         print("Разрезаем пиццу...")
#         # код для нарезки пиццы
#
#     def package(self):
#         print("Упаковываем пиццу...")
#         # код для упаковки пиццы
#
#
# class Order:
#     def __init__(self):
#         self.pizzas = []
#
#     def add_pizza(self, pizza):
#         self.pizzas.append(pizza)
#
#     def calculate_total(self):
#         total = 0
#         for pizza in self.pizzas:
#             total += pizza.price
#         return total
#
#
# class Terminal:
#     def __init__(self):
#         self.menu = {
#             1: Pizza("Pepperoni Dough", "Pepperoni Sauce", ["pepperoni"]),
#             2: Pizza("Barbecue Dough", "Barbecue Sauce", ["bacon", "onions", "pineapple"]),
#             3: Pizza("Seafood Dough", "Seafood Sauce", ["shrimp", "calamari", "mussels"])
#         }
#
#     def display_menu(self):
#         print("MENU:")
#         for index, pizza in self.menu.items():
#             print(f"{index}. {pizza.dough} {pizza.sauce} {pizza.toppings}")
#
#     def create_order(self):
#         order = Order()
#         while True:
#             self.display_menu()
#             selected_pizza = int(input("Выберите пиццу из меню (введите число): "))
#             order.add_pizza(self.menu[selected_pizza])
#
#             more_pizzas = input("Хотите добавить еще пиццы в свой заказ? (да/нет): ")
#             if more_pizzas.lower() != "да":
#                 break
#
#         print("Заказ подтвержден!")
#         total = order.calculate_total()
#         print(f"Общая сумма: {total} USD")
#
#         payment = float(input("Введите сумму платежа: "))
#         if payment >= total:
#             print("Оплата получена. Спасибо!")
#             order.process()
#         else:
#             print("Недостаточная оплата. Заказ отменен.")
#
#
# terminal = Terminal()
# terminal.create_order()

# # №2
#
# import random
#
# def get_user_choice():
#     while True:
#         choice = input("Выберите бумагу, камень или ножницы: ")
#         if choice.lower() in ['камень', 'ножницы', 'бумага']:
#             return choice.lower()
#         else:
#             print("Неверный выбор. Попробуйте еще раз.")
#
# def get_computer_choice():
#     choices = ['камень', 'ножницы', 'бумага']
#     return random.choice(choices)
#
# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "Одинаково"
#     elif user_choice == 'камень' and computer_choice == 'ножницы':
#         return "Красавчик!"
#     elif user_choice == 'ножницы' and computer_choice == 'бумага':
#         return "Красавчик!"
#     elif user_choice == 'бумага' and computer_choice == 'камень':
#         return "Красавчик!"
#     else:
#         return "Плохо."
#
# def play_again():
#     while True:
#         choice = input("Хотите сыграть еще раз? (да/нет): ")
#         if choice.lower() == 'да':
#             return True
#         elif choice.lower() == 'нет':
#             return False
#         else:
#             print("Неверный выбор. Попробуйте еще раз.")
#
# def main():
#     print("Добро пожаловать в игру камень, ножницы, бумага!")
#     while True:
#         user_choice = get_user_choice()
#         computer_choice = get_computer_choice()
#         print(f"Вы выбрали {user_choice}, компьютер выбрал {computer_choice}.")
#         print(determine_winner(user_choice, computer_choice))
#         if not play_again():
#             break
#     print("Спасибо за игру!")
#
# if __name__ == '__main__':
#     main()

# # №3
#
# import random
#
# def get_word():
#     words = ['python', 'java', 'javascript', 'ruby', 'php', 'html', 'css']
#     return random.choice(words)
#
# def play_again():
#     while True:
#         choice = input("Хотите сыграть еще раз? (да/нет): ")
#         if choice.lower() == 'да':
#             return True
#         elif choice.lower() == 'нет':
#             return False
#         else:
#             print("Неверный выбор. Попробуйте еще раз.")
#
# def main():
#     print("Добро пожаловать в игру Виселица!")
#     while True:
#         word = get_word()
#         guessed_letters = set()
#         tries = 6
#         while tries > 0:
#             print(f"У вас {tries} попыток.")
#             for letter in word:
#                 if letter in guessed_letters:
#                     print(letter, end=' ')
#                 else:
#                     print('_', end=' ')
#             print()
#             guess = input("Введите букву: ")
#             if guess in guessed_letters:
#                 print("Вы уже вводили эту букву. Давай еще.")
#             elif guess in word:
#                 guessed_letters.add(guess)
#                 if set(word) == guessed_letters:
#                     print(f"Вы угадали слово '{word}'! Красавчик!")
#                     break
#             else:
#                 tries -= 1
#                 print("Такой буквы в слове нет.")
#         else:
#             print(f"Вы проиграли. Загаданное слово было '{word}'.")
#         if not play_again():
#             break
#     print("Спасибо за игру!")
#
# if __name__ == '__main__':
#     main()

# # №4
#
# import random
#
# def play_again():
#     while True:
#         choice = input("Хотите сыграть еще раз? (да/нет): ")
#         if choice.lower() == 'да':
#             return True
#         elif choice.lower() == 'нет':
#             return False
#         else:
#             print("Неверный выбор. Попробуйте еще раз.")
#
# def main():
#     print("Добро пожаловать в игру Угадай число! надо загадать с 1 до 100")
#     while True:
#         number = random.randint(1, 100)
#         tries = 10
#         print(f"У вас {tries} попыток.")
#         while tries > 0:
#             guess = int(input("Введите число от 1 до 100: "))
#             if guess == number:
#                 print(f"Вы угадали число '{number}'! Кроасавчик!")
#                 break
#             elif guess < number:
#                 print("Загаданное число больше.")
#             else:
#                 print("Загаданное число меньше.")
#             tries -= 1
#             if tries > 0:
#                 print(f"Осталось {tries} попыток.")
#         else:
#             print(f"Вы проиграли. Загаданное число было '{number}'.")
#         if not play_again():
#             break
#     print("Респект бро!")
#
# if __name__ == '__main__':
#     main()