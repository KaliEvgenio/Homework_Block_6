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
print('-----------Оживим магией Вол с Уолл-Стрит--------------')
a1.alive=True
print('-----------И скормим ему Хатико--------------')
a1.eat(a2)
print(a1)
print(a2)