class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        return f"{self.name} издаёт звук"

    def info(self):
        return f"{self.name}, {self.age} лет, вид: {self.species}"

    def __str__(self):
        return f"Animal({self.name}, {self.age})"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Собака")
        self.breed = breed

    def speak(self):            
        return f"{self.name} говорит: Гав!"

    def fetch(self):
        return f"{self.name} принёс мяч!"

    def __str__(self):
        return f"Dog({self.name}, порода: {self.breed})"


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age, "Кошка")
        self.indoor = indoor       

    def speak(self):             
        return f"{self.name} говорит: Мяу!"

    def purr(self):
        return f"{self.name} мурлычет..."

    def __str__(self):
        return f"Cat({self.name}, домашняя: {self.indoor})"
    
class Snake(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age,"Рыба")
        self.breed = breed
    def speak(self):
        return super().speak()+" sss"
    def info(self):
        return super().info()+ "snake "+self.name
    def __str__(self):
        return f"Snake ({self.name}, brred: {self.breed})"
    