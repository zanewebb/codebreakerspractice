class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = 1000001
        self.values = [None] * 1000000
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # hashes then puts
        self.values[self.hashKey(key)] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        # hashes then gets
        return self.values[self.hashKey(key)] if self.values[self.hashKey(key)] is not None else -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # hashes then removes value at key
        self.values[self.hashKey(key)] = None
        return
        
    def hashKey(self, key: int) -> int:
        # hashes with modulo using self.M
        return (key % self.M)
