# Current version (2021)
from random import choice

adjectives = ["wet", "big"]
nouns = ["turnip", "dog"]
insult = choice(adjectives + nouns)

print(f"You are a {insult}")
