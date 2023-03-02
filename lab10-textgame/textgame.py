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
    lobby = Room(
        "Te despiertas en lo que parece la entrada de una casa. No sabes como has llegado alli y te sientes algo " +
        "mareado y desubicado.\nTratas de abrir la puerta principal de la casa, fallando en el intento: esta cerrada con llave. " +
        "Decides explorar la casa en busca de otra salida.\nTienes dos puertas accesibles, al este(e) y al oeste(w)."
                 , None, None, 3, 1)
    room_list.append(lobby)
    dining_room = Room("Dining room", 2, None, 0, None)
    room_list.append(dining_room)
    kitchen = Room("Kitchen", None, 1, None, None)
    room_list.append(kitchen)
    lounge = Room("Lounge", 5, 0, 4, None)
    room_list.append(lounge)
    balcony = Room("Balcony", None, None, None, 3)
    room_list.append(balcony)
    hallway = Room("Hallway", 6, 7, 3, 8)
    room_list.append(hallway)
    bedroom = Room("Bedroom", None, 5, None, None)
    room_list.append(bedroom)
    bathroom = Room("Bathroom", 5, None, None, None)
    room_list.append(bathroom)
    attic = Room("Attic", None, None, 5, None)
    room_list.append(attic)
    current_room = 0
    done = False

    while (done==False):
        print(room_list[current_room].description)

main()