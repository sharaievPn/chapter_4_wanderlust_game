"""
Module contains all classes for the main.py
"""


class Room:
    """
    Contains all characteristics that are connected with room
    >>> kitchen = Room("Kitchen")
    >>> kitchen.set_description("A dank and dirty room buzzing with flies.")

    >>> dining_hall = Room("Dining Hall")
    >>> dining_hall.set_description("A large room with ornate golden decorations on each wall.")

    >>> ballroom = Room("Ballroom")
    >>> ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

    >>> kitchen.link_room(dining_hall, "south")
    >>> dining_hall.link_room(kitchen, "north")
    >>> dining_hall.link_room(ballroom, "west")
    >>> ballroom.link_room(dining_hall, "east")

    >>> kitchen.name
    'Kitchen'

    >>> dining_hall.description
    'A large room with ornate golden decorations on each wall.'

    >>> kitchen.move('south').name
    'Dining Hall'
    """
    def __init__(self, name):
        """
        Initializes data
        :param name:
        """
        self.description = None
        self.item = None
        self.character = None
        self.name = name
        self.side_dct = dict()

    def set_description(self, room_description):
        """
        Sets description for room
        :param room_description:
        :return:
        """
        self.description = room_description
        return None

    def link_room(self, room: object, side: str):
        """
        Links to the current room another room connecting with the globe side
        :param room:
        :param side:
        :return:
        """
        self.side_dct.update({side: room})
        return None

    def set_character(self, character: object):
        """
        Sets person who is in this room
        :param character:
        :return:
        """
        self.character = character
        return None

    def set_item(self, item: object):
        """
        Sets item which is in this room
        :param item:
        :return:
        """
        self.item = item
        return None

    def get_details(self):
        """
        Displays descriptions of the room
        :return:
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for side in list(self.side_dct.keys()):
            print(f"The {self.side_dct[side].name} is {side}")
        return None

    def get_character(self):
        """
        Returns person who is in this room
        :return:
        """
        return self.character

    def get_item(self):
        """
        Returns item which is in the room
        :return:
        """
        return self.item

    def move(self, side: str):
        """
        Changes room
        :param side:
        :return:
        """
        return self.side_dct[side]


class Enemy:
    """
    Data about person who is in a certain room

    Attributes:
        wins = 0 (quantity of battles won)


    >>> dining_hall = Room("Dining Hall")
    >>> ballroom = Room("Ballroom")
    >>> dave = Enemy("Dave", "A smelly zombie")
    >>> dave.set_conversation("What's up, dude! I'm hungry.")
    >>> dave.set_weakness("cheese")
    >>> dining_hall.set_character(dave)

    >>> tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
    >>> tabitha.set_conversation("Sssss....I'm so bored...")
    >>> tabitha.set_weakness("book")
    >>> ballroom.set_character(tabitha)

    >>> tabitha.talk()
    [Tabitha says] Sssss....I'm so bored...

    >>> tabitha.weakness
    'book'

    >>> ballroom.character.name
    'Tabitha'
    """
    wins = 0

    def __init__(self, name, tipe):
        """
        Initializes data
        :param name:
        :param tipe:
        """
        self.weakness = None
        self.conversation = None
        self.name = name
        self.type = tipe

    def set_conversation(self, conversation):
        """
        Sets response of the person
        :param conversation:
        :return:
        """
        self.conversation = conversation
        return None

    def set_weakness(self, weakness):
        """
        Sets item which can defeat person
        :param weakness:
        :return:
        """
        self.weakness = weakness
        return None

    def describe(self):
        """
        Displays description of the person
        :return:
        """
        print(f"{self.name} is here!")
        print(self.type)
        return None

    def talk(self):
        """
        Displays phrase of the person
        :return:
        """
        print(f"[{self.name} says] {self.conversation}")
        return None

    def fight(self, fight_with: str):
        """
        Makes the user find with person.
        According to the battle result adds won battles or
        displays that player is defeated
        :param fight_with:
        :return:
        """
        if fight_with == self.weakness:
            Enemy.wins += 1
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

    @staticmethod
    def get_defeated():
        """
        Counts battles won
        :return:
        """
        return Enemy.wins


class Item:
    """
    Contains information about items

    >>> dining_hall = Room("Dining Hall")
    >>> ballroom = Room("Ballroom")

    >>> cheese = Item("cheese")
    >>> cheese.set_description("A large and smelly block of cheese")
    >>> ballroom.set_item(cheese)

    >>> book = Item("book")
    >>> book.set_description("A really good book entitled 'Knitting for dummies'")
    >>> dining_hall.set_item(book)

    >>> book.describe()
    The [book] is here - A really good book entitled 'Knitting for dummies'

    >>> dining_hall.get_item().name
    'book'
    """
    def __init__(self, name):
        """
        Initializes data
        :param name:
        """
        self.description = None
        self.name = name

    def set_description(self, description):
        """
        Sets description of the item
        :param description:
        :return:
        """
        self.description = description
        return None

    def describe(self):
        """
        Displays description of the item
        :return:
        """
        print(f"The [{self.name}] is here - {self.description}")
        return None

    def get_name(self):
        """
        Returns item's name
        :return:
        """
        return self.name


if __name__ == '__main__':
    import doctest
    doctest.testmod()
