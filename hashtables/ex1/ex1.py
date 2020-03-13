#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

import pdb


def get_indices_of_item_weights(weights, length, limit):
    pdb.set_trace()
    ht = HashTable(16)
    """
    YOUR CODE HERE
    """
    for item in range(length):
        # answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
        # weights_3 = [4, 6, 10, 15, 16]
        retrieved = hash_table_retrieve(ht, limit-weights[item])
        print(retrieved)
        if retrieved is not None:
            return (item, retrieved)
        else:
            hash_table_insert(ht, weights[item], item)
    return None

get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
