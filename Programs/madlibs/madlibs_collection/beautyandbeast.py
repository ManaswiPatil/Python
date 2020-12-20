def madlib():
    adjective1 = input("Adjective: ")
    body_part = input("Body Part: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    adjective2 = input("Adjective: ")
    adjective3 = input("Adjective: ")
    verb = input("Verb ends in s: ")
    noun3 = input("Noun for an animal: ")
    adjective4 = input("Adjective: ")
    adjective5 = input("Adjective: ")

    madlib = f"""Prince Adam was cursed to a beast form by an Enchantress who saw no love in his {adjective1}
{body_part} for others. The one way he could break the spell was to learn to love another and earn her love in return
before the last {noun1} from his enchanted {noun2} fell, which would last until his twenty-first birthday.
But who could ever learn to love a beast?
Ten years later, Maurice, a {adjective2} inventor from a {adjective3} village, becomes lost in the woods 
and seeks shelter in the Beast's castle, the Beast {verb} him for trespassing. His daughter Belle,
a bookworm who dreams of life outside her shallow village, finds him trapped in the castle
and offers her place in his stead. The Beast accepts with a promise she'll remain in the castle forever.
In the beginning Belle views him as nothing more than a {noun3}, he views her as difficult and {adjective4}.
But the two soon taste the bitter-sweetness of finding you can change and learning you were {adjective5}."""

    print(madlib)


if __name__ == "__main__":
    madlib()
