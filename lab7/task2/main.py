from models import Animal, Dog, Cat, Snake

generic = Animal("Безымянный", 3, "Неизвестно")
dog = Dog("Рекс", 5, "Немецкая овчарка")
cat = Cat("Мурка", 2, False)

animals = [generic, dog, cat]


print(" Все животные ")
for animal in animals:
    print(animal)           


print("\n Информация")
for animal in animals:
    print(animal.info())

print("\nПолиморфизм: speak() ")
for animal in animals:
    print(animal.speak())

print(dog.fetch())
print(cat.purr())
snake = Snake("snake1",2,"anaconda")
print(snake.speak())