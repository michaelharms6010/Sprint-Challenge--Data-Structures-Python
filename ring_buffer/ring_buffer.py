from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == None:
            self.current=self.storage.head
            
        if len(self.storage) == self.capacity and self.current == self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.current.next
        elif len(self.storage) == self.capacity and self.current == self.storage.tail:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif len(self.storage) >= self.capacity:
            self.current.insert_before(item)
            t = self.current.next
            self.storage.length += 1
            self.storage.delete(self.current)
            self.current = t
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        temp = self.storage.head
        list_buffer_contents.append(temp.value)

        while temp != self.storage.tail:
            temp = temp.next
            list_buffer_contents.append(temp.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.currentindex = 0
        self.storage = [None] * 5

    def append(self, item):
           
        if len(self.storage) == self.capacity:
            self.storage[self.currentindex] = item
            self.currentindex = (self.currentindex + 1) % self.capacity

        else:
            self.storage.append(item)

    def get(self):
        return [i for i in self.storage if i]
