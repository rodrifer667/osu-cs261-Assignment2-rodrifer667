# Name: Fernando I. Rodriguez-Estrada
# OSU Email: rodrifer@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Dynamic Array and ADT Implementation
# Due Date: 02/06/2023
# Description:


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds value to bag data structure.

        parameters:
            value (object): item to be put in bag.

        returns:
            NA
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes item from bag.

        parameters:
            value (object): value to be removed from bag.

        returns:
            (bool): True <= value was removed. False otherwise.
        """
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                self._da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Returns number of occurrences for value in bag.
        """
        value_count = 0
        # increment count if value encountered in bag
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                value_count += 1
        return value_count

    def clear(self) -> None:
        """
        Empties the bag.
        """
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        TO DO: Write this implementation
        """

        equal_bag = True
        hit = 0
        if second_bag.size() != self.size():
            return False
        for i in range(self.size()):
            for j in range(second_bag.size()+1):
                try:
                    if self._da.get_at_index(i) == second_bag._da.get_at_index(j):
                        hit += j
                        break
                except:
                    equal_bag = False
            if equal_bag == False:
                return False
        if second_bag.size() != self.size():
            return False
        return hit ==((second_bag.size()-1)*(second_bag.size()-1 +1)/2)


    def __iter__(self):
        """
        TODO: Write this implementation
        """
        pass

    def __next__(self):
        """
        TODO: Write this implementation
        """
        pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
