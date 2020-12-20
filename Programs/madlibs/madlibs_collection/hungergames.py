def madlib():
    adjective1 = input("Adjective: ")
    adjective2 = input("Adjective: ")
    plural_noun1 = input("Plural Noun: ")
    plural_noun2 = input("Plural Noun: ")
    plural_noun3 = input("Plural Noun: ")
    location = input("Location: ")
    noun = input("Noun: ")
    verb1 = input("Verb in present tense: ")
    verb2 = input("Verb ending in ing: ")
    verb3 = input("Verb in present tense: ")
    verb4 = input("Verb in past tense: ")
    number1 = input("Number: ")
    number2 = input("Number: ")
    food = input("Food: ")
    emotion1 = input("Emotion: ")
    emotion2 = input("Emotion: ")

    madlib = f"""The Hunger Games takes place in an {adjective1} future time period after the destruction of North America,
    in a nation known as Panem. Panem consists of a {adjective2} Capitol and twelve surrounding, poorer districts.
    District 12, where the book begins, is located in the coal-rich region that was formerly Appalachia.
    As punishment for a previous rebellion against the Capitol, every year one boy and one girl between the ages of 
    12 and 18 from each district are selected at random and forced to participate in the Hunger Games,
    a televised event in which the participants, or {plural_noun1} must fight to the death in a dangerous outdoor arena
    until only one remains. The story follows fatherless 16-year-old Katniss Everdeen, a girl from District 12
    who volunteers for the 74th Games in place of her younger sister, Primrose.
    Also participating from District 12 is Peeta Mellark, a boy whom Katniss knows from {location}
    and who once gave her {noun} when her family was starving.
    Katniss and Peeta are taken to the Capitol, where they meet the other {plural_noun1} and are publicly displayed
    to the Capitol audience. During this time, Peeta {verb1} on-air his long-time unrequited love for Katniss.
    Katniss believes this to be a ploy to gain audience support for the Games, which can be crucial for survival,
    as audience members are permitted to send gifts to favored tributes during the Games. The Games begin with
    {number1} of the {number2} {plural_noun1} dying in the first day, while Katniss relies on her well-practiced {verb2}
    and outdoor skills to survive. As the games continue, the {plural_noun1} death toll increases,
    but both Katniss and Peeta are able to {verb3} death.
    Supposedly due to Katniss and Peeta's beloved image in the minds of the audience as star-crossed lovers,
    a rule change is announced midway through the games, stating that two {plural_noun1} from the same district
    can win the Hunger Games as a pair. Upon hearing this, Katniss searches for Peeta and finds him {verb4}.
    She nurses him back to health and acts the part of a young girl falling in love to gain more favor with the audience
    and, consequently, {plural_noun2} from her sponsors. When the couple are finally the last two {plural_noun1}
    the Gamemakers suddenly reverse the rule change and try to force them into a dramatic finale
    where one must kill the other to win. Instead, they both threaten suicide by means of poisonous {food}
    in hope that the Gamemakers would rather have two winners than none.
    It works, and both Katniss and Peeta are declared winners of the 74th Hunger Games.
    Though she survives the ordeal in the arena and is treated to a hero's welcome in the Capitol, Katniss is warned
    that she has now become a political target after having defied her society's authoritarian {plural_noun3} so publicly.
    Afterwards, Peeta is {emotion1} to learn that their relationship was at least partially a calculated ploy
    to garner {emotion2} from the audience, although Katniss remains unsure of her own feelings."""

    print(madlib)


if __name__ == "__main__":
    madlib()
