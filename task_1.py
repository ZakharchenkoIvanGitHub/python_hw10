class Fabric:

    def __init__(self, an_t, kind, name, age, spec):
        self.an_t = an_t
        self._kind = kind
        self._name = name
        self._age = age
        self._spec = spec

    def get_an(self):
        dct = {"рыба": Fishes,
               "птица": Birds,
               "млекопитающий ": Mammals,
               }
        return dct[self.an_t](self._kind, self._name, self._age, self._spec)


class Animal():
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1


class Fishes(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size


class Birds(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color


class Mammals(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec


f1 = Fabric('рыба', 'Карась', 'Федя', 1, 15).get_an()


print(f'Вид: {f1.get_kind()}')
print(f'кличка: {f1.get_name()}')
print(f'возраст: {f1.get_age()} лет')
print(f'размер: {f1.get_specific()} см.')
