#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length-1)
    current_airport = 'NONE'

    # Populate hash table with ticket information
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    
    for i in range(length-1):
        route[i] = hash_table_retrieve(hashtable, current_airport)
        current_airport = route[i]
    return route
