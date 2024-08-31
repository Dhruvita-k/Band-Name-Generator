import random

adjectives = ["Cosmic", "Electric", "Neon", "Thundering", "Mystic"]
nouns = ["Pandas", "Rhythms", "Waves", "Dragons", "Shadows"]

def generate_band_name():
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

if __name__ == "__main__":
    print("Welcome to the Band Name Generator!")
    print("Your band name is:", generate_band_name())
    print("Rock on!")
