class Animal:                                                 # Класс животное
    alive = True                                    # живой
    fed = False                                     # накормленный
    def __init__(self, name):
        self.name = name                            #(индивидуальное название каждого животного)

    def eat(self, food):                                      # Метод еды
        if food.edible:                                       # Если еда съедобная
            print(f'{self.name} съел {food.name}')
            self.fed = True                                   # Млекопитающее стало есть
        else:                                                 # Если нет еды
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False                                # Млекопитающее умерло


class Plant:                                 # Класс Растение
    edible = False
    def __init__(self, name):                # (съедобность)
        self.name = name                     # (индивидуальное название каждого растения)


class Mammal(Animal):                       # Класс Млекопитающее
    pass

class Predator(Animal):                     # Класс хищников
    pass

class Flower(Plant):                        # Класс Растение цветок
    pass

class Fruit(Plant):                         # Класс Растение фрукт
    edible = True

    def __init__(self, name):
        super().__init__(name)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


