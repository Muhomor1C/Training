class Zebra:
    register = {}
    count_foot = 4

    def __init__(self, zebra_name, speed, weight):
        self.__name__ = zebra_name
        self.speed = speed
        self.weight = weight
        self.direction = ""
        self.count_eat = 0

    def eat(self, count_eat):
        self.count_eat = count_eat

    def run(self, direction=""):
        if self.count_eat > 0:
            print("Я сыта", end="")
            self.direction = direction
            if self.direction != "":
                print(f" и бегу на {self.direction}")
                self.count_eat -= 1
            else:
                print("Куда бежать?")
        else:
            print("Сперва меня надо покормить!")

    def about(self):
        print(
            f"Я {self.__name__}, у меня {self.count_foot} ноги. Имею {self.count_eat} кг. зерна."
            f" Максимальная скорость {self.speed} км/ч,"
            f" вес {self.weight} кг.")


def zebra_factory(zebra_name, speed, weight):
    zebra = Zebra(zebra_name, speed, weight)
    Zebra.register[zebra_name] = zebra


zebra_factory("Маша", 30, 50)
zebra_factory("Дуня", 25, 30)
zebra_factory("Коля", 50, 60)


