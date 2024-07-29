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