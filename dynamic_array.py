# Name: Fernando I. Rodriguez-Estrada
# OSU Email: rodrifer@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Dynamic Array and ADT Implementation
# Due Date: 02/06/2023
# Description:


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Resizes the self.

        The function branches according to whether or not the new_capacity
        is greater than or equal to zero. If the new_capacity is at least 1,
        the function creates a new resized_static_array to update
        self._data by iterate through the indices of the current static
        array that holds the data as it updates the capacity/size. Then,
        the function updates the capacity.
        """

        if new_capacity <= 0 and self._size > 0:
            return

        # capacity is within correct range
        elif new_capacity > 0:
            resized_data_container = StaticArray(new_capacity)
            # append dynamic array value to resized static array for each index
            for data_index in range(self._size):
                # don't append anymore if new capacity reaches size
                if new_capacity < self._size:
                    resized_data_container = self._data
                    new_capacity = self._capacity
                    break
                data_value = self._data.get(data_index)
                resized_data_container.set(data_index, data_value)
            # correct self._size if new capacity is smaller than size
            if new_capacity < self._size:
                new_size = new_capacity
                self._size = new_size
            # update capacity and data
            self._capacity = new_capacity
            self._data = resized_data_container


    def append(self, value: object) -> None:
        """
        Adds the value to the end of the dynamic array.

        Doubles capacity if necessary. Appends the value.

        Parameters:
            value (object): value to be appended

        Returns:
            NA
        """
        # resize if capacity isn't big enough
        if self._size >= self._capacity:
            self.resize(2*self._capacity)

        # append value
        self._data.set(self.length(), value)
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts value at index of DynamicArray.

        First, the function checks that "index" is within the correct range.
        The function breaks down the problem into the case that the capacity is
        too small, case 1 and the case that the capacity is large enough. In
        the first case, the function creates a new data container, "new_data".
        Then, it populates new_data up until "new_data" reaches index. At this
        point, the function populates "index" with "value". Finally,
        the function proceeds to populate "new_data" with the values from
        the old data container. The function proceeds to update the capacity
        and the original data container with the values from "new_data". In
        contrast, if the capacity for the dynamic array is large enough,
        case 2, the function translates the values from the original
        container, "self._data", one space to the right by iterating backwards
        starting at the last index of "self._data". The function sets the
        values of the current index to the value at the previous index until it
        reaches "index". At which point, the function sets the value at
        "index" to "value". Finally, after case 1 and case 2 the function
        increments the size.

        Parameters:
            index (int): index to place value in dynamic array
            value (object): value to place at index in dynamic array

        Returns:
            NA
        """
        # account for invalid index: negative index or out of bounds
        if index < 0 or index >= self._size+1:
            raise DynamicArrayException

        # case 1: capacity is too small
        if self._capacity <= self._size:
            # initialize new container for data
            new_capacity = 2*self._capacity
            new_data = StaticArray(new_capacity)

            # add data values from self._data to new container up to index-1
            for data_index in range(index):
                new_data.set(data_index, self._data.get(data_index))
            # add "value" at "index" in new data container
            new_data.set(index, value)
            # add the rest of the data values from self._data to new container
            for data_index in range(index+1, self._size+1):
                new_data.set(data_index, self._data.get(data_index-1))
            self._capacity = new_capacity
            self._data = new_data
        # case 2: capacity is large enough
        else:
            # shift values to the right
            for data_index in range(self._size, index, -1):
                self._data.set(data_index, self._data.get(data_index - 1))
            # insert "value" at "index"
            self._data.set(index, value)

        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        Removes value at index.

        The function removes the value at the index.

        First, the value makes sure that the index is within range. The,
        the function iterates through the indices of the data starting at
        the value that will be removed. At each iteration, the function sets
        the value at that index to value at the next index. The iteration
        stops after it has reached the last value in the data.

        Parameters:
            index (int): index that holds value in data to be removed

        Returns:
            NA
        """
        # account for invalid index: negative index or out of bounds
        if index < 0 or index >= self._size:
            raise DynamicArrayException

        # size is STRICTLY LESS than a 1/4 of the capacity
        if self._size < 0.25 * self._capacity and self._capacity/2 > 10:
            self.resize(2*self._size)
            # shift values to the left
            for data_index in range(index, self._size - 1):
                self._data.set(data_index, self._data.get(data_index + 1))
        elif self._size < 0.25 * self._capacity and self._capacity > 10 :
            self.resize(10)
            # shift values to the left
            for data_index in range(index, self._size - 1):
                self._data.set(data_index, self._data.get(data_index + 1))
        # size isn't relatively too small
        else:
            # shift values to the left
            for data_index in range(index, self._size-1):
                self._data.set(data_index, self._data.get(data_index+1))

        self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        This function returns new DynamicArray that contains the data from
        the original data between the index bounds of
        [start_index, start_index+size).

        First, the function checks that the bounds of the slice are in the
        correct range. Otherwise, the function raises an exception. Then,
        the function initializes a new DynamicArray, answer. Next,
        the function iterates through the indices starting at
        "start_index" after "size" number of occurrences. At each iteration,
        the function appends the value from self._data at the index to answer.
        Finally, the function returns answer.

        Parameters:
            start_index (int): index from data container for self that holds the
                    value of the first slice
            size (int): the size of the DynamicArray that will be returned

        Returns:
            answer (DynamicArray)
        """

        # invalid size or invalid start index
        if start_index < 0 or start_index >= self._size:
                raise DynamicArrayException
        if size+start_index > self._size or size < 0:
            raise DynamicArrayException

        # append values at index within given bounds of slice
        answer = DynamicArray()
        for data_index in range(start_index, size+start_index):
            answer.append(self._data.get(data_index))

        return answer

    def merge(self, second_da: "DynamicArray") -> None:
        """
        This function merges second_da to self.

        The iterates through the values of second_do. It appends the value
        from second_da to the current dynamic array.

        Parameters:
            second_da (DynamicArray): holds the values that will be appended to
                    self.

        Returns:
            NA
        """
        # capacity too small -> make capacity double of the largest size
        for second_da_index in range(second_da.length()):
            second_da_value = second_da.get_at_index(second_da_index)
            self.append(second_da_value)

    def map(self, map_func) -> "DynamicArray":
        """
        Emulates Python map function.

        The function iterates through the indices of self. At each
        iteration, the function applies the map function to the value
        corresponding to the current index. Then, it appends the value to
        answer. After the function iterates through all the indices,
        it returns answer.
        """

        answer = DynamicArray()
        # appends the value resulting from applying the map function to each
        # value at all the indices
        for self_index in range(self._size):
            answer_value = map_func(self._data.get(self_index))
            answer.append(answer_value)
        return answer

    def filter(self, filter_func) -> "DynamicArray":
        """
        This function imitates the filter function in Python.

        The function creates a new DynamicArray. Then, the function iterates
        through the indices of the data container for self. At each index,
        the function appends the value at the current index if it satisfies
        the criteria laid out by the filter function to the new DynamicArray.
         After the function iterates through all the indices of the data
         container for self, it returns the new DynamicArray.

         Parameters:
             filter_func (function): this is the function that will lay out
                    the criteria for each value to be added to the new
                    DynamicArray.
        Returns:
            result (DynamicArray): this is the data structure that holds the
                    values from self that satisfy the filter function.
        """
        result = DynamicArray()

        for i in range(self._size):
            value = self._data.get(i)
            if filter_func(value):
                result.append(value)

        return result

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This function imitates the Python reduce function.

        The function starts by branching for the case that the input
        includes and does not include an initializer. If the function does
        not have an initializer the first input of reduce_func, value,
        becomes the value held at the first index of self and the second input
        for input becomes the value held at index 1 in self. In the case that
        there is no initializer, the first input value for reduce_func
        becomes the initializer and the second input value for the
        initializer becomes the value store at the 0th index of self. Then,
        the function iterates through the indices of self and cumulatively
        operates with the value as the first input and the value held at the
        given index in the second input. "value" is the output.

        Parameters:
            reduce_func (function): this is the function used to cumulatively
                    operate with "value" and the value held at the given index
                    of self.
            initializer (int): optional value to start the rally.
        Returns:
            value (int):
        """
        if initializer is None:
            value = self._data.get(0)
            start_index = 1
        else:
            value = initializer
            start_index = 0
        for i in range(start_index, self._size):
            value = reduce_func(value, self.get_at_index(i))
        return value

def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    TODO: Write this implementation
    """
    arr_mode_values = DynamicArray()
    frequency_mode = 1
    frequency_previous_value = 1
    for i in range(1, arr.length()):
        previous_value = arr.get_at_index(i-1)
        current_value = arr.get_at_index(i)
        if previous_value == current_value:
            frequency_previous_value += 1
        else:
            if frequency_previous_value == frequency_mode:
                arr_mode_values.append(previous_value)
            elif frequency_previous_value > frequency_mode:
                arr_mode_values = DynamicArray()
                arr_mode_values.append(previous_value)
                frequency_mode = frequency_previous_value
            frequency_previous_value = 1

    return (arr_mode_values, frequency_mode)

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
