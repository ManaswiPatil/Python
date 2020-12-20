def madlib():
    adjective = input("Adjective: ")
    CharacterNoun = input("Main character noun: ")
    PlaceNoun = input("Noun for a place to live: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    ItemNoun = input("Noun for a magical item: ")
    PlaceNoun2 = input("Noun for a place: ")
    feeling = input("a Feeling: ")
    AnimalNoun = input("Noun for a animal: ")
    ItemNoun2 = input("Noun for a valuable item: ")

    madlib = f""" Once upon a time there was a {adjective}{CharacterNoun}, who lived in a giant {PlaceNoun}.
 One day a {noun1} came to visit, bringing news about a {ItemNoun} in a nearby {PlaceNoun2}.
 The {CharacterNoun} was very {feeling} to hear such interesting news
 and quickly made plans to visit the {PlaceNoun2}.
 Before they arrived, a ghastly {AnimalNoun} leaped out in front of their carriage.
 The {AnimalNoun} demanded all of their {ItemNoun2}.
 It was then that a handsome {noun2} appeared as if out of nowhere and chased away the {AnimalNoun}.
 The {CharacterNoun} and the handsome {noun2} decided to throw a grand party to celebrate."""

    print(madlib)


if __name__ == '__main__':
    madlib()
