class HotelTreeNode:
    def __init__(self, name, status='Vacant', children=None):
        self.name = name
        self.status = status
        self.children = [] if children is None else children

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return f"{self.name} ({self.status})"



class HotelTree:
    def __init__(self, num_floors, num_rooms_per_floor):
        self.num_floors = num_floors
        self.num_rooms_per_floor = num_rooms_per_floor
        self.rooms = {}
        for floor in range(1, num_floors + 1):
            for room_num in range(1, num_rooms_per_floor + 1):
                room_name = str(floor) + chr(64 + room_num)
                self.rooms[room_name] = 'Available'

    def book_room(self, room_num):
        if room_num in self.rooms and self.rooms[room_num] == 'Available':
            self.rooms[room_num] = 'Occupied'
            print(f"Room {room_num}: Occupied")
        else:
            print(f"Room {room_num}: Not available")




    def checkout_room(self, room_num):
        if room_num in self.rooms and self.rooms[room_num] == 'Occupied':
            self.rooms[room_num] = 'Vacant'
            print(f"Room {room_num}: Vacant")
        else:
            print(f"Room {room_num}: Not occupied")

    def clean_room(self, room_num):
        if room_num in self.rooms and self.rooms[room_num] == 'Vacant':
            self.rooms[room_num] = 'Available'
            print(f"Room {room_num}: Available")
        else:
            print(f"Room {room_num}: Cannot be cleaned")

    def repair_room(self, room_num):
        if room_num in self.rooms and self.rooms[room_num] == 'Vacant':
            self.rooms[room_num] = 'Repair'
            print(f"Room {room_num}: Under repair")
        else:
            print(f"Room {room_num}: Cannot be repaired")

    def end_repair(self, room_num):
        if room_num in self.rooms and self.rooms[room_num] == 'Repair':
            self.rooms[room_num] = 'Vacant'
            print(f"Room {room_num}: Vacant after repair")
        else:
            print(f"Room {room_num}: Not under repair")


    def traverse(self):
        for room_num, status in self.rooms.items():
            print(f"Room {room_num}: {status}")

    def traverse_floorwise(self):
        available_room = None
        for floor in range(1, self.num_floors+1):
            for room_num in range(1, self.num_rooms_per_floor+1):
                room_name = str(floor) + chr(64 + room_num)
                if self.rooms[room_name] == 'Available':
                    available_room = room_name
                    break
            if available_room:
                break
        return available_room
