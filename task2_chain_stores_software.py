# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности,
# но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача —
# создать класс Store, который можно будет использовать для создания различных магазинов.
# Шаги:
# 1. Создай класс Store:
# -Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
# -  метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.

class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_new_product(self):
        product = input("Введите название товара: ")
        try:
            price = float(input("Введите цену товара: "))
            self.items[product] = price
            print(f"Товар {product} добавлен по цене {price}")
        except ValueError:
            print("Введите число в цену товара. ")

    def delete_product(self):
        if not self.items:
            print("Нет товаров для удаления!")
            return

        product = input("Введите название товара, который нужно удалить: ")
        if product in self.items:
            del self.items[product]
            print(f"Товар {product} удален!")
        else:
            print("Такого товара нет в ассортименте.")

    def get_price(self):
        product = input("Введите название товара для получения его цены: ")
        price = self.items.get(product)
        if price is not None:
            print(f"Цена товара {product}: {price}")
        else:
            print("Такого товара нет в магазине.")

    def update_price(self):
        product = input("Введите название товара для обновления цены: ")
        if product in self.items:
            try:
                new_price = float(input("Введите новую цену товара: "))
                self.items[product] = new_price
                print(f"Цена товара {product} обновлена до {new_price}!")
            except ValueError:
                print("Ошибка! Цена должна быть числом.")
        else:
            print("Такого товара нет в магазине.")

    def show_products(self):
        if not self.items:
            print("Магазин пуст! Нет товаров в ассортименте.")
        else:
            print("Ассортимент магазина:")
            for product, price in self.items.items():
                print(f"{product}: {price}")

pyaterochka = Store("Пятерочка", "проспект Ленина, 10")
smart = Store("Смарт", "Казанское шоссе, 17а")
fix_price = Store("Fix price", "ул. Плотникова, 3")
svetofor = Store("Светофор", "проспект Гагарина, 19")

stores = {
    "1": pyaterochka,
    "2": smart,
    "3": fix_price,
    "4": svetofor
    }

while True:

    print("Выберите магазин: ")
    for key, store in stores.items():
        print(f"{key} - {store.name}; {store.address}")
    print("5 - Выход")

    choice_store = input("Введите номер магазина: ")

    if choice_store == "5":
        print("Выход из программы.")
        break
    elif choice_store in stores:
        store = stores[choice_store]
        print(f"Вы выбрали магазин: {store.name}")

    print("Выберите действие:")
    print("1 - Добавить товар")
    print("2 - Удалить товар")
    print("3 - Получить цену товара")
    print("4 - Обновить цену товара")
    print("5 - Показать ассортимент")
    print("6 - Вернуться в меню выбора магазина")

    choice = input("Введите номер действия: ")

    if choice == "1":
        store.add_new_product()
    elif choice == "2":
        store.delete_product()
    elif choice == "3":
        store.get_price()
    elif choice == "4":
        store.update_price()
    elif choice == "5":
        store.show_products()
    elif choice == "6":
        print("Выход из программы.")
        break
    else:
        print("Некорректный ввод! Попробуйте снова.")