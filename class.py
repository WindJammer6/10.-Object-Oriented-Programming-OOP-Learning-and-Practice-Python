class Car():
    def __init__(self, speed, color):
        print(speed)
        print(color)
        self.speed = speed
        self.color = color
        print("the __init__ is called")

ford = Car(200, 'red')
hond = Car(250, 'blue')
audi = Car(300, 'black')

print(ford.speed)
print(ford.color)

