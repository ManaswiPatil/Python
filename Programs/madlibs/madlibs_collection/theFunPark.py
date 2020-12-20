def madlib():
    adjective1 = input("Adjective: ")
    adjective2 = input("Adjective: ")
    adjective3 = input("Adjective: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    adverb1 = input("Adverb: ")
    adverb2 = input("Adverb: ")
    number = input("Number: ")
    pasttenseverb1 = input("Past tense verb: ")
    pasttenseverb2 = input("Past tense verb: ")

    madlib = f"""Today, my fabulous camp group went to a (an){adjective1} amusement park. 
It was a fun park with lots of cool {noun1} and enjoyable play structures. When we got there, my 
kind counselor shouted loudly, 'Everybody off the {noun2}.' We all pushed out in a terrible 
hurry. My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn't figure out 
what exciting thing to do first. I saw a scary roller coaster I really liked so, I {adverb1} ran 
over to get in the long line that had about {number} people in it. When I finally 
got on the roller coaster I was {pasttenseverb1}. In fact I was so nervous my two knees were knocking together. 
This was the {adjective2} ride I had ever been on! In about two minutes I heard the crank and grinding of the gears. 
That’s when the ride began! When I got to the bottom, I was a little {pasttenseverb2} but I was proud of myself. 
The rest of the day went {adverb2}. 
It was a(n) {adjective3} day at the fun park."""

    print(madlib)


if __name__ == '__main__':
    madlib()
