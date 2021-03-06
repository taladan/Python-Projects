#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
kenku name generator, based on fantasynamegenerators.com generator code.

Author: Taladan
Last Edited: December 13, 2017
"""
import random

nm1 = ["Angler", "Baker", "Barker", "Basher", "Bather", "Beggar", "Biter",
       "Boiler", "Bomber", "Bonker", "Bounce r", "Braker", "Brander", "Breaker",
       "Broiler", "Bruiser", "Bubbler", "Burner", "Butcher", "Buzzer", "Cackler",
       "Carver", "Caster", "Chimer", " Chitter", "Chomper", "Chopper", "Clamor",
       "Clamper", "Clanger", "Clapper", "Clawer", "Cleaver", "Clicker",
       "Clinger", "Clinker", "Clipper", " Clubber", "Clucker", "Cobbler",
       "Cooker", "Cougher", "Crackler", "Crinkler", "Croaker", "Cruncher",
       "Crusher", "Cutter", "Dangler", "Deflater", "Digger", "Dipper", "Doodler",
       "Dragger", "Drawer", "Dribbler", "Driller", "Dripper", "Drummer",
       "Duster", "Enchanter", "Engraver", "Etch er", "Exploder", "Flapper",
       "Flipper", "Flopper", "Flusher", "Forger", "Fryer", "Giggler", "Gnasher",
       "Gnawer", "Gouger", "Greaser", "Griller ", "Grinder", "Growler", "Gusher",
       "Hammer", "Hammerer", "Hiccup", "Hummer", "Impaler", "Inscriber",
       "Itcher", "Jangler", "Jingler", "Knocker", "Lasher", "Locker", "Lugger",
       "Mangler", "Masher", "Mauler", "Mewer", "Mimer", "Molder", "Nailer",
       "Neigher", "Nestler", "Nibbler", "Paddler", "Piercer", "Piper", "Plunger",
       "Presser", "Prodder", "Puffer", "Raker", "Rasper", "Rattler", "Ripper",
       "Roarer", "Roaster", "Ruffler", "Rustler", "Scooper", "Scorcher",
       "Scratcher", "Scribbler", "Scrubber", "Shaker", "Shaver", "Shearer",
       "Shoveler", "Shrieker", "Sifter", "Singe r", "Sketcher", "Slammer",
       "Slicer", "Smasher", "Snapper", "Sneezer", "Snorer", "Spitter",
       "Splasher", "Splitter", "Squeaker", "Squealer", "S quisher", "Stamper",
       "Stomper", "Strangler", "Striker", "Strummer", "Swatter", "Sweeper",
       "Swiper", "Tinkerer", "Trampler", "Walloper", "Wha cker", "Whipper",
       "Whistler"]

nm2 = ["Albatross Call", "Albatross Flap", "Alligator Hiss", "Alligator Roar",
       "Ape Call", "Ape Hoo t", "Ape Scratch", "Aper", "Badger Growl",
       "Badger Run", "Badger Scratch", "Barker", "Bat Flap", "Bat Screech",
       "Bat Swoop", "Bear Growl", "Bear Roar", "Bear Rustle", "Bear Step",
       "Bear Stomp", "Beaver Call", "Beaver Chew", "Beaver Nibble",
       "Beaver Rustle", "Bee Buzzer", "Bis on Breath", "Bison Call",
       "Bison Stomp", "Bleater", "Boar Charge", "Boar Grunt", "Boar Rustle",
       "Boar Squeal", "Boar Stamp", "Boarer", "Ca ckler", "Cat Call", "Cat Hiss",
       "Cat Purr", "Cat Rustle", "Cat Scratch", "Catter", "Chirper", "Cow Moo",
       "Cow Step", "Cow Stomp", "Cower", " Coyote Cackle", "Coyote Howl",
       "Coyote Yelp", "Coyote Yowl", "Cricket Chirp", "Cricketer", "Croaker",
       "Crocodile Hiss", "Crocodile Roar", "Crocodiler", "Crow Call",
       "Crow Rustle", "Crower", "Deer Clash", "Deer Rustle", "Deer Scratch",
       "Deer Stomp", "Dino Chew", "Dino Growl", "Dino Roar", "Dino Snort",
       "Dino Stomp", "Dog Bark", "Dog Growl", "Dog Howl", "Dog Run",
       "Dog Sneeze", "Dog Step", "Dog Wiggle", "Dog Yelp", "Dog Yip", "Dog Yowl",
       "Dogger", "Donkey Call", "Donkey Stomp", "Dove Rustle", "Dove Swoop",
       "Dover", "Dragon Bite", "Dragon Breath", " Dragon Chew", "Dragon Roar",
       "Dragon Swoop", "Duck Quacker", "Duck Rustle", "Ducker", "Eagle Screech",
       "Elephant Roar", "Elephant Stampe de", "Elephant Stomp", "Falcon Rustle",
       "Falcon Swoop", "Fox Rustle", "Fox Yelp", "Fox Yowl", "Foxer",
       "Frog Croak", "Frog Splash", "Frogg er", "Gecko Croak", "Giraffe Smash",
       "Giraffe Snort", "Giraffe Stomp", "Goat Baa", "Goat Bleat", "Goat Chew",
       "Goater", "Goose Hiss", "Goo se Honk", "Growler", "Hamster Squeak",
       "Hee-Haw", "Hisser", "Hog Oink", "Hog Snort", "Honker", "Hooter",
       "Horse Blow", "Horse Neigh", "Hors e Sneeze", "Horse Snort",
       "Horse Stamp", "Horse Whinny", "Horser", "Howler", "Hyena Cackle",
       "Hyena Laugh", "Jackal Call", "Jackal Laugh", "Jackal Rustle",
       "Lion Growl", "Lion Roar", "Monker", "Monkey Howl", "Monkey Rustle",
       "Monkey Scream", "Mouse Peep", "Mouse Rustle", "Mo use Squeak", "Mouser",
       "Nightingale Song", "Nightingaler", "Oinker", "Owl Call", "Owl Hoot",
       "Owl Rustle", "Owl Swoop", "Owler", "Panda Sn eeze", "Panther Growl",
       "Panther Roar", "Parrot", "Parrot Bite", "Parrot Call", "Parrot Nibble",
       "Parrot Rustle", "Parrot Squawk", "Parro ter", "Pheasant Call",
       "Pheasant Rustle", "Pig Snort", "Pigeon Coo", "Pigeon Rustle", "Pigeoner",
       "Quacker", "Quail Call", "Quail Rustle", "Quailer", "Rabbit Scream",
       "Rabbit Yelp", "Ram Ram", "Ram Stamp", "Rammer", "Rat", "Rat Rustle",
       "Rat Squeak", "Rat Yelp", "Ratter", "Rav en Rustle", "Rhino Snort",
       "Rhino Stamp", "Rook Rustle", "Rooker", "Screamer", "Screecher",
       "Seal Bark", "Seal Flop", "Sealer", "Sheep Baa ", "Sheep Bleat", "Singer",
       "Snake Hiss", "Snake Rattle", "Snake Slither", "Snaker", "Snorter",
       "Squawker", "Squeaker", "Squirrel Chatter", "Squirrel Chitter",
       "Squirrel Nibble", "Squirrel Rustle", "Squirreler", "Stampede",
       "Swan Cry", "Swan Flap", "Swan Hiss", "Swan Honk", " Swanner",
       "Toad Croak", "Trumpet", "Trumpeter", "Turkey Call", "Turkey Gobble",
       "Tweeter", "Vulture Scream", "Warbler", "Whale Song", "Wol f Growl",
       "Wolf Howl", "Wolf Yelp", "Wolfer", "Wolverine Growl", "Wolverine Yelp"]

nm3 = ["Net Cast", "Net Splash", "Anchor Splas h", "Anchor Chain", "Anchor Drop",
       "Leather Smack", "Leather Flick", "Leather Drop", "Hide Smack",
       "Hide Flick", "Hide Drop", "Paint Drop ", "Paint Stroke", "Paint Squeeze",
       "Brush Stroke", "Brush Flick", "Hammer Crash", "Hammer Drop",
       "Hammer Clank", "Nail Drop", "Nail Ting le", "Saw Drop", "Saw Wobble",
       "Saw Pull", "Spade Dig", "Spade Drop", "Hoe Dig", "Hoe Scrape",
       "Hoe Scratch", "Mallet Crash", "Mallet Smas h", "Mallet Drop",
       "Chisel Tick", "Chisel Cut", "Chisel Carve", "Armor Clank", "Armor Crash",
       "Steel Clank", "Steel Crash", "Steel Drop", "Furnace Roar",
       "Furnace Door", "Hatchet Cut", "Hatchet Drop", "Hatchet Split",
       "Hatchet Chop", "Wood Chop", "Wood Crack", "Wood Creak", "Wood Drop",
       "Tree Fall", "Tree Creak", "Fire Crackle", "Fire Roar", "Potion Bubble",
       "Potion Crash", "Potion Gush", "Potion Swirl", "Pot ion Splash",
       "Kettle Bubble", "Kettle Splash", "Kettle Bubble", "Cauldron Swirl",
       "Cauldron Stir", "Cauldron Bubble", "Cauldron Splash", "Bell Ring",
       "Bell Drop", "Crier Bell", "Bowstring Flick", "Bowstring Stretch",
       "Blacksmith Clank", "Lute Pluck", "Lute String", "Glass  Shatter",
       "Fruit Squish", "Crate Smash", "Crate Crack", "Crate Creak", "Ship Creak",
       "Sail Slap", "Rope Slap", "Rope Whip", "Book Drop", "Book Slam",
       "Page Turn", "Grain Trash", "Grain Mill", "Cork Pop", "Wood Scrape",
       "Sail Flick"]

def nameGen():


    for i in range(11):
        if i < 4:
            rnd = random.randrange(len(nm1))
            names = nm1[rnd]
        elif i < 7:
            rnd = random.randrange(len(nm2))
            names = nm2[rnd]
        else:
            rnd = random.randrange(len(nm3))
            names = nm3[rnd]

    return names


if __name__ == "__main__":

    print(nameGen())
