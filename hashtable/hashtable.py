class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.buckets = [None] * int(self.capacity)
        # self.list = None


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # Count number of keys
        keys = 0
        for x in self.buckets:
            if x == None:
                continue
            node = x
            while node:
                keys += 1
                node = node.next
        load_factor = keys / self.capacity
        
        # If LF > 0.7, rehash the table to double its previous size
        if load_factor > 0.07:
            new_capacity = self.capacity * 2
            self.resize(new_capacity=new_capacity)
        elif load_factor < 0.2:
            new_capacity = self.capacity // 2
            self.resize(new_capacity=new_capacity)
        load_factor = keys / self.capacity
        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # hash_num = 5381
        # for char in key:
        #     hash_num = (hash_num * 33) + ord(char)
        # return hash_num
        string_bytes = key.encode()
        hash = 5381
        for i in string_bytes:
            hash = ((hash * 33) ^ i) % 0x100000000
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        ## Linked List attempt
        # Removed self.get_load_factor() because it hit recursion limit when resizing using put()
        node = self._get_node(key=key)
        if node == None:
            node = self.buckets[self.hash_index(key=key)]
            if node == None:
                self.buckets[self.hash_index(key=key)] = HashTableEntry(key=key, value=value)
                # self.get_load_factor()
                return
            while node.next:
                node = node.next
            node.next = HashTableEntry(key=key, value=value)
            # self.get_load_factor()
            return
        else:
            node.value = value
            # self.get_load_factor()
            return

        ## Overwrite attempt
        # self.buckets[self.hash_index(key)] = HashTableEntry(key=key, value=value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        node = self._get_node(key)
        if node == None:
            print("Warning: Key is not found")
        else:
            current_node = self.buckets[self.hash_index(key=key)]

            while current_node:
                # If current node has the key and there is a next node
                ## make the next node, the first node
                if (current_node.key == key) and (current_node.next):
                    self.buckets[self.hash_index(key=key)] = current_node.next
                    self.get_load_factor()
                    return
                # Elif current node has the key and there isn't a next node
                elif (current_node.key == key) and (current_node.next == None):
                    self.buckets[self.hash_index(key=key)] = None
                    self.get_load_factor()
                    return
                # Elif next node has the key
                elif (current_node.next.key == key):
                    current_node.next = current_node.next.next
                    self.get_load_factor()
                    return


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        node = self._get_node(key=key)
        if node == None:
            return None
        else:
            return node.value
    
    def _get_node(self, key):
        """
        Retrieves the node where node.key == key

        Returns None if key is not found
        """
        h_index = self.hash_index(key=key)
        current_node = self.buckets[h_index]
        while current_node != None:
            if key == current_node.key:
                return current_node
            current_node = current_node.next
        return None
        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_table = HashTable(capacity=new_capacity)

        # Loop through the first node of all the linked lists
        for x in self.buckets:
            if x == None:
                continue
            # Loop through all the nodes of each linked list
            node = x
            while node:
                new_table.put(key=node.key,value=node.value)
                node = node.next
        self.capacity = new_capacity
        self.buckets = new_table.buckets
        return



if __name__ == "__main__":
    ht = HashTable(8)
    # print(ht.buckets)
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
