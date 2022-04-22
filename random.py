"""
I made it just for fun lol. Dont use it to cheat your homeworks.
"""

import random as rd

good_feeling = ['excited', 'happy', 'joy']
bad_feeling = ['disappointed ', 'angry', 'sad']
desc = ['hard-working', 'honest', 'professional', 'brave']
person = ['data scientist,', 'doctor,','chef,','nurse,','programmer,','musican,']
taste = ['delicious', 'sweet', 'sour', 'spicy', 'salty', 'disgusting', 'bitter', 'appetizing', 'luxury']
food = ['doughnut.', 'roasted chicken.', 'instant noodles.', 'fine dining.', 'grilled salmon.','pizza.', 'fried chicken.']
typeofthings = ['new', 'durable', 'gorgeous','expensive', 'old', 'complex']
things = ['pot,', 'watch,', 'vase,', 'marble machine,', 'game console,']

class Rightgifts:
    def generate(self):
        print('The', rd.choice(desc),rd.choice(person),'\nIs',rd.choice(good_feeling), 'to get a gift from me.\nA', rd.choice(typeofthings), rd.choice(things),'\nAnd a', rd.choice(taste), rd.choice(food), '\nMy', rd.choice(desc),rd.choice(person),'\nIs', rd.choice(bad_feeling),'to get this from me.\nMy thoughtless gift of an', rd.choice(typeofthings), rd.choice(things),'\nAnd a', rd.choice(taste), rd.choice(food))

octo = Rightgifts()
octo.generate()
