# HotelManagement
Python class to manage hotel room booking.


The HotelTree class includes a  data structure, available_rooms, which is a dictionary that maps room numbers to HotelTreeNode objects. When a new room is added to the hotel, its node is added to available_rooms.

When the traverse_floorwise() method is called, it iterates over all the rooms in the hotel as before. However, when it encounters an available room, it removes it from available_rooms using the del statement.

After the method has finished traversing the hotel, it checks whether available_rooms is empty. If it's not, it finds the first available room by taking the minimum room number in available_rooms.

This optimization reduces the time complexity of finding the first available room to O(1), since we are now just doing a lookup in a dictionary rather than iterating over all the rooms in the hotel. The time complexity of traversing the hotel is still O(MN), where M is the number of floors and N is the number of rooms per floor.
