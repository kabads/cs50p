class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Capacity must be positive")

    def __str__(self):
        print ("🍪" * self.size)

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Jar is full")
        else:
            self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Jar is empty")
        else:
            self.size -= n  

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def set_capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def set_size(self, size):
        self._size = size   
