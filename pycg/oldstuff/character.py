#!/usr/bin/python3.6


class Character:
    abilities_order = ['str', 'dex', 'con', 'int', 'wis', 'cha']
    abilities_fullname = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    stat_skills = {'strength': ['athletics'],
                   'dexterity': ['acrobatics', 'sleight of hand', 'stealth'],
                   'intelligence': ['arcana', 'history', 'investigation', 'nature', 'religion'],
                   'wisdom': ['animal handling', 'insight', 'medicine', 'perception', 'survival'],
                   'charisma': ['deception', 'intimidation', 'performance', 'persuasion']}
    starting_level = 1
    character_classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter',
                         'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer',
                         'Warlock', 'Wizard']

    def calculate_ability_mods(self, abilities):
        mods = {}
        for k, v in abilities.items():
            mods[k] = int((v-10)/2)
        return mods

    def set_ability(ability, num):
        pass

    def __init__(self):
        self.name = None
        self.player = None
        self.level = 1
        self.abilities = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0}
        self.ability_mods = self.calculate_ability_mods(self.abilities)
        self.skills = {}
        self.height = 0
        self.weight = 0
        self.equipment = {}
        self.background = None
        self.description = None
        self.character_class = None
        self.character_likeness = None

    def skills(self):
        pass

    def equipment(self):
        pass

    def background(self):
        pass

    def description(self):
        pass
