import pytest
from pokemon import Pokemon, Player

all_data = {'Poggers': {
                        'against_bug': 2,
                        'against_dark': 0.5,
                        'against_dragon': 1,
                        'against_electric': 1,
                        'against_fairy': 1,
                        'against_fight': 1,
                        'against_fire': 1,
                        'against_flying': 1,
                        'against_ghost': 1,
                        'against_grass': 1,
                        'against_ground': 1,
                        'against_ice': 1,
                        'against_normal': 1,
                        'against_poison': 1,
                        'against_psychic': 1,
                        'against_rock': 1,
                        'against_steel': 1,
                        'against_water': 1,
                        'attack': 10,
                        'base_egg_steps': 1,
                        'base_happiness': 1,
                        'base_total': 1,
                        'capture_rate': 1,
                        'classfication': 1,
                        'defense': 10,
                        'experience_growth': 1,
                        'height_m': 1,
                        'hp': 10,
                        'japanese_name': 'Poggers',
                        'name': 'Poggers',
                        'percentage_male': 1,
                        'pokedex_number': 1,
                        'sp_attack': 1,
                        'sp_defense': 1,
                        'speed': 1,
                        'type1': 'bug',
                        'type2': 'dark',
                        'weight_kg': 10,
                        'generation': 1,
                        'is_legendary': 0
    },
            'Froggers': {
                        'against_bug': 2,
                        'against_dark': 0.5,
                        'against_dragon': 1,
                        'against_electric': 1,
                        'against_fairy': 1,
                        'against_fight': 1,
                        'against_fire': 1,
                        'against_flying': 1,
                        'against_ghost': 1,
                        'against_grass': 1,
                        'against_ground': 1,
                        'against_ice': 1,
                        'against_normal': 1,
                        'against_poison': 1,
                        'against_psychic': 1,
                        'against_rock': 1,
                        'against_steel': 1,
                        'against_water': 1,
                        'attack': 10,
                        'base_egg_steps': 1,
                        'base_happiness': 1,
                        'base_total': 1,
                        'capture_rate': 1,
                        'classfication': 1,
                        'defense': 10,
                        'experience_growth': 1,
                        'height_m': 1,
                        'hp': 5,
                        'japanese_name': 'Froggers',
                        'name': 'Froggers',
                        'percentage_male': 1,
                        'pokedex_number': 1,
                        'sp_attack': 1,
                        'sp_defense': 1,
                        'speed': 1,
                        'type1': 'bug',
                        'type2': 'grass',
                        'weight_kg': 10,
                        'generation': 1,
                        'is_legendary': 0
    }}


def test_pok_create():
    poggers = Pokemon(all_data, 'Poggers')
    assert str(poggers) == 'Poggers'
    assert poggers.is_dead() is False
    assert poggers.current_defense() == 10
    assert poggers.current_hp() == 10
    assert poggers.pok_data('against_fire') == 1


def test_none_pok_create():
    poggers = Pokemon(all_data, None)
    assert str(poggers) == 'None'
    assert poggers.is_dead() is True
    assert poggers.current_defense() is None
    assert poggers.current_hp() is None


def test_pok_name():
    poggers = Pokemon(all_data, 'Poggers')
    assert str(poggers) == 'Poggers'
    poggers.take_damage(40.0)
    assert str(poggers) == 'Dead'


def test_pok_pok_data_not_used_parameter():
    poggers = Pokemon(all_data, 'Poggers')
    assert poggers.pok_data('is_legendary') == 0


def test_pok_set_current_hp():
    poggers = Pokemon(all_data, 'Poggers')
    poggers.set_current_hp(7.0)
    assert poggers.current_hp() == 7.0


def test_pok_defend():
    poggers = Pokemon(all_data, 'Poggers')
    poggers.defend()
    assert poggers.current_defense() == 11.0


def test_pok_defend2():
    poggers = Pokemon(all_data, 'Poggers')
    poggers.set_current_defense(11.0)
    assert poggers.current_defense() == 11.0


def test_pok_take_damage():
    poggers = Pokemon(all_data, 'Poggers')
    poggers.take_damage(5)
    assert poggers.current_hp() == 5


def test_pok_attack_normal(monkeypatch):
    def not_rand(a, b):
        return 100
    monkeypatch.setattr('pokemon.random.randint', not_rand)
    poggers1 = Pokemon(all_data, 'Poggers')
    poggers2 = Pokemon(all_data, 'Poggers')
    poggers1.attack(poggers2)
    assert poggers2.current_hp() == 7.6


def test_pok_attack_special1(monkeypatch):
    def not_rand(a, b):
        return 100
    monkeypatch.setattr('pokemon.random.randint', not_rand)
    poggers1 = Pokemon(all_data, 'Poggers')
    poggers2 = Pokemon(all_data, 'Poggers')
    poggers1.attack(poggers2, 1)
    assert poggers2.current_hp() == 5.2


def test_pok_attack_special2(monkeypatch):
    def not_rand(a, b):
        return 100
    monkeypatch.setattr('pokemon.random.randint', not_rand)
    poggers1 = Pokemon(all_data, 'Poggers')
    poggers2 = Pokemon(all_data, 'Poggers')
    poggers1.attack(poggers2, 2)
    assert poggers2.current_hp() == 8.8


def test_pok_dies():
    poggers = Pokemon(all_data, 'Poggers')
    poggers.take_damage(16)
    assert poggers.current_hp() == 0
    assert poggers.is_dead() is True


def test_pok_dies2():
    poggers = Pokemon(all_data, 'Poggers')
    poggers.death()
    assert poggers.is_dead() is True


def test_player_creation():
    player1 = Player(all_data, "Jacek", ['Poggers', 'Froggers'])
    player2 = Player(all_data, "Andrzej", ['Froggers', 'Poggers'], player1)
    player1.set_enemy(player2)
    assert str(player1) == 'Jacek'
    assert str(player2) == 'Andrzej'
    assert str(player1.pokemon(1)) == 'Poggers'
    assert str(player1.pokemon(2)) == 'Froggers'
    assert str(player1.enemy()) == 'Andrzej'


def test_player_some_pokemons_alive():
    player1 = Player(all_data, "Jacek", ['Poggers', 'Froggers'])
    player2 = Player(all_data, "Andrzej", ['Froggers', 'Poggers'], player1)
    player1.set_enemy(player2)
    player2.pokemon(1).take_damage(30)
    player2.pokemon(2).take_damage(30)
    assert player1.some_pokemons_alive() is True
    assert player2.some_pokemons_alive() is False


def test_player_change_current1():
    player1 = Player(all_data, "Jacek", ['Poggers', 'Froggers'])
    player1.pokemon(2).take_damage(30)
    assert player1.change_current(1) == 3
    assert player1.change_current(2) == 2
    assert player1.change_current(3) == 1


def test_player_change_current2():
    player1 = Player(all_data, "Jacek", ['Poggers', 'Froggers'])
    player1.change_current(2)
    assert player1.current_pokemon == player1.pokemon(2)
    pass


def test_player_pokemon_info():
    player1 = Player(all_data, "Jacek", ['Poggers', 'Froggers'])
    assert str(player1.pokemon(1)) == 'Poggers'
    assert player1.pokemon(1).is_dead() is False
    assert player1.pokemon(1).current_defense() == 10
    assert player1.pokemon(1).current_hp() == 10
    assert player1.pokemon(1).pok_data('against_fire') == 1
