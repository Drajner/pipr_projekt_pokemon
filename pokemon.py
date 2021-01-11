import csv
import random

POKEMON_MAX_NUMBER=6


class Player:
    """
    class Player - class containing data about player
    atributes : all_data - data from file about all pokemons
                pokemons - team of pokemons (class Pokemon)
                current_pokemon - pokemon which is fighting (class Pokemon)
                name - name of the player (string)
                enemy - opponent of the player (class Player)
    """
    def __init__(self, all_data, name, pokemon_names, enemy=None):
        self._name = name
        self._pokemons = []
        for name in pokemon_names:
            self._pokemons.append(Pokemon(all_data, name))
        """
        self.pokemon1 = Pokemon(all_data, pokemon_name1)
        self.pokemon2 = Pokemon(all_data, pokemon_name2)
        self.pokemon3 = Pokemon(all_data, pokemon_name3)
        self.pokemon4 = Pokemon(all_data, pokemon_name4)
        self.pokemon5 = Pokemon(all_data, pokemon_name5)
        self.pokemon6 = Pokemon(all_data, pokemon_name6)
        """
        self.current_pokemon = None
        self._enemy = None
    """
    __str__ - returns name of the player
    """
    def __str__(self):
        return self._name
    """
    pokemon - returns requested pokemon if it exists
    """
    def pokemon(self, number_of_pokemon):
        try:
            number_of_pokemon -= 1
            return self._pokemons[number_of_pokemon]
        except Exception:
            return None
    """
    pokemon_list - returns list of pokemons
    """
    def pokemon_list(self):
        return self._pokemons
    """
    set_enemy - sets new_enemy (class Player) as enemy of the player
    """
    def set_enemy(self, new_enemy):
        self._enemy = new_enemy
    """
    enemy - retuns enemy
    """
    def enemy(self):
        return self._enemy
    """
    some_pokemons_alive - checks if the player has any remaining pokemons
    """
    def some_pokemons_alive(self):
        some_pokemon_is_alive = False
        list_of_pokemons = self.pokemon_list()
        for pokemon in list_of_pokemons:
            if pokemon.is_dead() is False:
                some_pokemon_is_alive = True
        return some_pokemon_is_alive
    """
    choose_action - chooses action basing on the numbers given by the Interface
    attributes:
        action_number - main number necessary for choice of action (int 1-4)
        pokemon_number - number needed only for action 4 to change pokemon (int 1-6)
        use_target_type - number needed only for action 2 to attack on certain type (int 1-2)
    returns 0 if none of the actions have been chosen
    """
    def choose_action(self, action_number, pokemon_number=None, use_target_type=None):

        if action_number == 1:
            self.current_pokemon.attack(self.enemy().current_pokemon)
        elif action_number == 2:
            self.current_pokemon.attack(self.enemy().current_pokemon, use_target_type)
        elif action_number == 3:
            self.current_pokemon.defend()
        elif action_number == 4:
            self.change_current(pokemon_number)
        else:
            return 0

    """
    change_current - chooses another pokemon with pokemon_number to take part in fight
    return is not necessary, but is a base of responses from the interface if action dictated by the player can't be made
    0 means that the change of pokemon is pointless
    1 means that pokemon with this number does not exist
    2 means that pokemon of this number is dead
    3 means that choice went smoothly
    """
    def change_current(self, pokemon_number):
        pokemon_wanted = self.pokemon(pokemon_number)
        """
        if pokemon_number == 1:
            pokemon_wanted = self._pokemon1
        elif pokemon_number == 2:
            pokemon_wanted = self._pokemon2
        elif pokemon_number == 3:
            pokemon_wanted = self._pokemon3
        elif pokemon_number == 4:
            pokemon_wanted = self._pokemon4
        elif pokemon_number == 5:
            pokemon_wanted = self._pokemon5
        elif pokemon_number == 6:
            pokemon_wanted = self._pokemon6
        else:
            return 1
        """
        if pokemon_wanted:
            if self.current_pokemon == pokemon_wanted:
                return 0
            elif pokemon_wanted.is_dead():
                return 2
            else:
                self.current_pokemon = pokemon_wanted
                return 3
        else:
            return 1


