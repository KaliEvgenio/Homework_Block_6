class Vehicle:
    __COLOR_VARIANTS=['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, model, color, eng_pow):
        self.owner = owner
        self._model = model
        self._engine_power = eng_pow
        if color.casefold() in self.__COLOR_VARIANTS:
            self._color = color.casefold()
        else:
            self._color = self.__COLOR_VARIANTS[0]
    def get_model(self):
        return f'Модель: {self._model} '
    def set_model(self,value):
        self._model = str(value)
        return self
    def get_horsepower(self):
        return f'Мощность двигателя: {self._engine_power} '
    def set_horsepower(self,value):
        self._engine_power = int(value)
        return self
    def get_color(self):
        return f'Цвет: {self._color} '
    def set_color(self,value):
        if type(value) == str and value.casefold() in self.__COLOR_VARIANTS:
            self._color = value.casefold()
        elif type(value) == int and value <= len(self.__COLOR_VARIANTS):
            self._color = self.__COLOR_VARIANTS[value]
        else:
            print(f'Нельзя сменить цвет на {value}')
        return self
    def print_info(self):
        print(self.get_model()+self.get_horsepower()+self.get_color()+f'Владелец: {self.owner}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT=5
    def __init__(self, owner, model, color, eng_pow):
        super().__init__(owner, model, color, eng_pow)
        self._passenger=0
    def add_passengers(self,value=1):
        if self._passenger+value <= self.__PASSENGERS_LIMIT:
            self._passenger+=value

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

vehicle1.set_color(2)
vehicle1.print_info()