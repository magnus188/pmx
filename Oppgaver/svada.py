import random

# create arrays of words
pronomen = ['jeg', 'du', 'hun', 'han', 'vi', 'dere', 'de']
verb = ['hopper', 'svømmer', 'spiser', 'løper', 'roper']
adverb = ['høyt', 'langt', 'raskt', 'fort']

#print sentence with random words from arrays
print(random.choice(pronomen), random.choice(verb), random.choice(adverb))