class Pokemon:
    """
    class Pokemon - class containing data about Pokemon
    attributes : all_data - data from file about all pokemons
                 pok_data - contains all data from csv file pokemon.csv
                 current_hp - amount of hit points
                 is_dead - tells if pokemon is dead
                 current_defense - amount of defense
    """
    def __init__(self, all_data, name):
        if name is None:
            self._is_dead = True
            self._pok_data = None
            self._current_hp = None
            self._current_defense = None
        else:
            self._pok_data = all_data[name]
            self._current_hp = float(self._pok_data['hp'])
            self._is_dead = False
            self._current_defense = float(self._pok_data['defense'])
    """
    pok_data - gets requested data from _pok_data (dictionary)
    """
    def pok_data(self, request):
        return self._pok_data[request]
    """
    current_hp - returns amount of hit points
    """
    def current_hp(self):
        return self._current_hp
    """
    current_defense - returns amount of defense
    """
    def current_defense(self):
        return self._current_defense
    """
    set_current_defense - changes current defense to new amount (new_def)
    """
    def set_current_defense(self, new_def):
        self._current_defense = new_def
    """
    death - changes status of the pokemon to dead
    """
    def death(self):
        self._is_dead = True
    """
    is_dead - checks if pokemon is dead
    """
    def is_dead(self):
        return self._is_dead
    """
    set_current_hp - sets new_hp as current_hp and if new_hp is below or equal to 0 "kills" pokemon
    """
    def set_current_hp(self, new_hp):
        if int(new_hp) <= 0:
            self._current_hp = 0
            self.death()
        else:
            self._current_hp = new_hp
    """
    __str__ - returns name of the pokemon
    """
    def __str__(self):
        if self.current_hp() is None:
            return 'None'
        elif self.is_dead():
            return 'Dead'
        else:
            return self.pok_data('name')
    """
    take_damage - applies damage to the pokemon
    """
    def take_damage(self, damage):
        new_hp = self.current_hp() - damage
        self.set_current_hp(new_hp)
    """
    attack - calculates damage and deals it to the opponents pokemon
    attributes: target - pokemon taking damage (class Pokemon)
                use_target_type - only in use when attack is special, used for choosing the type for attack (int 1-2)
    """
    def attack(self, target, use_target_type=None):
        modifier = float(random.randint(85, 100)) / 100.0
        if use_target_type:
            type_request = 'type' + str(use_target_type)
            against_type_modifier_name = 'against_' + target.pok_data(type_request)
            modifier *= float(self.pok_data(against_type_modifier_name))
        #damage = 2.4 * float(self.pok_data('attack')) / float(target.current_defense()) / 50.0 * modifier
        damage = 2.4 * float(self.pok_data('attack')) * modifier / float(target.current_defense())
        target.take_damage(damage)
    """
    defend - raises defense of the pokemon
    """
    def defend(self):
        new_def = self.current_defense() * 1.1
        self.set_current_defense(new_def)


