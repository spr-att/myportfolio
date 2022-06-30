class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        self.__trailer = self.__Node(None)
        self.__header = self.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0

    def __len__(self):
        return self.__size

    def append_element(self, val):
        newest = self.__Node(val)
        newest.next = self.__trailer
        self.__trailer.prev.next = newest
        newest.prev = self.__trailer.prev
        self.__trailer.prev = newest
        self.__size += 1

    def __get_node_at(self, index):
        if index < 0 or index >= self.__size or self.__size == 0:
            raise IndexError
        if index <= (self.__size // 2):
            cur = self.__header.next
            for _ in range(index):
                cur = cur.next
            return cur
        if index > (self.__size // 2):
            cur = self.__trailer.prev
            for _ in range(self.__size, index):
                cur = cur.prev
            return cur

    def insert_element_at(self, val, index):
        if index >= self.__size:
            raise IndexError
        if index == self.__size:
            self.append_element(val)
        else:
            cur = self.__get_node_at(index)
            newest = self.__Node(val)
            newest.next = cur
            cur.prev.next = newest
            newest.prev = cur.prev
            cur.prev = newest
            self.__size += 1

    def remove_element_at(self, index):
        cur = self.__get_node_at(index)
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        removed_val = cur.val
        cur.prev = None
        cur.next = None
        cur.val = None
        self.__size -= 1
        return removed_val

    def get_element_at(self, index):
        cur = self.__get_node_at(index)
        return cur.val

    def rotate_left(self):
        if self.__size != 0 and self.__size != 1:
            head = self.__header.next
            self.__header.next = head.next
            self.__trailer.prev.next = head
            head.prev = self.__trailer.prev
            self.__trailer.prev = self.__trailer.prev.next
        
    def __str__(self):
        if self.__size == 0:
            empty_list = "[ ]"
            return empty_list
        if self.__size == 1:
            head_value = self.__header.next.val
            one_list = "[ " + str(head_value) + " ]"
            return one_list
        if self.__size >= 2:
            cur = self.__header.next
            string = "[ "
            for i in range(0, self.__size):
                string = string + str(cur.val)
                if i != self.__size - 1:
                    string = string + ", "
                cur = cur.next
            string = string + " ]"
            return string

    def __iter__(self):
        self.__iter_at = self.__header.next
        return self

    def __next__(self):
        if self.__iter_at == self.__trailer:
            raise StopIteration
        to_return = self.__iter_at.val
        self.__iter_at = self.__iter_at.next
        return to_return

    def __reversed__(self):
        my_reversed_list = Linked_List()
        cur = self.__trailer.prev
        for _ in range(self.__size):
            my_reversed_list.append_element(cur.val)
            cur = cur.prev
        return my_reversed_list

# Unit tests make the main section unnecessary.
#if __name__ == '__main__':
#  pass