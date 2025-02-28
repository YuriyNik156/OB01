class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьет кого-то")
        self.endurance -= 6

    def wolk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"Имя воина - {self.name}")
        print(f"Цвет волос воина - {self.hair_color}")
        print(f"Сила воина - {self.power}")
        print(f"Выносливость воина - {self.endurance}")

war1 = Warrior("Степа", 76, 54, "коричневый")
war2 = Warrior("Егор", 45, 23, "блонд")

war1.sleep()
war1.eat()
war1.hit()
war1.wolk()
war1.info()

war2.sleep()
war2.eat()
war2.hit()
war2.wolk()
war2.info()