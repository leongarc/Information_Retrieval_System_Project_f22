from abstract import DictAbstract

#LinkedList Class - Zachary Malloy


class _LLNode:

    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.key) + ": " + str(self.value)


# LLDict by Leo Garcia
class LLDict(DictAbstract):

    def __init__(self):
        self._head = None
        self._length = 0
    # String magic method - Leo Garcia
    def __str__(self):
        result = ""
        node = self._head
        if node != None:
            result += str(node.value)
            node = node.next
            while node:
                result += ", " + str(node.value)
                node = node.next
        return result
    # Lenth of LL - Leo Garcia
    def __len__(self):
        return self._length

    def __contains__(self, key):
        return not self._search(key) is None

    def __getitem__(self, key):
        node = self._search(key)
        print(key)
        if node == None:
            raise KeyError("Does not exist888")
        return node.value

    def _search(self, key):
        current = self._head
        while current != None:
            if current.key == key:
                return current  # Key found

            current = current.next

        return None  # Key not found

    def __setitem__(self, key, value):
      self._insert(key, value)
      """
        if self._head == None:
            return None
        else:
            self._insert(key, value)
      """
    # Insert new node to end of list - Leo Garcia
    def _insert(self, key, value):
        new_node = _LLNode(key, value)

        # If the Linked List is empty, then make the
        #    new node as head
        if self._head is None:
            self._head = new_node
            return

        # Else traverse till the last node
        last = self._head
        while (last.next):
            last = last.next

        # Change the next of last node
        last.next = new_node

#Remove/Pop - Zachary Malloy
      
    def pop(self, key):
        value = self[key]
        self._head = self._remove(key)
        self._length -= 1
        return value

    def _remove(self, key):
        assert key is not None, "Does not exist"
