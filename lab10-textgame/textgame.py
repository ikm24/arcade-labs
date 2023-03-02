"""
Text game
"""

class Room:
    """Represents a room"""

    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

def main():
    room_list = []
    Lobby = Room("Lobby", None, None, 3, 1)
    Dining_room = Room("Dining room", 2, None, 0, None)
    Kitchen = Room("Kitchen", None, 1, None, None)
    Lounge = Room("Lounge", 5, 0, 4, None)
    Balcony = Room("Balcony", None, None, None, 3)
    Hallway = Room("Hallway", 6, 7, 3, 8)
    Bathroom = Room("Bathroom", 5, None, None, None)
    Bedroom = Room("Bedroom", None, 5, None, None)
    Attic = Room("Attic", None, None, 5, None)

    room_list.append(Lobby)