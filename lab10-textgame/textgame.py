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
    room = Room("Lobby",None,None,1,3)


