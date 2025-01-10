import colorama

# Переглянути всі атрибути та методи
print(dir(colorama))

# Отримати допомогу по конкретному атрибуту або методу
help(colorama)

from colorama import init
init()  # Ініціалізація для коректної роботи кольорів

from colorama import Fore
print(Fore.RED + 'Цей текст червоний')

from colorama import Back
print(Back.GREEN + 'Цей текст має зелене тло')