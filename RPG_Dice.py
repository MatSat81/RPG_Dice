"""
    This is a class for roll role playing game dice's
"""

import random


class Dice:

    def __init__(self, number=1, dice_sides=6, modifier=0):
        """
            Creation of a die:
            number: number of dice.
            dice_face: number of faces of the dice.
            modifier: value of a bonus or maluse
            Standard dice have a number of sides of: 2, 4, 6, 8, 10, 12, 20 or 100
            but you can use other positive values.
        """

        self.number = number
        self.dice_sides = dice_sides
        self.modifier = modifier

        if self.dice_sides not in [2, 4, 6, 8, 10, 12, 20, 100]:
            print("*** Warning : number of sides of the unconventional die." +
                  " Conventional value: 2, 4, 6, 8, 10, 12, 20, 100. ***")

        if self.number < 0 or self.dice_sides < 0:
            print("*** WARNING : The number of dice and the number of sides of the dice must be positive. ***")
            self.number = abs(self.number)
            self.dice_sides = abs(self.dice_sides)

        if type(self.number) is not int or type(self.dice_sides) is not int:
            print("*** WARNING : The number of dice and the number of sides of the dice must be int. ***")
            self.number = round(self.number)
            self.dice_sides = round(self.dice_sides)

    def roll(self):
        """
            Roll the dice.
            You can use this method to make a comparison in a test.
        """

        result = random.randint(self.number, self.number * self.dice_sides) + self.modifier
        return result

    def info(self):
        """
             Returns info about the die.
             You can use this method in a print () to display the info in the console.
        """

        if self.modifier > 0:
            return "Dice : {} : random number between {} and {} for example {}" \
                .format(self.__repr__(), self.number + self.modifier,
                        self.number * self.dice_sides + self.modifier, self.roll())
        elif self.modifier == 0:
            return "Dice : {} : random number between {} and {} for example {}" \
                .format(self.__repr__(), self.number + self.modifier,
                        self.number * self.dice_sides, self.roll())
        elif self.modifier < 0:
            return "Dice : {} : random number between {} and {} for example {}" \
                .format(self.__repr__(), self.number + self.modifier,
                        self.number * self.dice_sides + self.modifier, self.roll())

    def __repr__(self):
        """
            Return string information about the die.
             You can use this method to display the characteristics of the die in the console.
        """
        if self.modifier > 0:
            return "{}D{}+{}".format(self.number, self.dice_sides, self.modifier)
        elif self.modifier == 0:
            return "{}D{}".format(self.number, self.dice_sides)
        elif self.modifier < 0:
            return "{}D{}{}".format(self.number, self.dice_sides, self.modifier)


def main():
    dice_list = [[1, 6, 0],
                 [2, 8, 5],
                 [1, 20, -2],
                 [3, 3, 0],
                 [-5, 4, 0],
                 [2, -10, 5],
                 [1.8, 6.2, 0]]
    for dice_test in dice_list:
        dice = Dice(dice_test[0], dice_test[1], dice_test[2])
        print(dice.info())
        print(dice)
        for i in range(5):
            print(dice.roll())


if __name__ == "__main__":
    main()
