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
    # Length of LL - Leo Garcia
    def __len__(self):
        return self._length

    def __contains__(self, key):
        return not self._search(key) is None

    def __getitem__(self, key):
        node = self._search(key)
        if node == None:
            raise KeyError("Does not exist")
        return node.value
      
    # Search though list linearly with while loop - Leo Garcia
    def _search(self, key):
        current = self._head
        while current != None: # Search through list linearly
            if current.key == key:
                return current  # Key found

            current = current.next

        return None  # Key not found

    def __setitem__(self, key, value):
      self._insert(key, value)
     
    # Insert new node to end of list - Leo Garcia
    # Geeks 4 Geeks helped with implementation
    def _insert(self, key, value):
        new_node = _LLNode(key, value)

        # If the Linked List is empty, then make the
        #    new node as head
        if self._head is None:
            self._head = new_node
            self._length += 1

            return

        # Else traverse till the last node
        last = self._head
        while (last.next):
            last = last.next
        


        # Change the next of last node
        last.next = new_node
        self._length += 1

#Remove/Pop - Zachary Malloy 
# Geeks for Geeks helped with implementation
    def pop(self, key):
        temp = self._head
 
        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.key == key:
                self._head = temp.next
                temp = None
                self._length -= 1
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.key == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if temp == None:
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None
        self._length -= 1
         
