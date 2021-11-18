class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @classmethod
    def multiply_things(cls, num1, num2):
        return cls('Mike', num1 * num2)

    def speak(self):
        print(f'My name is {self._name}')

if __name__ == '__main__':
    # print(PlayerCharacter.adding_things(2,3))

    # POINT 1
    player3 = PlayerCharacter.multiply_things(3, 5)
    print(player3._age)
