#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if not isinstance(size, int):
            print("size must be an integer")
        else:
            self._size = size
        self.condition = "New"

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if not isinstance(new_size, int):
            print("size must be an integer")
        else:
            self._size = new_size

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'

    size = property(get_size, set_size)


shoe_mine = Shoe("mama", "12")