class Game:
    """
    class Game - runs the game and contains interface
    all_data - data from csv file
    player1 - first player
    player2 - second player
    __init__ - loads data from file, initiates player and starts duel
    """
    def __init__(self):
        self.all_data = {}
        with open('pokemon.csv') as csvfile:
            data_from_file = csv.DictReader(csvfile)
            for line in data_from_file:
                self.all_data[line['name']] = line
            pass
        name, player_pokemons = self.player_creation()
        self.player1 = Player(self.all_data, name, player_pokemons)
        name, player_pokemons = self.player_creation()
        self.player2 = Player(self.all_data, name, player_pokemons)
        self.player1.set_enemy(self.player2)
        self.player2.set_enemy(self.player1)
        self.duel()
    """
    player_creation - takes input from player to get data about them
    """
    def player_creation(self):
        print('What is you name Player?')
        name = input()
        print('Hello ' + name + '!')
        choice_player_not_finished = True
        player_pokemons = []
        while choice_player_not_finished:
            print('Please name six pokemons you want to use.')
            print('Use their full names and strat with great letter (example: Bulbasaur)')
            print('If you want to use less just write "Stop", when you mention all you want to use.')
            player_pokemons = []
            enough_pokemon = False
            for i in range(POKEMON_MAX_NUMBER):
                if enough_pokemon:
                    break
                pokemon_is_not_chosen = True
                while pokemon_is_not_chosen:
                    available_names = self.all_data.keys()
                    answer = input()
                    if answer == "Stop":
                        pokemon_is_not_chosen = False
                        enough_pokemon = True
                        break
                    elif answer in available_names:
                        player_pokemons.append(answer)
                        print(str(i+1) + '. pokemon will be ' + player_pokemons[i])
                        pokemon_is_not_chosen = False
                    else:
                        print('Sorry I do not understand you. Please write again.')
            print("These are your pokemon:")
            for i in range(len(player_pokemons)):
                print(str(i+1) + '.' + player_pokemons[i])
            print("Right? Y/N")
            answer = input()
            if answer == 'N':
                print('OK lets start again')
            else:
                print('I will count that as "yes". Lets move on!')
                choice_player_not_finished = False
        return name, player_pokemons

    """
    duel - fight takes place here
    """
    def duel(self):
        there_is_no_winner = True
        winner = None
        print('Lets start the fight!')
        self.choose_pokemon(self.player1)
        self.choose_pokemon(self.player2)
        while there_is_no_winner:
            if self.player1.some_pokemons_alive():
                if self.player1.current_pokemon.is_dead():
                    print(str(self.player1) + ", your pokemon died!")
                    self.choose_pokemon(self.player1)
                else:
                    self.turn(self.player1)
            else:
                print(str(self.player1) + ", last of your pokemons died!")
                winner = self.player2
                there_is_no_winner = False
                break
            if self.player2.some_pokemons_alive():
                if self.player2.current_pokemon.is_dead():
                    print(str(self.player2) + ", your pokemon died!")
                    self.choose_pokemon(self.player2)
                else:
                    self.turn(self.player2)
            else:
                print(str(self.player2) + ", your pokemon died!")
                winner = self.player1
                there_is_no_winner = False
                break
        print("The winner is " + str(winner))
    """
    choose_pokemon - allows player to change pokemon
    """
    def choose_pokemon(self, player):
        player_have_not_chosen = True
        while player_have_not_chosen:
            print(str(player) + ", please choose a pokemon to fight:")
            for i in range(len(player.pokemon_list())):
                print(str(i+1)+'.' + str(player.pokemon(i+1)))
            answer = input()
            answers = ['1', '2', '3', '4', '5', '6']
            if answer in answers:
                response = player.change_current(int(answer))
                if response == 0:
                    print('This pokemon is already in use. You can not choose it.')
                elif response == 1:
                    print('There is no such pokemon.')
                elif response == 2:
                    print('This pokemon is dead.')
                elif response == 3:
                    player_have_not_chosen = False
                else:
                    print('Sorry something unexpected happened.')
            else:
                print('Sorry I do not understand.')
    """
    attack_special - if special attack is chosen by the player this module is used
    """
    def attack_special(self, player):
        if player.enemy().current_pokemon.pok_data('type2'):
            choice_not_made = True
            while choice_not_made:
                print('Please choose type to attack')
                print('1. ' + player.enemy().current_pokemon.pok_data('type1'))
                print('2. ' + player.enemy().current_pokemon.pok_data('type2'))
                answer = input()
                answers = ['1', '2']
                if answer in answers:
                    if int(answer) == 1:
                        player.current_pokemon.attack(player.enemy().current_pokemon, 1)
                        choice_not_made = False
                    elif int(answer) == 2:
                        player.current_pokemon.attack(player.enemy().current_pokemon, 2)
                        choice_not_made = False
                    else:
                        print('Sorry something went wrong! Lets try again.')
                else:
                    print('Sorry I do not understand please try again')
        else:
            player.current_pokemon.attack(player.enemy().current_pokemon, 1)

    """
    turn - module running single turn for player
    """
    def turn(self, player):
        player_did_not_finish_his_turn = True
        print(str(player) + ' turn')
        print(' ')
        print("Your pokemon:")
        print(str(player.current_pokemon))
        print("HP: " + str(player.current_pokemon.current_hp()))
        print("DEF: " + str(player.current_pokemon.current_defense()))
        print("ATK: " + str(player.current_pokemon.pok_data('attack')))
        print(' ')
        print("Enemy pokemon:")
        print(str(player.enemy().current_pokemon))
        print("HP: " + str(player.enemy().current_pokemon.current_hp()))
        print("DEF: " + str(player.enemy().current_pokemon.current_defense()))
        print("ATK: " + str(player.enemy().current_pokemon.pok_data('attack')))
        print('')
        print('Please choose your action:')
        print('1. Normal attack.')
        print('2. Special attack.')
        print('3. Defense.')
        print('4. Change pokemon.')
        while player_did_not_finish_his_turn:
            answer = input()
            answers = ['1', '2', '3', '4']
            if answer in answers:
                if int(answer) == 1:
                    player.current_pokemon.attack(player.enemy().current_pokemon)
                    player_did_not_finish_his_turn = False
                elif int(answer) == 2:
                    self.attack_special(player)
                    player_did_not_finish_his_turn = False
                elif int(answer) == 3:
                    player.current_pokemon.defend()
                    player_did_not_finish_his_turn = False
                elif int(answer) == 4:
                    self.choose_pokemon(player)
                    player_did_not_finish_his_turn = False
                else:
                    print('Sorry something went wrong! Lets try again.')
            else:
                print('Sorry I do not understand please try again')


game = Game()
"""
def __main__():
    game = Game()

if __name__ == "__main__":
    pass
"""
