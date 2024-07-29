import abc

class Plant:
    def __init__(self,name):
        self.edible=False

class Fruit(Plant):
    def __init__(self,name=''):
        super().__init__(self)
        self.edible=True
        self.name=name

class Flower(Plant):
    def __init__(self,name):
        super().__init__(self)
        self.name=name

class Animals(abc.ABC):
    def __init__(self,name=''):
        self.alive=True
        self.fed=False
        self.name=name
    def _is_alive(self):
        if self.alive:
            return 'живо'
        else:
            return 'мертво'
    def _is_fed(self):
        if self.fed:
            return 'сыто'
        else:
            return 'голодно'
    def __str__(self):
        return f'{self.name} {self._is_alive()} и {self._is_fed()}'

    @abc.abstractmethod
    def eat(self,food): pass

class Predator(Animals):
    def eat(self,food):
        if isinstance(food,Plant):
            self.fed=False
            self.alive=False
            print(f'{self.name} не стал есть {food.name} и сдох от голода!')
        if isinstance(food,Animals):
            self.fed=True
            food.alive=False
            print(f'{self.name} съел {food.name}, {food.name} умер!')
        return self

class Mammal(Animals):
    def eat(self,food):
        if isinstance(food,Plant):
            self.fed=True
            self.alive=food.edible
            print(f'{self.name} съел {food.name} и {'насытился' if food.edible else 'сдох от отравления'}')
        if isinstance(food,Animals):
            self.fed=False
            food.alive=False
            print(f'{self.name} не стал есть {food.name} и сдох от голода!')
        return self

from Animals import *
from Plant import *

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
print(a1)
print(a2)
print('-----------Оживим магией Волк с Уолл-Стрит--------------')
a1.alive=True
print('-----------И скормим ему Хатико--------------')
a1.eat(a2)
print(a1)
print(a2)