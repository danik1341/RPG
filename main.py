import inspect


class Character:
    """
    Represents a generic character in the Battle Arena.

    """

    def __init__(self, name, life=20, attack=10):
        """
        Initializes a Character instance with the given name, life points, and attack points.

        :param name: The name of the character.
        :param life: The initial life points of the character (default is 20).
        :param attack: The initial attack points of the character (default is 10).

        """
        self.name = name
        self.life = life
        self.attack = attack
        self.current_action = None

    def basic_attack(self, other_character):
        """
        Performs a basic attack on the target character.

        :param other_character: The target character to attack.

        """
        if not isinstance(other_character, Character):
            raise TypeError(
                "Parameter must be an instance of the Character class.")

        other_character.life -= self.attack
        print(f"{self.name} attacked {other_character.name}. {other_character.name}'s life reduced to {other_character.life}.")


class Druid(Character):
    def __init__(self, name, life=20, attack=5):
        super().__init__(name, life, attack)
        print(f"Spirit of Elune guide {name}'s path")
        print("|----------------------------------------------------------------|")

    def meditate(self):
        self.life += 10
        self.attack -= 2
        print(f"{self.name} meditates, gaining Mark of The Wild buff, increasing life by 10 and decreasing attack by 2.")
        print("|----------------------------------------------------------------|")

    def animal_help(self):
        self.attack += 5
        print(
            f"Beasts of the forest heed {self.name}'s call! Attack increased by 5")
        print("|----------------------------------------------------------------|")

    def fight(self, other_character):
        damage = int(0.25 * self.life + 0.75 * self.attack)
        other_character.life -= damage
        print(f"{self.name} attacks {other_character.name} with nature's fury. {other_character.name}'s life reduced by {damage}.")
        print("|----------------------------------------------------------------|")


