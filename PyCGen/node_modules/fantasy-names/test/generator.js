var should = require('chai').should(), generator = require('../generator');

describe('#generator', function() {
	it('Produces a single name with 2 arguments', () => generator('military', 'nato').split('\n').length.should.equal(1));
	it('Produces a single name with 3 arguments', () => generator('military', 'nato', 1).split('\n').length.should.equal(1));
	it('Produces no names with 3 arguments',      () => generator('military', 'nato', -10).should.be.empty);
	it('Produces no names with 4 arguments',      () => generator('military', 'nato', 0, 0).should.be.empty);
	it('Produces a single name with 4 arguments', () => generator('military', 'nato', 1, 0).split('\n').length.should.equal(1));
	it('Produces ten names with 4 arguments',     () => generator('military', 'nato', 10, 0).split('\n').length.should.equal(10));

	it('Returns different results without a seed', function() {
		const result = require('../generator')('military', 'nato', 10, 0);
		for(var i = 0; i < 1000; i++) {
			if(require('../generator')('military', 'nato', 10, 0) != result) return;
		}
		throw new Error();
	});

	it('Returns the same result with a seed', function() {
		const result = require('../generator')('military', 'nato', 10, 0, "Hello, World!");		
		for(var i = 0; i < 1000; i++) {
			if(require('../generator')('military', 'nato', 10, 0, "Hello, World!") != result) throw new Error();
		}
	});

	it('Check each generator works', function() {
		const generators = {
			"armour": ["belts", "boots", "chests", "cloaks", "gauntlets", "helmets", "legs", "pauldrons", "shields", "vambraces"],
			"descriptions": ["aliens", "animals", "armys", "backstorys", "battlefields", "bows", "castles", "characters", "citys", "coat_of_arms", "constellations", "countrys", "diseases", "dragons", "dungeons", "dyings", "fancy_clothings", "flags", "gems", "ghost_towns", "gods", "hand_gestures", "holidays", "houses", "humanoids", "laws", "leather_armors", "martial_arts", "medieval_clothings", "monuments", "pains", "personalitys", "pistols", "planets", "plants", "plate_armors", "plots", "pokemons", "potions", "prophecys", "quests", "rag_clothings", "rifles", "school_uniforms", "shields", "shotguns", "societys", "spells", "staffs", "taverns", "towns", "traditions", "wands", "weapons"],
			"destiny": ["awokens", "cabals", "exos", "fallens", "hives", "humans", "vexs"],
			"diablo": ["angels", "demons", "khazras", "nephalems"],
			"doctor_who": ["daleks", "gallifreyans", "ice_warriors", "raxacoricofallapatorians", "silurians", "sontarans", "zygons"],
			"dragon_age": ["dwarfs", "elfs", "humans", "qunaris"],
			"dragon_ball": ["frieza_clans", "hakaishins", "humans", "others", "saiyans", "skians", "tuffles"],
			"dungeon_and_dragons": ["devas", "dragonborns", "drows", "dwarfs", "eladrins", "elfs", "githzerais", "gnomes", "goliaths", "halflings", "half_elfs", "half_orcs", "humans", "minotaurs", "shardminds", "shifters", "tieflings", "wildens"],
			"elder_scrolls": ["altmers", "argonians", "bosmers", "bretons", "daedrics", "dragons", "dunmers", "dwemers", "falmers", "forsworns", "imperials", "khajiits", "nords", "orc", "redguards", "spriggans"],
			"eve_online": ["amarrs", "caldaris", "gallentes", "minmatars"],
			"fantasy": ["aliens", "amazons", "angels", "animal_species", "animatronics", "apocalypse_mutants", "bandits", "barbarians", "bounty_hunters", "cat_people_nekojins", "cavemens", "centaurs", "christmas_elfs", "codes", "cowboys", "creatures", "deaths", "demons", "detectives", "dragons", "dryads", "dwarfs", "elementals", "elfs", "ents", "evils", "fairys", "fantasy_animals", "fantasy_races", "fantasy_surnames", "fursonas", "futuristics", "ghosts", "ghost_classifications", "giants", "gnolls", "gnomes", "goblins", "gods", "gorgons", "griffins", "half_elfs", "harpys", "heros", "hobbits", "horses", "imps", "kaijus", "killers", "knights", "kobolds", "lamias", "lichs", "mechas", "medievals", "mermaids", "minotaurs", "mobsters", "monsters", "mutant_species", "nagas", "necromancers", "nephilims", "ninjas", "nymphs", "ogres", "orcs", "pegasus", "phoenixs", "pirates", "robots", "satyr_fauns", "sea_creatures", "servants", "shapeshifters", "sirens", "slaves", "species", "steampunks", "succubus", "superhero_teams", "sylphs", "taurens", "trolls", "twins", "unicorns", "valkyries", "vampires", "vampire_clans", "villains", "warrior_nicknames", "werewolfs", "werewolf_packs", "witchs", "wizards", "zombie_types"],
			"final_fantasy": ["au_ras", "elezens", "hyurs", "lalafells", "miqotes", "roegadyns"],
			"game_of_thrones": ["dothrakis", "free_citys", "free_folks", "ghiscaris", "mountain_clans", "nicknames", "summer_islanders", "unsullieds", "valyrians", "westeros"],
			"guild_wars": ["asuras", "charrs", "human", "norns", "sylvaris"],
			"halo": ["forerunners", "huragoks", "jiralhanaes", "kig_yars", "mgalekgolos", "sangheilis", "san_shyuums", "unggoys"],
			"harry_potter": ["dragon_species", "goblins", "hippogriffs", "house_elfs", "winged_horses"],
			"inheritance_cycle": ["dragons", "dwarfs", "elfs", "humans", "urgals"],
			"legend_of_zelda": ["anoukis", "deitys", "dekus", "fairys", "gerudos", "gorons", "humans", "korok_kokiris", "minishs", "zoras"],
			"lord_of_the_rings": ["dwarfs", "elfs", "hobbits", "humans", "maiars", "orcs"],
			"lord_of_the_rings_online": ["beorning", "dwarf", "elf", "hobbit", "human"],
			"mass_effect": ["asaris", "batarians", "drells", "geths", "humans", "krogans", "quarians", "salarians", "turians"],
			"military": ["itu", "nato", "numeric", "royal_air_force", "royal_navy", "signalese", "telegram", "united_states"],
			"miscellaneous": ["afterlifes", "airplanes", "airships", "alliances", "animal_groups", "anime_attacks", "apocalypses", "armys", "artifacts", "attack_moves", "awards", "bands", "battles", "birds", "board_games", "book_titles", "bouquets", "brands", "candys", "cars", "chivalric_orders", "class", "clothing_brands", "colors", "constellations", "creepypastas", "crops", "currencys", "dances", "dates", "dinosaurs", "diseases", "drinks", "drugs", "enchantments", "energy_types", "epithets", "evil_groups", "foods", "fruit_vegetables", "fungis", "galaxys", "game_engines", "game_soundtracks", "gangs", "gear_enchantments", "gem_minerals", "graffiti_tags", "guilds", "hackers", "heists", "helicopters", "herbs", "holidays", "holy_books", "human_species", "instruments", "inventions", "jewelrys", "languages", "love_nicknames", "magazines", "magical_diseases", "magical_plants", "magical_trees", "magic_types", "martial_arts", "mascots", "medicines", "metals", "military_divisions", "military_operations", "military_ranks", "military_vehicles", "molecules", "motorcycle_clubs", "mutant_plants", "natural_disasters", "newspapers", "nicknames", "noble_houses", "pirate_crews", "pirate_ships", "plagues", "plants", "poisons", "political_partys", "post_apocalyptic_societys", "potions", "professions", "racers", "railways", "ranks", "religions", "scientific_creatures", "ships", "siege_engines", "softwares", "song_titles", "spaceships", "space_fleets", "spells", "sports", "sports_teams", "squads", "superpowers", "teleportations", "thrones", "time_periods", "titles", "tool_nicknames", "treatys", "trees", "tribals", "tribes", "usernames", "vehicles", "video_games", "vocal_groups", "weapon_abilities", "web_series", "wines", "wrestlers", "wrestling_moves"],
			"pathfinder": ["aasimars", "catfolks", "drows", "dwarfs", "elfs", "fetchlings", "gnomes", "goblins", "halflings", "half_elfs", "half_orcs", "hobgoblins", "humans", "ifrits", "kobolds", "orcs", "oreads", "ratfolks", "sylphs", "tengus", "tians", "tieflings", "undines"],
			"pets": ["aliens", "amphibians", "bats", "bears", "birds", "bird_of_preys", "cats", "cows", "crabs", "deers", "dogs", "elephants", "fishs", "horses", "insects", "lions", "marine_mammals", "monkeys", "mouses", "owls", "parrots", "pigs", "rabbits", "reptiles", "rodents", "sheeps", "turtles", "wolfs"],
			"places": ["amusement_parks", "antique_stores", "asylums", "bakerys", "banks", "battle_arenas", "beachs", "brewerys", "bridges", "business", "cafes", "camps", "casinos", "castles", "caves", "circus", "city_districts", "civilizations", "cliffs", "companys", "continents", "countrys", "day_cares", "dimensions", "dungeons", "farms", "film_studios", "fire_lands", "forests", "game_studios", "grasslands", "graveyards", "harbors", "headquarters", "hospitals", "hotels", "inns", "islands", "jungles", "kingdoms", "laboratorys", "lakes", "lands", "librarys", "magic_schools", "magic_shops", "mansions", "mining_companys", "mountains", "museums", "nightclubs", "oasis", "orphanages", "outposts", "parks", "pirate_coves", "planets", "plantations", "plazas", "prisons", "realms", "restaurants", "rivers", "roads", "ruins", "schools", "shops", "sky_islands", "snowlands", "space_colonys", "stadiums", "stars", "streets", "swamps", "temples", "theaters", "towers", "volcanos", "waterfalls", "waters"],
			"pop_culture": ["arthurians", "avatar_last_airbenders", "digimons", "dragonriders_of_perns", "homestucks", "how_to_train_your_dragons", "hunger_games", "hyborians", "lovecraftians", "maze_runners", "mortal_kombats", "my_little_ponys", "one_piece_devil_fruits", "pacific_rims", "pokemons", "rwbys", "shadowhunter_chronicles", "skulduggery_pleasants", "starcrafts", "stormlight_archives", "transformers", "warrior_cats", "wheel_of_times", "wings_of_fires", "x_mens"],
			"real": ["20th_century_englishs", "aboriginals", "african_americans", "akans", "albanians", "algerians", "amazighs", "ancient_greeks", "anglo_saxons", "argentinians", "armenians", "assyrians", "azerbaijanis", "aztecs", "babylonians", "basothos", "basques", "belgians", "bengalis", "biblicals", "bosnians", "brazilians", "bulgarians", "burmese_myanmars", "cajuns", "catalans", "celtics", "celtic_bretons", "celtic_welshs", "chineses", "circassians", "colonial_americans", "croatians", "czechs", "danishs", "dutchs", "edo_japaneses", "edwardians", "egyptians", "englishs", "enochians", "estonians", "ethiopians", "faroeses", "filipinos", "finnishs", "frankishs", "frenchs", "frisians", "georgians", "germans", "gothics", "greeks", "hausas", "hawaiians", "hebrews", "hillbillys", "hindus", "hippies", "hispanics", "hungarians", "icelandics", "indonesians", "inuits", "irishs", "italians", "jamaicans", "japaneses", "jewishs", "kazakhs", "khmers", "koreans", "kurdishs", "laotians", "latins", "latvians", "lithuanians", "malaysians", "malteses", "maoris", "mayans", "modern_egyptians", "mongolians", "moroccans", "muslims", "native_americans", "natures", "nepaleses", "normans", "norwegians", "old_high_germans", "pashtuns", "persians", "polishs", "portugueses", "poshs", "punjabis", "puritans", "quebecois", "romanians", "romans", "roma_gypsys", "russians", "serbians", "shakespeareans", "shonas", "sikhs", "sinhaleses", "slavics", "slovenians", "somalis", "stages", "suebis", "sumerians", "swahilis", "swedishs", "swiss", "tajiks", "tamils", "telugus", "thais", "tibetans", "turkishs", "twins", "ukrainians", "victorians", "vietnameses", "vikings", "yorubas", "zulus"],
			"rift": ["bahmis", "dwarfs", "eths", "high_elfs", "kelaris", "mathosians"],
			"star_trek": ["andorians", "bajorans", "benzites", "betazoids", "bolians", "caitians", "ferengis", "gorns", "jemhadars", "klingons", "letheans", "nausicaans", "orions", "pakleds", "remans", "rigelians", "romulans", "saurians", "tellarites", "trills", "vulcans"],
			"star_wars": ["anzatis", "biths", "bothans", "darths", "devaronians", "dugs", "duross", "ewoks", "falleens", "gamorreans", "gands", "gotals", "grans", "gungans", "hutts", "iktotchis", "ishi_tibs", "ithorians", "jawas", "kel_dors", "korunnais", "mandalorians", "mon_calamaris", "nautolans", "neimoidians", "niktos", "ortolans", "quarrens", "rodians", "shistavanens", "sullustans", "swiss", "toydarians", "trandoshans", "tusken_raiders", "weequays", "wookiees"],
			"star_wars_the_old_republic": ["cathars", "chiss", "cyborgs", "human_sws", "miralukas", "mirialans", "rattatakis", "siths", "togrutas", "twileks", "zabraks"],
			"the_witcher": ["dwarfs", "elfs", "halflings", "humans"],
			"towns_and_cities": ["ancient_greek_towns", "apocalypse_towns", "central_african_towns", "central_american_towns", "central_east_african_towns", "citys", "city_nicknames", "dwarven_citys", "east_asian_towns", "east_european_towns", "egyptian_towns", "elven_citys", "fantasy_towns", "middle_eastern_towns", "northern_south_american_towns", "north_african_towns", "north_american_towns", "north_european_towns", "oceania_towns", "orcish_citys", "roman_towns", "russian_towns", "southeast_african_towns", "southeast_asian_towns", "southeast_european", "south_african_towns", "south_american_towns", "south_asian_towns", "south_european_towns", "steampunk_citys", "towns", "underwater_citys", "viking_towns", "west_african_towns", "west_european_towns", "wild_west_towns"],
			"warhammer": ["beastmens", "bretonnias", "daemons_of_chaos", "dark_elfs", "dwarfs", "empires", "goblins", "high_elfs", "lizardmens", "ogres", "orcs", "skavens", "tomb_kings", "vampire_counts", "warriors_of_chaos", "wood_elfs"],
			"warhammer_40k": ["chaos", "dark_eldars", "eldars", "necrons", "orks", "sisters_of_battles", "space_marines", "taus"],
			"weapons": ["battle_axes", "bomb_missiles", "bows", "claw_weapons", "daggers", "dual_wields", "fist_weapons", "flails", "magic_books", "magic_weapons", "pistols", "rifles", "sci_fi_guns", "scythes", "shotguns", "spears", "staffs", "swords", "throwing_weapons", "war_hammers", "whips"],
			"wildstar": ["wildstar_aurins", "wildstar_cassians", "wildstar_chuas", "wildstar_drakens", "wildstar_granoks", "wildstar_humans", "wildstar_mecharis", "wildstar_mordeshs"],
			"world_of_warcraft": ["blood_elf", "draenei", "dwarf", "forsaken", "gnome", "goblin", "human", "night_elf", "orc", "pandaren", "tauren", "troll", "worgen"],
			"world_of_warcraft_pets": ["bat_dragonhawks", "birds", "boars_bears", "cats", "crabs", "dino_rhinos", "dog_wolfs", "goat_porcupines", "gorilla_monkeys", "insects", "reptiles", "wow_pets"]
		};

		// Generate a single name with each generator.
		var failed = 0;
		for(var group in generators) {
			for(var individual in generators[group]) {
				try {
					var value = generator(group, generators[group][individual]).length;
					if(value == 0) throw new Error(value);
				} catch(e) {
					if(failed == 0) {
						failed++;
						console.error("Failing:\n========");
					}
					console.error(" > " + group + "," + generators[group][individual] + ": " + e);
				}
			}
		}

		if(failed > 0) throw new Error(failed);
	});
});
