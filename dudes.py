'''
A generator for a youtube chanel that casts dude-related content. There's a whole linguistic analysis to do on dudes channels, however I enjoy the joke more than I enjoy the research.
'''
import random

first = ['Dude', 'Bros', 'Extreme', 'Epic', 'Parkour', 'Riding', 'Training', 'Sport', 'Team', 'Xtreme', 'Real', 'Alpha', 'Clash']
second = ['Watch', 'Challenge', '3000', 'TV', 'Fight', 'Battle', 'Dudes', 'Mates', 'Pal', 'Zone', 'Perfect', 'Buddy']

def generate(list1, list2):
    return random.choice(list1) + ' ' + random.choice(list2)

print(generate(first, second))