class Warrior(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(
            f"Mighty {self.name} entered the killing field. Lok'tar Ogar!!!!!!!")
        print("|----------------------------------------------------------------|")

    def brawl(self, other_character):
        damage = 2 * self.attack
        other_character.life -= damage
        self.life += int(0.5 * self.attack)
        print(f"{self.name} engages in a brawl with {other_character.name}. "
              f"{self.name} bathes in their opponent's blood gaining {int(0.5 * self.attack)} life and {other_character.name} sufferes a devastating blow, reducing their life by {damage}.")
        print("|----------------------------------------------------------------|")

    def train(self):
        self.attack += 2
        self.life += 2
        print(f"{self.name} would not sit idle. Like a wet stone to a sword, {self.name} trains mind, body and soul, gaining 2 point to their attack and life")
        print("|----------------------------------------------------------------|")

    def roar(self, other_character):
        other_character.attack -= 3
        print(
            f"Lok'tar Ogar! {other_character.name} cowers in fear from {self.name} mighty roar, reducing their attack points by 3")
        print("|----------------------------------------------------------------|")


class Mage(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(
            f"The currents of magic are in upheaval. I, {self.name}, shall bend them to my will")
        print("|----------------------------------------------------------------|")

    def curse(self, other_character):
        other_character.attack -= 2
        print(
            f"Karabos kor koramond! {other_character.name} cursed by {self.name} vile magic, reducing their attack points by 2")
        print("|----------------------------------------------------------------|")

    def summon(self):
        self.attack += 3
        print(
            f"Chaos comes at my command! {self.name} summons a chaos minion increasing their attack by 3")
        print("|----------------------------------------------------------------|")

    def cast_spell(self, other_character):
        other_character.life -= self.attack/self.life
        print(f"{other_character.name} burns in arcane fire. {self.name} laugths as {other_character.name}'s flesh sizzling reducing their life by {self.attack/self.life}")
        print("|----------------------------------------------------------------|")


class_actions = {
    "Druid": {
        "1": {"name": "Basic Attack", "target": "enemy", "method": "basic_attack"},
        "2": {"name": "Meditate", "target": "self", "method": "meditate"},
        "3": {"name": "Animal Help", "target": "self", "method": "animal_help"},
        "4": {"name": "Fight", "target": "enemy", "method": "fight"},
    },
    "Warrior": {
        "1": {"name": "Basic Attack", "target": "enemy", "method": "basic_attack"},
        "2": {"name": "Brawl", "target": "enemy", "method": "brawl"},
        "3": {"name": "Train", "target": "self", "method": "train"},
        "4": {"name": "Roar", "target": "enemy", "method": "roar"},
    },
    "Mage": {
        "1": {"name": "Basic Attack", "target": "enemy", "method": "basic_attack"},
        "2": {"name": "Curse", "target": "enemy", "method": "curse"},
        "3": {"name": "Summon", "target": "self", "method": "summon"},
        "4": {"name": "Cast Spell", "target": "enemy", "method": "cast_spell"},
    }
}


def print_menu():
    """
    Print menu
    """
    print("==== Welcome to the Battle Arena ====")
    print("1. Play")
    print("2. Quit")


def choose_character_class(player_name):
    """
    Asks the player to choose a character class and returns the selected class.

    :param player_name: The name of the player choosing the character class.
    :return: The selected character class.

    """
    print(f"{player_name}, choose your character class:")
    for idx, character_class in enumerate(Character.__subclasses__(), start=1):
        print(f"{idx}. {character_class.__name__}")
    choice = None
    while not choice:
        try:
            choice = int(input("Who would you be in the Battle Arena: "))
            if not 1 <= choice <= len(Character.__subclasses__()):
                choice = None
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return Character.__subclasses__()[choice - 1]


def create_player():
    """
    Creates a new player by asking for their name and character class.

    :return: A new player instance.

    """
    name = input("Enter your character name: ")
    player_class = choose_character_class(name)
    return player_class(name)


def prompt_for_players():
    """
    Asks the user to input the number of players participating in the game.

    :return: The number of players participating.

    """
    num_players = 0
    while num_players <= 0:
        try:
            num_players = int(
                input("Enter the number of players (at least 2): "))
            if num_players < 2:
                print("Please enter a number greater than or equal to 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return num_players


def get_next_player(players, current_player_index):
    """
    Gets the next player in the list of players.

    :param players: The list of players in the game.
    :param current_player_index: The index of the current player.
    :return: The next player in the list.

    """
    return players[(current_player_index + 1) % len(players)]


def choose_action(character, players):
    """
    Displays the available actions for the given character and prompts the player to choose an action.

    :param character: The character for whom to choose an action.
    :param players: The list of players in the game.

    """
    class_name = character.__class__.__name__
    actions = class_actions[class_name]
    available_targets = [
        target for target in players if target != character]

    print(
        f"\n{character.name}, it's your turn | HP: {character.life} || Attack: {character.attack} | {class_name}")
    print("Your enemies are: ")
    for idx, player in enumerate(available_targets):
        print(
            f" * {player.name} | HP: {player.life} || Attack: {player.attack} | {player.__class__.__name__}")
    for idx, action_info in actions.items():
        print(f"{idx}. {action_info['name']}")

    while True:
        try:
            choice = input("What is your move? ")
            if choice not in actions.keys():
                choice = input("Please eneter a valid choice: ")
            else:
                character.current_action = choice
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def choose_target(character, players):
    """
    Prompts the player to choose a target for the chosen action of the given character.

    :param character: The character whose action needs a target.
    :param players: The list of players in the game.

    """
    class_name = character.__class__.__name__
    current_action = character.current_action

    if current_action:
        target_type = class_actions[class_name][current_action]['target']
        method_name = class_actions[class_name][current_action]['method']
        target = None

        if target_type == 'enemy':
            available_targets = [
                target for target in players if target != character]

            print("|----------------------| ")
            for idx, player in enumerate(available_targets):
                print(
                    f"{idx + 1}. {player.name} | HP: {player.life} || Attack: {player.attack} | {player.__class__.__name__}")

            while True:
                try:
                    target_index = int(
                        input("Choose which foe you want to attack: ")) - 1
                    if 0 <= target_index < len(available_targets):
                        target = available_targets[target_index]
                        break
                    else:
                        print("Please select a valid target: ")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        elif target_type == 'self':
            target = character

        if target and method_name:
            method = getattr(character, method_name)

            method_signature = inspect.signature(method)
            if len(method_signature.parameters) == 0:  # Only 'self' parameter
                method()
            else:
                method(target)

    else:
        print('Unexpected Error')
        return None


def play_game():
    """
    Starts the Battle Arena game, displaying the main menu, processing player's choice, and running the game loop.

    """
    print_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        num_players = prompt_for_players()
        players = []
        for _ in range(num_players):
            player = create_player()
            players.append(player)

        current_player_index = 0

        while True:
            current_player = players[current_player_index]
            choose_action(current_player, players)
            choose_target(current_player, players)

            defeated_players = [
                player for player in players if player.life <= 0]
            if defeated_players:
                for player in defeated_players:
                    players.remove(player)

                if len(players) == 1:
                    print(
                        f"\nCongratulations! {players[0].name} is the winner!")
                    break

            current_player_index = (current_player_index + 1) % len(players)

    elif choice == "2":
        print("Thanks for playing! See you next time.")
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    play_game()
