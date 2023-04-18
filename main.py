from hotel import HotelTree
# create hotel with 3 floors and 4 rooms on each floor
hotel = HotelTree(3, 4)

# check initial room status
print("Initial Room Status")
hotel.traverse()

# book a room
hotel.book_room("1A")
print("\nRoom 1A is booked")
hotel.traverse()

# try to book an occupied room
hotel.book_room("1A")
print("\nTrying to book an occupied room 1A")
hotel.traverse()

# book another room
hotel.book_room("2B")
print("\nRoom 2B is booked")
hotel.traverse()


# check-out from the room
hotel.checkout_room("1A")
print("\nGuest checked-out from room 1A")
hotel.traverse()

# clean the vacant room
hotel.clean_room("1A")
print("\nRoom 1A is cleaned")
hotel.traverse()

# repair the room
hotel.repair_room("1A")
print("\nRoom 1A is repaired")
hotel.traverse()

# traverse floor wise and find first available room
print("\nFirst available room:", hotel.traverse_floorwise())

# try to book a room that does not exist
hotel.book_room("4A")
print("\nTrying to book a room that does not exist")
hotel.traverse()