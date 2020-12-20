import random

color = random.choice(["Gold", "Silver", "Green", "Blue", "Red"])

print(''' Guess the color from following:
1. Gold
2. Silver
3. Green
4. Blue
5. Red''')

again = True

while again:
    guess = input("Guess the color: ")
    if guess == color:
        print("Well Done!")
        again = False
    else:
        if color == "Gold":
            print('''Lets try again:
Some people bite into it
But it is not a carrot
It is a precious metal
That’s pure 24 karat.''')
        elif color == "Silver":
            print('''Lets try again:
These are the color of bells
In a famous Christmas song
It’s said clouds have this lining
Even when something is wrong''')
        elif color == "Green":
            print('''Lets try again:
Certain types of peppers
Some asparagus and peas
Lettuce, spinach and limes
What’s the color of all these?''')
        elif color == "Blue":
            print('''Lets try again:
Violet, yellow, orange
Red, green and indigo
What’s the missing color
That is in a rainbow.''')
        elif color == "Red":
            print('''Lets try again:
When you’re driving in a car
This color is on top
Of a set of traffic lights
It means that you should stop.''')
