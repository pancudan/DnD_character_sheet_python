import random

races = ["Dwarf", "Elf", "Orc", "Halfling", "Human", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]
classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
backgrounds = ["Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero", "Guild Artisan", "Hermit", "Noble", "Outlander", "Sage", "Sailor", "Soldier", "Urchin"]
religions = ["Forgotten Realms", "Greyhawk", "Dragonlance", "Eberron", "Ravenloft", "Planescape", "Mystara"]
def choose_option(options, message):
    print("\n".join([f"{i+1}. {option}" for i, option in enumerate(options)]))
    choice = input(message)
    while not choice.isdigit() or int(choice) not in range(1, len(options) + 1):
        print("Invalid choice. Please enter a valid number.")
        choice = input(message)
    return options[int(choice) - 1]
def generate_ability_scores():
    return {
        "Strength": random.randint(8, 18),
        "Dexterity": random.randint(8, 18),
        "Constitution": random.randint(8, 18),
        "Intelligence": random.randint(8, 18),
        "Wisdom": random.randint(8, 18),
        "Charisma": random.randint(8, 18)
    }
def generate_character():
    character = {}
    character["Race"] = choose_option(races, "Choose a race (enter the corresponding number): ")
    character["Class"] = choose_option(classes, "Choose a class (enter the corresponding number): ")
    character["Background"] = choose_option(backgrounds, "Choose a background (enter the corresponding number): ")
    character["Religion"] = choose_option(religions, "Choose a religion (enter the corresponding number): ")
    character["Name"] = input("Enter your character's name: ")
    character.update(generate_ability_scores())
    return character

def display_character_sheet(character):
    print("\nCharacter Sheet:")
    for key, value in character.items():
        print(f"{key}: {value}")
def save_character_sheet(character):
    with open("character_sheet.txt", "w") as file:
        file.write("Character Sheet:\n")
        for key, value in character.items():
            file.write(f"{key}: {value}\n")
while True:
    print("Welcome to Dungeons and Dragons Character Creation!")
    new_character = generate_character()
    display_character_sheet(new_character)
    save_character_sheet(new_character)
    print("Character sheet saved as 'character_sheet.txt'")
    create_new_character = input("Do you want to create a new character? (yes/no): ").lower()
    if create_new_character != "yes":
        break
