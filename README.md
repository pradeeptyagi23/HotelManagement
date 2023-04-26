Assignment 1 : 
# HotelManagement 
Python class to manage hotel room booking.


The HotelTree class includes a  data structure, available_rooms, which is a dictionary that maps room numbers to HotelTreeNode objects. When a new room is added to the hotel, its node is added to available_rooms.

When the traverse_floorwise() method is called, it iterates over all the rooms in the hotel as before. However, when it encounters an available room, it removes it from available_rooms using the del statement.

After the method has finished traversing the hotel, it checks whether available_rooms is empty. If it's not, it finds the first available room by taking the minimum room number in available_rooms.

This optimization reduces the time complexity of finding the first available room to O(1), since we are now just doing a lookup in a dictionary rather than iterating over all the rooms in the hotel. The time complexity of traversing the hotel is still O(MN), where M is the number of floors and N is the number of rooms per floor.

Execute :

python main.py


Assignment 2 : 
graph.md

Basic Graph:
In this basic graph, we represent the entities (Michelin, T40, Peugeot, Toyota, Peugeot 306, and Toyota Supra) as nodes in the graph, and the relationships between them as edges. The labels on the edges represent the type of relationship between the entities.


   (Michelin) ---[is a]---> (Manufacturer) ---[makes]---> (Tires) ---[has model]---> (T40)
                    |                                   |                           |
                    |                                   |                           |
                    +-----[can be fixed on]---------------+                           |
                                                                                        |
                                                                                        |
                                                                                    (Products)
                    |                                   |                           |
                    |                                   |                           |
                    +-----[uses]--------------------------+                           |
                                |                                                       |
                                |                                                       |
                          (Peugeot 306)                               (Toyota Supra)

                          
Improved Graph:
In this improved graph, we represent the entities as nodes, and the relationships between them as edges with additional labels that capture more information about the relationships. We also use different types of edges to represent different types of relationships.
                                      (Michelin)
                                          |
                                          |
                            +-------------[is a manufacturer of]-------------+
                            |                                               |
                       (Tires)                                            (Countries)
                            |                                               |
                            |                                               |
          +----------------[has model T40 that can be fixed on]--------------+
          |                                                                 |
          |                                                                 |
     (Peugeot)                                                        (Toyota)
          |                                                                 |
          |                                                                 |
          +---------[T40 model's durability is average for]-----------------+
                              |                                             |
                              |                                             |
                         (Peugeot 306)                               (Toyota Supra)
In this graph, we distinguish between different types of relationships: Michelin is a manufacturer of tires; the T40 model of tires can be fixed on Peugeot and Toyota products; the durability of the T40 model is average for Peugeot 306 cars and optimal for Toyota Supra cars. We also add additional nodes for countries, which allow us to capture information about where Michelin operates.
